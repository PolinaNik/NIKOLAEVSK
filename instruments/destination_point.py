from math import radians, degrees, sin, cos, atan2, asin


def destination_point(start_point, bearing, distance):
    """ Находит координаты точки на заданном удалении
     с заднным азимутом от стартовой точки"""

    f1 = radians(start_point[0])
    l1 = radians(start_point[1])
    rad = 6371
    b = distance / rad
    f2 = asin(sin(f1) * cos(b) + cos(f1) * sin(b) * cos(radians(bearing)))
    l2 = l1 + atan2(sin(radians(bearing)) * sin(b) * cos(f1), cos(b) - sin(f1) * sin(f2))
    return degrees(f2), degrees(l2)
