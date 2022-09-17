# intellegent_placer
## Постановка задачи
Необходимо по фотографии одного или нескольких предметов и многоугольника, который нарисован черным маркером на белом листе A4, определить, могут ли каким-либо образом данные предметы одновременно, поместиться в этот многоугольник. Предметы не должны перекрывать друг друга. Все предметы, которые могут оказаться на фотографии, заранее известны.

### Общее
* Программа получает на вход путь до изображения со всеми объектами и нарисованным на листе многоугольником
* Программа должна выдать ответ хотя бы за 15 минут
* Программа должна вывести ответ True (предметы можно поместить в многоугольник) либо False (предметы нельзя поместить в многоугольник)
* Ответ выводится в стандартный поток вывода

## Требования
### Требования к изображениям
* Все изображения в формате .jpg
* Угол между направлением камеры и перпендикуляром к поверхности должен быть не более 15°
* Фотографии сделаны при дневном освещении. Объекты на фотографии имеют чёткую границу, отсутствуют засвеченные области и тени высокой интенсивности
* Фотографии цветные, без цветовой коррекции и наложения фильтров
* Объекты и многоугольник должны быть размещены на светлой поверхности из тренировочного набора данных

### Требования к многоугольнику
* Многоугольник должен быть замкнут
* Многоугольник должен быть выпуклым
* Многоугольник задаётся черным маркером на белом листе бумаги.

### Требования к объектам
* Объекты рассматриваются только из тренировочного набора данных
* Один объект присутствовать на фото только один раз
* Объекты и многоугольник должны быть размещены на белой поверхности
* Объекты не должны пересекаться друг с другом
* Объекты не должны пересекаться с многоугольником
* Объекты и многоугольник должны целиком помещаться на фото
* Объекты должны распологаться вне многоугольника
* Программа расценивает любые снятые объекты как абсолютно твёрдые тела
* Дыры внутри объектов не учитываются при работе программы

### Требования к выводу
* Программа отвечает False если входные данные некорректны
* Программа отвечает True, если предметы можно поместить в многоугольник
* Программа отвечает False, если предметы нельзя поместить в многоугольник
