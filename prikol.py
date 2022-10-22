import cv2

KERNEL_SIZE = (7, 7)
MIN_AREA = 1000
CANNY_THRESHOLD_LOW = 50
CANNY_THRESHOLD_HIGH = 200
APPROX_CURVE = 0.000001


def get_joke(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, CANNY_THRESHOLD_LOW, CANNY_THRESHOLD_HIGH)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, KERNEL_SIZE)
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    masks_pts = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > MIN_AREA:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, APPROX_CURVE * peri, True)
            masks_pts.append(approx)
    return image, masks_pts
