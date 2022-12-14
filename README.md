# intelligent_placer
## Постановка задачи
Необходимо определить по фотографии предмета(-ов) и многоугольника, который нарисован черным маркером на белом листе A4, могут ли данные предметы поместиться в этот многоугольник. Все предметы, которые могут использоваться, заранее известны.

### Ввод и вывод
* Программа получает на вход путь до фотографии со всеми объектами и нарисованным многоугольником
* В случае если входные данные корректны, программа может ввести два варианта ответов: либо True (предметы можно поместить в многоугольник) либо False (предметы нельзя поместить в многоугольник). В случае некорректных данных программа выводит False. Корректность данных проверяется исходя из требований к многоугольнику и объектам, которые приведены ниже

## Требования
### Требования к входным данным
* Все изображения должны быть в формате .jpg
* Все изображения находятся в папке *"./images/dataset"* (можно изменять)
* Файл *"info.xlsx"* содержит в себе точное название изображения, правильный ответ и описание к изображению (не является обязательным, но удобен для тестирования)

### Требования к фотографиям
* Направление камеры – перпендикулярно плоскости, на которой расположены предметы и лист с нарисованным многоугольником
* Фотографии должны быть сделаны при достаточном освещении: объекты на фотографии имеют чёткую границу, отсутствуют засвеченные области и тени высокой интенсивности
* При необходимости можно использовать вспышку (или фонарик) на телефоне, но так, чтобы не было "засветов" на фотографиях
* Предметы и нарисованный многоугольником должны быть размещены на поверхности из тренировочного набора данных (строгое требование)

### Требования к многоугольнику
* Многоугольник должен быть выпуклым (высока вероятность, что может быть и невыпуклым, но не должен содержать в себе дыры)
* Многоугольник задаётся черным маркером на белом листе бумаги формата А4
* Многоугольник, нарисованный на листе А4, должен полностью помещаться на фотографии
* Многоугольник может иметь любое количество вершин (3 и более)
* Многоугольник должен обязательно присутствовать на фотографии
* Многоугольник может быть только один

### Требования к предметам
* Предметы рассматриваются только из тренировочного набора данных (хотя на самом деле можно использовать любые объекты в разумных пределах)
* Предмет может присутствовать на фотографии дважды (например: две одинаковые ручки)
* На фотографии могут не присутствовать предметы (в то время как многоугольник должен быть всегда)
* Предметы должны располагаться выше нарисованного многоугольника (выше верхней точки многоугольника)
* Предметы не должны пересекаться друг с другом
* Предметы не должны пересекаться с многоугольником
* Предметы должны располагаться вне многоугольника
* Предметы должны целиком помещаться на фотографии

### Требования к выводу результата
* Программа выводит ответ в стандартный поток вывода
* Программа отвечает True, если предметы можно поместить в многоугольник
* Программа отвечает False, если предметы нельзя поместить в многоугольник
* Для наглядности программа может выводить изображения на экран

### Дополнительные требования
* Дыры, находящиеся внутри предметов, не учитываются в работе программы, такие предметы будут расцениваться как предмет без дыры (например, тор будет расцениваться как окружность)

## План решения задачи
1. Считать изображение, поданное на вход (возвращается экземпляр класса Picture)
2. Сжать изображение для ускорения работы
3. Найти на изображении все контуры
   + После обнаружения отфильтровать их по минимальной площади, чтобы исключить "фантомные" контуры
4. Разделить контуры на многоугольник и предметы
   + Так как многоугольник на фотографии всегда располагается ниже предметов, то он всегда будет самым первым контуром
   + Все остальные контуры, кроме первого, принадлежат предметам
5. По полученным контурам создать полигоны *(class Polygon from shapely.geometry)*
6. Заполнить оставшиеся поля класса Picture (для дальнейшего вывода изображений)
7. Применить алгоритм нахождения оптимального положения предметов в многоугольнике
8. Вывести изображение на экран (исходное, контуры и результат) (опционально)
9. Сравнить полученный результат (True/False) с верным (True/False) (опционально)

