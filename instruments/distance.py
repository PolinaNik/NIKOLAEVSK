from instruments import converter
from math import sqrt


def distance(cord1, cord2):
    """ Находит расстояние между двумя точками, выводит значение в км"""

    (x1, y1) = converter.geo_to_flat(cord1[0], cord1[1])
    (x2, y2) = converter.geo_to_flat(cord2[0], cord2[1])
    dist = (sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) / 1000
    return dist
