from prikol import get_joke
from matplotlib import pyplot as plt
from pathlib import Path
import cv2

# CONSTANTS
JPG_FORMAT = "*.jpg"
RGB_WHITE = (255, 255, 255)
RGB_BLACK = (0, 0, 0)
THICKNESS = 5
CONTOUR_IDX = -1

# FOR SINGLE TEST
img_path = "0.jpg"
file_path = "images/dataset/test/"

# PATHS IN MAIN FOLDER
path_dataset_test = Path("dataset/test/")
path_dataset_true = Path("images/dataset/true/")
path_dataset_false = Path("images/dataset/false/")
path_primitives = Path("images/primitives/")


def get_paths(folder_path):
    paths = []
    for path in folder_path.glob(JPG_FORMAT):
        paths.append(path)
    return paths


def process_image_to_demo(path):
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
    axs[1].set_title("Bounding boxes")
    axs[2].set_title("Contours")

    for im, ax in zip(images, axs):
        ax.imshow(im)
    plt.show()

    _, axs_p = plt.subplots(1, len(masks_pts), figsize=(10, 10))

    if len(masks_pts) > 1:
        axs_p = axs_p.flatten()
        for i, ax in enumerate(axs_p.ravel()):
            ax.set_title("Object #{}".format(i))
        for im, ax in zip(objects, axs_p):
            ax.imshow(im)
    else:
        plt.title("Object")
        plt.imshow(objects[0])
    plt.show()


def run_demo(path_dataset):
    paths_images = get_paths(path_dataset)
    for path_image in paths_images:
        process_image_to_demo(path_image)


def main():
    run_demo(path_dataset_test)


if __name__ == '__main__':
    main()
