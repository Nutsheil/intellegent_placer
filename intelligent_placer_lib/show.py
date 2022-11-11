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


def show_images_and_contours(pictures):
    for picture in pictures:
        _, axs = plt.subplots(1, 2, figsize=(12, 12))
        height = picture.image.shape[0]
        width = picture.image.shape[1]
        image_contours = np.zeros((height, width, 3), np.uint8)

        for item in picture.items:
            cv2.drawContours(image_contours, item.contour, CONTOUR_IDX, RGB_RED, THICKNESS)

        cv2.drawContours(image_contours, picture.polygon.contour, CONTOUR_IDX, RGB_GREEN, THICKNESS)

        axs[0].set_title(picture.name)
        axs[1].set_title("Items count: {}".format(len(picture.items)))
        axs[0].imshow(picture.image)
        axs[1].imshow(image_contours)
        plt.show()
    return


def show_images_with_contours(pictures):
    for picture in pictures:
        _, axs = plt.subplots(1, 2, figsize=(12, 12))
        image_contours = picture.image.copy()

        for item in picture.items:
            cv2.drawContours(image_contours, item.contour, CONTOUR_IDX, RGB_RED, THICKNESS)

        cv2.drawContours(image_contours, picture.polygon.contour, CONTOUR_IDX, RGB_GREEN, THICKNESS)

        axs[0].set_title(picture.name)
        axs[1].set_title("Items count: {}".format(len(picture.items)))
        axs[0].imshow(picture.image)
        axs[1].imshow(image_contours)
        plt.show()
    return


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
