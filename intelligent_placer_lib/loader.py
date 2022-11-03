import os
from cv2 import imread

JPG_FORMAT = "jpg"


def load_images(path_images):
    if path_images.endswith(JPG_FORMAT):
        _, filename = os.path.split(path_images)
        image = imread(path_images)
        return image, filename
    else:
        images = []
        filenames = []
        for filename in os.listdir(path_images):
            if filename.endswith(JPG_FORMAT):
                images.append(imread(os.path.join(path_images, filename)))
                filenames.append(filename)
        return images, filenames
