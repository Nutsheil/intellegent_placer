import cv2
from matplotlib import pyplot as plt
import numpy as np

RGB_WHITE = (255, 255, 255)
RGB_BLACK = (0, 0, 0)
THICKNESS = 5
CONTOUR_IDX = -1


def show_images_and_contours(images, contours):
    for image, contour in zip(images, contours):
        _, axs = plt.subplots(1, 2, figsize=(12, 12))
        height = image.shape[0]
        width = image.shape[1]
        print("height / width: ", height, " / ", width)
        image_contours = np.zeros((height, width, 3), np.uint8)
        cv2.drawContours(image_contours, contour, CONTOUR_IDX, RGB_WHITE, THICKNESS)
        axs[0].set_title("Original image")
        axs[1].set_title("Contours count: {}".format(len(contour)))
        axs[0].imshow(image)
        axs[1].imshow(image_contours)
        plt.show()
    return
