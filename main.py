from prikol import get_joke
from matplotlib import pyplot as plt
from pathlib import Path
import cv2

JPG_FORMAT = "*.jpg"
RGB_WHITE = (255, 255, 255)
RGB_BLACK = (0, 0, 0)
THICKNESS = 5
CONTOUR_IDX = -1

img_path = "0.jpg"
file_path = "images/dataset/test/"

tests_path = Path("images/dataset/test/")


def get_paths(path):
    paths = []
    for path in path.glob(JPG_FORMAT):
        paths.append(path)
    return paths


def demonstration_test(path_tests):
    paths = get_paths(path_tests)
    for path in paths:
        image = cv2.imread(str(path))
        image = cv2.resize(image, (image.shape[1] // 4, image.shape[0] // 4))
        img, masks_pts = get_joke(image.copy())

        bounding_box = img.copy()
        contours = img.copy()

        cv2.drawContours(contours, masks_pts, CONTOUR_IDX, RGB_WHITE, THICKNESS)
        objects = []
        for poly in masks_pts:
            x, y, w, h = cv2.boundingRect(poly)
            bounding_box = cv2.rectangle(bounding_box, (x, y), (x + w, y + h), RGB_BLACK, THICKNESS)
            cv2.drawContours(img, masks_pts, CONTOUR_IDX, RGB_WHITE, THICKNESS)
            objects.append(img[y: y + h, x: x + w])

        images = [image, bounding_box, contours]

        _, axs = plt.subplots(1, 3, figsize=(10, 10))
        axs = axs.flatten()
        axs[0].set_title("Original image")
        axs[1].set_title("With bounding boxes")
        axs[2].set_title("With contours")

        for im, ax in zip(images, axs):
            ax.imshow(im)
        plt.show()

        _, axs_p = plt.subplots(1, len(masks_pts), figsize=(10, 10))

        if len(masks_pts) > 1:
            axs_p = axs_p.flatten()
            for i, ax in enumerate(axs_p.ravel()):
                ax.set_title("contour #{}".format(i))
            for im, ax in zip(objects, axs_p):
                ax.imshow(im)
        else:
            plt.title("contour")
            plt.imshow(objects[0])
        plt.show()


def main():
    demonstration_test(tests_path)


if __name__ == '__main__':
    main()
