from math import cos, sin, acos, asin, sqrt, pi, atan2, radians, degrees


def intersection_point(cord1, cord2, bearing1, bearing2):
    """ Находит пересечение прямых, при известных стартовых координатах
    и азимутов. Азимуты должны указываться с учетом магнитного склонения.
    Входные координаты - десятичные градусы."""

    f1 = radians(cord1[0])
    l1 = radians(cord1[1])
    f2 = radians(cord2[0])
    l2 = radians(cord2[1])
    df = f2 - f1
    dl = l2 - l1
    b_12 = 2 * asin(sqrt((sin(df/2)) ** 2 + cos(f1) * cos(f2) * (sin(dl / 2)) ** 2))
    Q_a = acos((sin(f2) - sin(f1) * cos(b_12))/ (sin(b_12) * cos(f1)))
    Q_b = acos((sin(f1) - sin(f2) * cos(b_12)) / (sin(b_12) * cos(f2)))
    if sin(dl) > 0:
        Q_12 = Q_a
        Q_21 = 2 * pi - Q_b
    else:
        Q_12 = 2 * pi - Q_a
        Q_21 = Q_b
    Q_13 = radians(bearing1)
    Q_23 = radians(bearing2)
    a1 = Q_13 - Q_12
    a2 = Q_21 - Q_23
    a3 = acos(-1 * cos(a1) * cos(a2) + sin(a1) * sin(a2) * cos(b_12))
    b_13 = atan2(sin(b_12) * sin(a1) * sin(a2), cos(a2) + cos(a1) * cos(a3))
    f3 = asin(sin(f1) * cos(b_13) + cos(f1) * sin(b_13) * cos(Q_13))
    dl_13 = atan2(sin(Q_13) * sin(b_13) * cos(f1), cos(b_13) - sin(f1) * sin(f3))
    l3 = l1 + dl_13
    return degrees(f3), degrees(l3)