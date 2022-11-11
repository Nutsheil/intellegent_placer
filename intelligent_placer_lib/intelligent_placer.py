import cv2
import numpy as np
from intelligent_placer_lib.contours import get_contours_v1
from intelligent_placer_lib.loader import load_images
from intelligent_placer_lib.structure import Picture, Polygon, Item, Primitive
from intelligent_placer_lib.algorithm import my_first_algorithm
from intelligent_placer_lib.show import \
    show_images_and_contours, \
    show_images_with_contours, \
    show_primitives_with_contours


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
    images, filenames = load_images(path_image)
    pictures = []
    for image, filename in zip(images, filenames):
        image = compress_image(image, 0.5)
        contours = get_contours_v1(image)
        picture = Picture(image, filename, contours)
        split_items_and_polygon(picture, contours)
        pictures.append(picture)

    show_images_and_contours(pictures)
    # show_images_with_contours(pictures)

    for picture in pictures:
        result = my_first_algorithm(picture)
        print(picture.name, " result: ", result)


def init_items(path_items):
    images, filenames = load_images(path_items)
    primitives = []
    for image, filename in zip(images, filenames):
        image = compress_image(image, 0.2)
        contour = get_contours_v1(image)
        if len(contour) > 0:
            primitives.append(Primitive(image, filename, contour))

    show_primitives_with_contours(primitives)

    return
