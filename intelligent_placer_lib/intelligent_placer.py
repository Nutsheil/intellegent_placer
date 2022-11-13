import cv2
import numpy as np
from intelligent_placer_lib.contours import get_contours, get_contours_v2
from intelligent_placer_lib.loader import load_pictures
from intelligent_placer_lib.structure import Picture, Polygon, Item, Primitive
from intelligent_placer_lib.algorithm import my_first_algorithm
from intelligent_placer_lib.show import \
    show_primitives_with_contours, \
    fill_field_contours, \
    show_picture


def compress_image(image, scale):
    new_size = (int(image.shape[1] * scale), int(image.shape[0] * scale))
    return cv2.resize(image, new_size)


def split_items_and_polygon(picture, contours):
    picture.polygon = Polygon([contours[0]])
    for i in range(1, len(contours)):
        picture.items.append(Item([contours[i]]))
    picture.sort_items()
    return


def placer(path_image):
    pictures = load_pictures(path_image)
    for picture in pictures:
        picture.image = compress_image(picture.image, 0.5)
        contours = get_contours(picture.image)
        # contours = get_contours_v2(picture.image)
        split_items_and_polygon(picture, contours)
        fill_field_contours(picture)
        show_picture(picture)
        result = my_first_algorithm(picture)
        print(picture.name, " result: ", result)


def init_items(path_items):
    pictures = load_pictures(path_items)
    primitives = []
    for picture in pictures:
        picture.image = compress_image(picture.image, 0.2)
        contour = get_contours(picture.image)
        if len(contour) > 0:
            primitives.append(Primitive(picture.image, picture.name, contour))

    show_primitives_with_contours(primitives)

    return
