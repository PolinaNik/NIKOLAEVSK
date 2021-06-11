def change_angle(angle):
    """Избавляется от отрицательных углов и углов больше 360 градусов"""

    if angle < 0:
        return 360 + angle
    elif angle > 360:
        return angle - 360
    else:
        return angle
