import numpy as np
from cv2 import cvtColor, COLOR_BGR2RGB


# Класс изображения для более удобной работы
class Picture:
    def __init__(self, image: np.ndarray, name:str):
        self.name = name                                            # Имя файла
        self.image = image                                          # Само изображения (формат BGR)
        self.image_RGB = cvtColor(image, COLOR_BGR2RGB)             # Изображение в формате RGB
        self.image_with_contours = None                             # Исходное изображение с контурами
        self.image_contours_only = None                             # Изображение с контурами на черном фоне
        self.items_contours = None                                  # Контуры предметов
        self.items_polygons = None                                  # Полигоны (class Polygon) предметов
        self.figure_contour = None                                  # Контур многоугольника
        self.figure_polygon = None                                  # Полигон (class Polygon) многоугольника
