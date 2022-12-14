import os
from cv2 import imread
from intelligent_placer_lib.structure import Picture

JPG_FORMAT = "jpg"              # Формат исходных изображений


# Функция считывания изображений из директории (возвращает экземпляр класса Picture)
def load_pictures(path_images):
    if path_images.endswith(JPG_FORMAT):
        _, filename = os.path.split(path_images)
        image = imread(path_images)
        return [Picture(image, filename)]
    else:
        pictures = []
        for filename in os.listdir(path_images):
            if filename.endswith(JPG_FORMAT):
                pictures.append(Picture(imread(os.path.join(path_images, filename)), filename))
        return pictures
