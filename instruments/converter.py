from pyproj.transformer import TransformerGroup
import math


def str_to_gr(cord):
    """ Принимает строковое значение для широты или долготы
    coord = '532010' и возвращает результат в формате int
    result = 53.336111111111116 """

    if len(cord) == 6:
        N_gr = int(cord[0:2])
        N_min = int(cord[2:4]) / 60
        N_sec = int(cord[4:]) / 3600
        result = N_gr + N_min + N_sec
        return result
    else:
        E_gr = int(cord[0:3])
        E_min = int(cord[3:5]) / 60
        E_sec = int(cord[5:]) / 3600
        result = E_gr + E_min + E_sec
        return result


def slds_to_gr(cord):
    lat = cord[1:7]
    lon = cord[10:17]
    return str_to_gr(lat), str_to_gr(lon)


def geo_to_flat(lat, lon):
    """ Переводит геодезические координаты в плоские x,y.
    Возвращает кортеж (5912115.946632388, 24481558.644002877)"""

    trans_group = TransformerGroup("epsg:4326", "epsg:28424")
    return trans_group.transformers[0].transform(lat, lon)


def flat_to_geo(x, y):
    """ Переводит плоские координаты в геодезические lat, lon
    Возвращает кортеж (53.336111111111116, 140.72472222222223)"""

    trans_group = TransformerGroup("epsg:28424", "epsg:4326")
    return trans_group.transformers[0].transform(x, y)


# Перевод десятичных градусов в градусы, минуты и секунды
def to_gr(line):
    f = float(line[0])
    l = float(line[1])
    f_gr = math.trunc(f)
    l_gr = math.trunc(l)
    f_min = math.trunc((f - f_gr) * 60)
    l_min = math.trunc((l - l_gr) * 60)
    f_sec = math.trunc(((f - f_gr) * 60 - f_min) * 60)
    l_sec = math.trunc(((l - l_gr) * 60 - l_min) * 60)
    f_mili = math.ceil((((f - f_gr) * 60 - f_min) * 60 - f_sec) * 60)
    l_mili = math.ceil((((l - l_gr) * 60 - l_min) * 60 - l_sec) * 60)
    f_gr = str(f_gr).rjust(2, '0')
    l_gr = str(l_gr).rjust(3, '0')
    f_min = str(f_min).rjust(2, '0')
    l_min = str(l_min).rjust(2, '0')
    f_sec = str(f_sec).rjust(2, '0')
    l_sec = str(l_sec).rjust(2, '0')
    f_mili = str(f_mili).rjust(2, '0')
    l_mili = str(l_mili).rjust(2, '0')
    f = 'N' + f_gr + f_min + f_sec + f_mili
    l = 'E' + l_gr + l_min + l_sec + l_mili
    coord = f + l
    return coord
