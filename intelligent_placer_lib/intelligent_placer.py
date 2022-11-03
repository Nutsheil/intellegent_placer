from matplotlib import pyplot as plt
from intelligent_placer_lib.contours import get_contours_v1
from intelligent_placer_lib.loader import load_images
from intelligent_placer_lib.show import show_images_and_contours
import cv2

# CONSTANTS
JPG_FORMAT = "*.jpg"
RGB_WHITE = (255, 255, 255)
RGB_BLACK = (0, 0, 0)
THICKNESS = 5
CONTOUR_IDX = -1


def placer(path_image):
    images, filenames = load_images(path_image)
    contours = []
    for image in images:
        contour = get_contours_v1(image.copy())
        contours.append(contour)
    show_images_and_contours(images, contours)


def placer_v2(path_image):
    images, filenames = load_images("images/primitives/v1")
    _, axs = plt.subplots(len(images), 3, figsize=(12, 12))
    # axs = axs.flatten()
    # axs[0].set_title("Original image")
    # axs[1].set_title("Bounding boxes")
    # axs[2].set_title("Contours")
    index = 0
    for image in images:
        contours = get_contours_v1(image.copy())

        image_bbox = image.copy()
        image_contours = image.copy()

        cv2.drawContours(image_contours, contours, CONTOUR_IDX, RGB_WHITE, THICKNESS)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            image_bbox = cv2.rectangle(image_bbox, (x, y), (x + w, y + h), RGB_BLACK, THICKNESS)

        # axs[0][0].imshow(image)
        axs[index][0].imshow(image)
        axs[index][1].imshow(image_bbox)
        axs[index][2].imshow(image_contours)
        index = index+1

    plt.show()
