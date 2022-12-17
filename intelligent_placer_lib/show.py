import cv2
import os.path
import numpy as np
from matplotlib import pyplot as plt
from intelligent_placer_lib.structure import Picture

RGB_WHITE = (255, 255, 255)                     # Белый цвет
RGB_RED = (255, 0, 0)                           # Красный цвет
RGB_GREEN = (0, 255, 0)                         # Зеленый цвет
RGB_BLUE = (0, 0, 255)                          # Синий цвет
RGB_BLACK = (0, 0, 0)                           # Черный цвет
THICKNESS = 5                                   # Толщина линии
CONTOUR_IDX = -1                                # Параметр иерархии контуров


# Функция заполнения полей класса Picture для дальнейшего вывода изображений на экран
def fill_field_contours(picture: Picture):
    height = picture.image.shape[0]
    width = picture.image.shape[1]
    picture.image_contours_only = np.zeros((height, width, 3), np.uint8)            # Пустое черное изображение
    picture.image_with_contours = picture.image_RGB.copy()                          # Копия оригинала

    # Отрисовка контуров предметов на копии оригинала и пустом черном изображении
    for contour in picture.items_contours:
        cv2.drawContours(picture.image_contours_only, [contour], CONTOUR_IDX, RGB_RED, THICKNESS)
        cv2.drawContours(picture.image_with_contours, [contour], CONTOUR_IDX, RGB_RED, THICKNESS)

    # Отрисовка контуров многоугольника на копии оригинала и пустом черном изображении
    cv2.drawContours(picture.image_contours_only, [picture.figure_contour], CONTOUR_IDX, RGB_GREEN, THICKNESS)
    cv2.drawContours(picture.image_with_contours, [picture.figure_contour], CONTOUR_IDX, RGB_GREEN, THICKNESS)


# Функция вывода изображений на экран
def show_picture(picture: Picture,  with_contours=True, contours_only=True, result=True):
    image_count = 1 + with_contours + contours_only + result        # Количество изображений
    _, axs = plt.subplots(1, image_count, figsize=(12, 12))

    index = 0

    # Исходное изображение
    axs[index].set_title(picture.name)
    axs[index].imshow(picture.image_RGB)
    index += 1

    # Копия исходного изображения с контурами
    if with_contours:
        axs[index].set_title(f"Items count: {len(picture.items_contours)}")
        axs[index].imshow(picture.image_with_contours)
        index += 1

    # Контуры на пустом черном изображении
    if contours_only:
        axs[index].set_title(f"Items count: {len(picture.items_contours)}")
        axs[index].imshow(picture.image_contours_only)
        index += 1

    # Результат размещения предметов в многоугольнике
    if result:
        if os.path.exists(f"images/results/{picture.name}"):
            axs[index].set_title("result")
            axs[index].imshow(plt.imread(f"images/results/{picture.name}"))

    plt.show()
