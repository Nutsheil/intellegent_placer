import cv2
import numpy as np
from matplotlib import pyplot as plt

# CONSTANTS
KERNEL_SIZE = (7, 7)
CANNY_THRESHOLD_LOW = 50
CANNY_THRESHOLD_HIGH = 200
APPROX_CURVE = 0.000001


def get_contours(image):
    gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, CANNY_THRESHOLD_LOW, CANNY_THRESHOLD_HIGH)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, KERNEL_SIZE)
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    masks_pts = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, APPROX_CURVE * peri, True)
            masks_pts.append(approx)

    return masks_pts


def get_mask_from_contour(contours) -> []:
    masks = []
    for cnt in contours:
        bbox = cv2.boundingRect(cnt)

        x_most_left, width, y_most_bottom, height = bbox[1], bbox[3], bbox[0], bbox[2]
        mask = np.full((width, height), False, dtype=bool)
        for y in range(y_most_bottom, y_most_bottom + height):
            for x in range(x_most_left, x_most_left + width):
                if cv2.pointPolygonTest(cnt, (y, x), False) >= 0:
                    mask[x - x_most_left][y - y_most_bottom] = True
        masks.append((mask * 255).astype("uint8"))

    return masks
