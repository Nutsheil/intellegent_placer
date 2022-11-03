import cv2

# CONSTANTS
KERNEL_SIZE = (7, 7)
CANNY_THRESHOLD_LOW = 50
CANNY_THRESHOLD_HIGH = 200
APPROX_CURVE = 0.000001


def get_contours_v1(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, CANNY_THRESHOLD_LOW, CANNY_THRESHOLD_HIGH)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, KERNEL_SIZE)
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    masks_pts = []
    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, APPROX_CURVE * peri, True)
        masks_pts.append(approx)

    return masks_pts


def get_contours_v2(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
    img = cv2.Canny(img, CANNY_THRESHOLD_LOW, CANNY_THRESHOLD_HIGH)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
    img = cv2.dilate(img, kernel, iterations=3)
    img = cv2.erode(img, kernel, iterations=3)

    contours, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours
