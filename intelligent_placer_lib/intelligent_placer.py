import cv2
import numpy as np
from shapely.geometry import Polygon
from intelligent_placer_lib.contours import get_contours
from intelligent_placer_lib.loader import load_pictures
from intelligent_placer_lib.structure import Picture
from intelligent_placer_lib.algorithm import my_second_algorithm
from intelligent_placer_lib.show import fill_field_contours, show_picture

SCALE = 0.5                         # Коэффициент сжатия изображения (крупные изображения, лучше сжимать)
SIMPLIFY = 5                        # Сглаживание многоугольника класса Polygon


# Функция сжатия изображения
def compress_image(image: np.ndarray, scale: float):
    new_size = (int(image.shape[1] * scale), int(image.shape[0] * scale))
    return cv2.resize(image, new_size)


# Функция сжатия всех изображений (потому что изображения 2: BGR и RGB)
def compress_picture(picture: Picture, scale: float):
    picture.image = compress_image(picture.image, scale)
    picture.image_RGB = compress_image(picture.image_RGB, scale)


# Функция разделения контуров на контур многоугольника и контуры предметов
def split_items_and_polygon(picture: Picture, contours):
    picture.figure_contour = contours[0]

    items_contours = []
    for i in range(1, len(contours)):
        items_contours.append(contours[i])
    items_contours.sort(key=lambda x: cv2.contourArea(x), reverse=True)             # Отсортировать предметы по площади

    picture.items_contours = items_contours


# Функция создания полигонов (class Polygon from shapely.geometry) из контуров
def set_polygons_from_contours(picture: Picture):
    picture.figure_polygon = Polygon(picture.figure_contour[:, 0]).simplify(SIMPLIFY)
    picture.items_polygons = tuple(Polygon(contour[:, 0]).simplify(SIMPLIFY) for contour in picture.items_contours)


# Основная функция пакета intelligent_placer
def placer(path_image: str, show_results=True) -> bool or [bool]:
    pictures = load_pictures(path_image)                        # Считать изображение(я), поданное(ые) на вход
    results = []

    for picture in pictures:
        compress_picture(picture, SCALE)                        # Сжать изображение для ускорения работы
        contours = get_contours(picture.image)                  # Найти на изображении все контуры
        split_items_and_polygon(picture, contours)              # Разделить контуры на многоугольник и объекты
        set_polygons_from_contours(picture)                     # По полученным контурам создать полигоны
        fill_field_contours(picture)                            # Заполнить поля класса для вывода изображений
        results.append(my_second_algorithm(picture))            # Применить алгоритм нахождения оптимального положения
        if show_results:
            show_picture(picture)                               # Вывести изображения на экран

    if len(pictures) == 0:
        return None
    if len(pictures) == 1:
        return results[0]

    return results
