

# Inspired by the algorithm of my colleague Dmitry Veselyj (GitHub: DmitryjVeselyj)
def my_first_algorithm(picture):
    if picture.polygon.area < sum([item.area for item in picture.items]):
        return False
    return True
