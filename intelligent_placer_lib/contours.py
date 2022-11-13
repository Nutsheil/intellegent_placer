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


def get_contours_v2(image):
    img_gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    img_gauss = cv2.GaussianBlur(img_gray, (3, 3), 0)
    img_canny = cv2.Canny(img_gauss, 70, 250)
    # plt.imshow(img_canny)
    # plt.show()

    contours, hierarchy = cv2.findContours(image=img_canny, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

    good_contours = []
    cx = []
    cy = []
    area_contours = []
    min_contour_area = 200

    # delete noise contours
    for i, cnt in enumerate(contours):
        contour_area = cv2.contourArea(cnt)
        if contour_area > min_contour_area and hierarchy[0][i][3] == -1:
            area_contours.append(contour_area)
            good_contours.append(cnt)
            M = cv2.moments(cnt)
            cx.append(int(M['m10'] / (M['m00'] + 1e-5)))
            cy.append(int(M['m01'] / (M['m00'] + 1e-5)))
    selected_contour = None
    x_max = 0
    idx = 0

    # delete contours with almost equal area
    for i, cnt in enumerate(area_contours):
        for j, cnt in enumerate(area_contours):
            if i != j and abs(area_contours[i] - area_contours[j]) <= 70:
                area_contours.pop(j)
                good_contours.pop(j)

    return good_contours

    # # detect polygon
    # for i, cnt in enumerate(good_contours):
    #     x_pos = max([np.ndarray.reshape(x, (2,))[0] for x in cnt])
    #     img_copy = image.copy()
    #     cv2.drawContours(img_copy, [cnt], 0, (255, 0, 0), 8)
    #     if x_pos > x_max:
    #         selected_contour = cnt
    #         x_max = x_pos
    #         idx = i
    #
    # good_contours.pop(idx)
    # area_contours.pop(idx)
    # img_copy = image.copy()
    # cv2.drawContours(img_copy, good_contours, -1, (255, 0, 0), 8)
    # polygon = ObjectBase(image, "polygon", get_mask_from_contour([selected_contour])[0])
    #
    # objects_set = []
    # for i, mask in enumerate(get_mask_from_contour(good_contours)):
    #     objects_set.append(ObjectBase(image, f"{i}", mask))
    #
    # return polygon, objects_set
