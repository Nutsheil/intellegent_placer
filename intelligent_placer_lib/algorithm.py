import numpy as np
from shapely.geometry import Polygon
from shapely.affinity import rotate, translate
from matplotlib import pyplot as plt
from scipy.optimize import differential_evolution
from intelligent_placer_lib.structure import Picture

ITERATIONS = 10                             # Количество повторений метода дифференциальной эволюции
ALLOWABLE_ERROR = 2                         # Максимальная погрешность площадей
PATH_RESULT = "images/results/"             # Папка для сохранения изображений


# Функция отрисовки полигона
def plot_polygon(polygon: Polygon, color_flag: str):
    polygon_rings = list(polygon.exterior.coords)
    plt.plot([point[0] for point in polygon_rings], [point[1] for point in polygon_rings], color_flag)


# Функция сохранения изображения
def save_plot(picture: Picture):
    plt.axis('off')
    plt.savefig(PATH_RESULT + picture.name, bbox_inches='tight', pad_inches=0)
    plt.close()


# Функция сохранения результата "False"
def save_false_plot(picture: Picture):
    plt.clf()
    plt.text(0.5, 0.5, 'FALSE', ha='center', va='center', fontsize=28, color='red')
    save_plot(picture)


# Функция вычисления центра полигона
def get_polygon_center(polygon: Polygon):
    polygon_centroid = polygon.centroid
    return polygon_centroid.x, polygon_centroid.y


# Функция вычисления ширины и высоты полигона (bounding boxes)
def get_polygon_frame(polygon: Polygon):
    bounds = polygon.bounds
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    return width, height


# Функция вычисления расстояния между двумя точками
def get_dist(point_1: (float, float), point_2: (float, float)):
    distance = np.sqrt(sum(pow(a - b, 2) for a, b in zip(point_1, point_2)))          # Формула расстояния между точками
    return distance


# Функция вычисления расстояния между центрами двух полигонов
def dist_between_centers(polygon1: Polygon, polygon2: Polygon):
    polygon1_center = get_polygon_center(polygon1)
    polygon2_center = get_polygon_center(polygon2)
    distance = get_dist(polygon1_center, polygon2_center)
    return distance


# Алгоритм размещения предметов в многоугольнике
def my_second_algorithm(picture: Picture):
    figure = picture.figure_polygon
    items = picture.items_polygons
    my_dict = {}                                # Словарь, для сохранения результатов

    # Базовая проверка на наличие предметов и сумму площадей
    if len(items) == 0 or figure.area < sum([item.area for item in items]):
        save_false_plot(picture)
        return False

    plot_polygon(figure, 'g')                   # Отрисовка многоугольника

    for item in items:
        # Перемещение предмета в центр многоугольника
        item_center = get_polygon_center(item)
        figure_center = get_polygon_center(figure)
        item = translate(item, xoff=figure_center[0] - item_center[0], yoff=figure_center[1] - item_center[1])

        # Несколько итераций, для нахождения наилучшего решения. Чем больше, тем точнее, но медленнее
        for _ in range(ITERATIONS):
            # Критерий нахождения оптимального положения
            def criterion(args):
                item_replaced = rotate(translate(item, xoff=args[0], yoff=args[1]), args[2])
                return -figure.intersection(item_replaced).area - dist_between_centers(item_replaced, figure)

            # Метод дифференциальной эволюции, куда передаются перемещения по x, y и вращение
            width, height = get_polygon_frame(figure)
            result = differential_evolution(criterion, bounds=((-width, width), (-height, height), (0, 360)))
            my_dict[result.fun] = [*result.x]           # Сохранение результата в словарь

        # Лучшее решение - наименьшее значение функции критерия. Перемещение предмета на это решение
        offsets = my_dict[min(my_dict)]
        item = rotate(translate(item, xoff=offsets[0], yoff=offsets[1]), offsets[2])

        # Сравнение площади фигуры, принадлежащей предмету, но лежащей вне многоугольника и максимальной погрешности
        if item.difference(figure).area > ALLOWABLE_ERROR:
            save_false_plot(picture)
            return False

        plot_polygon(item, 'r')                     # Отрисовка предмета
        figure = figure.difference(item)            # Вырезать предмет из многоугольника
        my_dict.clear()                             # Очистить словаря для следующего предмета

    save_plot(picture)                              # Сохранение результата
    return True


# Первый алгоритм, созданный для второй итерации
def my_first_algorithm(picture):
    if picture.figure_polygon.area < sum([item.area for item in picture.items_polygons]):
        return False
    return True
