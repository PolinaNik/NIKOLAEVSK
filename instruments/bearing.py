from math import radians, degrees, cos, sin, atan2
from instruments.change_angle import change_angle


def bearing(cord1, cord2):
    """ Функция для нахождения азимута. На вход принимаются десятичные градусы,
    на выходе определяется угол в градусах"""

    f1 = radians(cord1[0])
    l1 = radians(cord1[1])
    f2 = radians(cord2[0])
    l2 = radians(cord2[1])
    dl = l2 - l1
    bearing = atan2(sin(dl) * cos(f2), cos(f1) * sin(f2) - sin(f1) * cos(f2) * cos(dl))
    return change_angle(degrees(bearing))
