import cv2
import numpy as np
from matplotlib import pyplot as plt
from intelligent_placer_lib.structure import Picture, Polygon, Item

RGB_WHITE = (255, 255, 255)
RGB_RED = (255, 0, 0)
RGB_GREEN = (0, 255, 0)
RGB_BLUE = (0, 0, 255)
RGB_BLACK = (0, 0, 0)
THICKNESS = 5
CONTOUR_IDX = -1


def fill_field_contours(picture: Picture):
    height = picture.image.shape[0]
    width = picture.image.shape[1]
    picture.image_contours_only = np.zeros((height, width, 3), np.uint8)
    picture.image_with_contours = picture.image.copy()
    for item in picture.items:
        cv2.drawContours(picture.image_contours_only, item.contour, CONTOUR_IDX, RGB_RED, THICKNESS)
        cv2.drawContours(picture.image_with_contours, item.contour, CONTOUR_IDX, RGB_RED, THICKNESS)

    cv2.drawContours(picture.image_contours_only, picture.polygon.contour, CONTOUR_IDX, RGB_GREEN, THICKNESS)
    cv2.drawContours(picture.image_with_contours, picture.polygon.contour, CONTOUR_IDX, RGB_GREEN, THICKNESS)


def show_picture(picture: Picture, contours_only=True, with_contours=True):
    image_count = 1 + contours_only + with_contours
    _, axs = plt.subplots(1, image_count, figsize=(12, 12))

    index = 0

    axs[index].set_title(picture.name)
    axs[index].imshow(picture.image)
    index += 1

    if contours_only:
        axs[index].set_title("Items count: {}".format(len(picture.items)))
        axs[index].imshow(picture.image_contours_only)
        index += 1

    if with_contours:
        axs[index].set_title("Items count: {}".format(len(picture.items)))
        axs[index].imshow(picture.image_with_contours)
        index += 1

    plt.show()


def show_primitives_with_contours(primitives):
    for primitive in primitives:
        _, axs = plt.subplots(1, 2, figsize=(12, 12))
        image_contours = primitive.image.copy()
        cv2.drawContours(image_contours, primitive.contour, CONTOUR_IDX, RGB_RED, THICKNESS)
        axs[0].set_title(primitive.name)
        axs[1].set_title("contour")
        axs[0].imshow(primitive.image)
        axs[1].imshow(image_contours)
        plt.show()
    return