### Алгоритм нахождения оптимального расположения
Алгоритм основан на минимизации функции, определяющей оптимальное расположение предметов,
с помощью метода дифференциальной эволюции *(differential_evolution from scipy.optimize)*, 
который выполняется несколько раз для улучшения качества решения.  
Функция цели, которая определяет оптимальное расположение предметов в многоугольнике учитывает в себе 2 параметра: 
площадь пересечения многоугольника с предметом и расстояние от центра предмета до центра многоугольника.  
Метод дифференциальной эволюции, в свою очередь, перемещает и вращает предмет в многоугольнике. 
В качестве параметров в метод передаются так называемые "степени свободы" предмета (перемещение по ширине, высоте и вращение).  
Метод запускается N раз, чтобы улучшить точность найденной позиции.  
После чего найденное положение предмета отсекается из многоугольника.  
То есть, если простыми словами, алгоритм для каждого предмета находит оптимальное положение максимально близко
к границе многоугольника, а затем вырезает из многоугольника кусок, где находится предмет.  
Сам алгоритм выглядит следующим образом:
1. Сделать базовую проверку на наличие предметов и сумму их площадей
2. Нарисовать многоугольник (для наглядности результата)
3. Для каждого предмета выполнить шаги 4-14
4. Перенести предмет в центр многоугольника
5. Для заданного количества итераций выполнить шаги 6-8
6. Найти ширину и высоту многоугольника
7. Запустить метод дифференциальной эволюции с параметрами перемещения по высоте и ширине и параметром поворота предмета
8. Найденные методом дифференциальной эволюции параметры перемещения предмета и значение функции сохранить в словарь
9. Найти минимальное значение функции среди всех полученных значений и взять из словаря соответствующие параметры
10. Переместить предмет по найденным параметрам (сдвиг по осям и поворот)
11. Нарисовать предмет (для наглядности результатов)
12. Найти площадь фигуры, принадлежащей предмету, но лежащей вне многоугольника. 
    Сравнить ее с максимальной погрешностью вычисления (Если просто сравнивать с нулем, 
    то ответ будет неверным, так как всегда найдутся хотя бы 1-2 точки, лежащие максимально близко
    к границе многоугольника, но вне него). В случае превышения погрешности вывести результат 
    False и закончить работу функции
13. Вырезать из многоугольника предмет, и рассматривать дальше уже меньший многоугольник
14. Очистить словарь параметров перемещения предмета
15. Сохранить все нарисованные объекты (для наглядности результата)

## Возможные улучшения
1. Сопоставлять по особым точкам предметы на фотографии с заранее известными предметами.
   Таким образом можно будет на результирующем изображении отображать не только контуры,
   а объекты целиком как они есть (выглядело бы гораздо эффектнее)
2. Использовать более сложную функцию определения оптимального расположения (например, добавить в нее веса)
3. Использовать другой алгоритм распознавания контуров многоугольника и предметов, 
   чтобы была возможность подать на вход фотографию с предметами, но без многоугольника, или же предметы и многоугольник с дырами

## Дополнительная информация
Помимо метода *differential_evolution* из библиотеки *scipy.optimize* так же были рассмотрены методы
*dual_annealing*, *shgo*, *direct*. В итоге были получены следующие результаты:
+ Метод *dual_annealing* выдает чуть меньшую погрешность вычисления, но работает в 4 раза дольше метода *differential_evolution*
+ Метод *shgo* работает в 3 раза быстрее метода *differential_evolution*, но выдает ошибку на более сложных тестах
+ Метод *direct* работает 2.5 раза дольше метода *differential_evolution*, но прижимает объекты не максимально плотно к границе и в основном ставит их под углом. Хотя все тесты он прошел успешно   

## Итоги
1. Метод *differential_evolution* оказался наиболее подходящим для данной задачи. 
   Десять предметов были успешно размещены в многоугольнике за 47 секунд 
2. Алгоритм имеет очень высокую точность. Все проведенные тесты были решены верно
3. Преимущество данного алгоритма в том, что он располагает предметы равномерно
   по границам многоугольника, из-за чего повышается плотность упаковки
4. Можно добиться большей точности, если не так сильно упрощать полигоны и проводить больше итераций,
   но из-за этого очень сильно возрастет время работы программы


## Замечания
Так же мне хотелось бы выразить особую благодарность моему коллеге Дмитрию Веселому
за помощь с реализацией алгоритма. Он вдохновил меня на использование методов глобальной оптимизации
для решения данной задачи (а именно библиотеки *scipy.optimize*) и помог составить формулу для оптимизации.

# Навигация по файлам
[Ссылка на объекты](images/primitives)  
[Ссылка на датасет](images/dataset)  
[Ссылка на результаты](images/results)  
[Демонстрационный файл](demonstration.ipynb)


---------------
Редченко Евгений Юрьевич  
СПБПУ, ФизМех, гр.5030102/90401  
Лабораторная работа "Intelligent placer" по предмету "машинное обучение"  
14 декабря 2022 г.
