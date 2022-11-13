# intellegent_placer
## Постановка задачи
Необходимо определить по фотографии предмета(-ов) и многоугольника, который нарисован черным маркером на белом листе A4, могут ли данные предметы поместиться в этот многоугольник. Все предметы, которые могут использоваться, заранее известны.

### Ввод и вывод
* Программа получает на вход путь до фотографии со всеми объектами и нарисованным многоугольником
* В случае если входные данные корректны, программа может ввести два варианта ответов: либо True (предметы можно поместить в многоугольник) либо False (предметы нельзя поместить в многоугольник). В случае некорректных данных программа выводит False. Корректность данных проверяется исходя из требований к многоугольнику и объектам, которые приведены ниже

## Требования
### Требования к входным данным
* Все изображения должны быть в формате .jpg
* Размер файла не должен превышать 20МБ

### Требования к фотографиям
* Направление камеры – перпендикулярно плоскости, на которой расположены предметы и лист с нарисованным многоугольником
* Фотографии должны быть сделаны при достаточном освещении: объекты на фотографии имеют чёткую границу, отсутствуют засвеченные области и тени высокой интенсивности
* При необходимости можно использовать вспышку (или фонарик) на телефоне, но так, чтобы не было "засветов" на фотографиях
* Объекты и лист А4 с нарисованным многоугольником должны быть размещены на поверхности из тренировочного набора данных

### Требования к многоугольнику
* Многоугольник должен быть замкнутым и выпуклым
* Многоугольник задаётся черным маркером на белом листе бумаги формата А4
* Многоугольник, нарисованный на листе А4, должен полностью помещаться на фотографии
* Многоугольник может иметь любое количество вершин (3 и более)
* Многоугольник должен обязательно присутствовать на фотографии
* Многоугольник может быть только один

### Требования к объектам
* Объекты рассматриваются только из тренировочного набора данных
* Каждый объект может присутствовать на фото только один раз либо не присутствовать вовсе
* На фотографии должен присутствовать хотя бы один объект
* Объекты должны располагаться выше нарисованного многоугольника (выше верхней точки многоугольника)
* Объекты не должны пересекаться с листом бумаги
* Объекты не должны пересекаться друг с другом
* Объекты не должны пересекаться с многоугольником
* Объекты должны располагаться вне многоугольника
* Объекты должны целиком помещаться на фотографии

### Требования к выводу результата
* Программа выводит ответ в стандартный поток вывода
* Программа отвечает False если входные данные некорректны
* Программа отвечает True, если предметы можно поместить в многоугольник
* Программа отвечает False, если предметы нельзя поместить в многоугольник

### Дополнительные требования
* Дыры, находящиеся внутри объектов, не учитываются в работе программы, в них нельзя будет поместить объекты

# План решения задачи
НА ДАННЫЙ МОМЕНТ ПЛАН НЕ ДЕЙСТВИТЕЛЕН, КАК ОБЫЧНО ВСЕ ПОШЛО НЕ ПО ПЛАНУ, ПОЭТОМУ ПРОСЬБА НЕ СМОТРЕТЬ НА НЕГО. СПАСИБО
1. Найти на изображении поверхность из набора данных (белые листы А4, которые наложены друг на друга) и обрезать лишние края (черный стол)
2. Найти на поверхности многоугольник, нарисованный черными маркером. Предполагается искать его по цвету маркера
3. Найти на изображении все остальные объекты, находящиеся выше (наивысшей вершины) многоугольника. Предполагается искать их по сильному контрасту с фоном или наличию "шумов" на краях объектов
4. Проверить частные случаи, представленные в тестовом наборе данных (отсутствие многоугольника, незамкнутость многоугольника и т.д.)
5. Построить для найденных объектов маленькие многоугольники, в которые они помещаются (так называемая оболочка объекта)
6. Проверка оставшихся частных случаев, представленных в тестовом наборе данных
7. Проверка наличия очевидных решений. Например, сумма площадей оболочек объектов больше площади многоугольника. В этом случае объекты точно нельзя расположить внутри многоугольника
8. Расположить маленькие многоугольники внутри большого. Начинать с наибольшего по площади объекта, переходя к более маленьким. Пока что предполагается делать это созданием конечного множества всех возможных положений объектов (в том числе учитывая поворот объекта) и решить задачу перебором. Но это может повлечь за собой чрезмерную затрату временных ресурсов. Поэтому данный пункт будет доработан

## Замечания
План может быть переработан в дальнейшем. Все идеи по улучшению будут появляться в данном параграфе "замечания", а в случае их принятия, они будут перемещены в основной план

# Изображения используемых объектов
[Ссылка на объекты](images/primitives)

# Датасет
[Ссылка на датасет](images/dataset)   
[Ссылка на тестовые примеры](images/dataset/test)
