import cv2
import numpy as np

KERNEL_SIZE = (7, 7)                            # Размер фильтра
CANNY_THRESHOLD_LOW = 50                        # Нижняя граница метода Кэнни
CANNY_THRESHOLD_HIGH = 200                      # Верхняя граница метода Кэнни
APPROX_CURVE = 0.000001                         # Убрать шумы с изображения
MIN_AREA = 1000                                 # Минимальная площадь контура (чтобы убрать "фантомные" контуры)


def get_contours(image: np.ndarray):
    gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, CANNY_THRESHOLD_LOW, CANNY_THRESHOLD_HIGH)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, KERNEL_SIZE)
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contours = filter(lambda x: cv2.contourArea(x) > MIN_AREA, contours)
    contours = tuple(
        cv2.approxPolyDP(contour, APPROX_CURVE * cv2.arcLength(contour, True), True)
        for contour in contours
    )

    return contours
