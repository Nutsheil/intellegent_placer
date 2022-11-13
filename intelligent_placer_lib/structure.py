from cv2 import contourArea


class Primitive:
    def __init__(self, image, name, contour):
        self.image = image
        self.name = name
        self.contour = contour
        self.area = contourArea(contour[0])


# Entity "subject, object"
class Item:
    def __init__(self, contour):
        self.contour = contour
        self.area = contourArea(contour[0])


# Entity "polygon, figure"
class Polygon:
    def __init__(self, contour):
        self.contour = contour
        self.area = contourArea(contour[0])


# The entity of the whole image
class Picture:
    def __init__(self, image, name, contours=None):
        self.image = image
        self.name = name
        self.contours = contours            # will be removed in next version (for debug now)
        self.items = []
        self.polygon = None
        self.image_with_contours = None
        self.image_contours_only = None
        self.image_bbox = None

    def sort_items(self):
        self.items.sort(key=lambda x: x.area, reverse=True)
