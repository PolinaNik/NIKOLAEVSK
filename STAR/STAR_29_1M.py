import points
import rnav_points
import cords
import os
from instruments import converter as convert
from instruments.draw_route import draw_route
from instruments.draw_point import draw_point
from instruments.add_trenajor import create_trenajor_file

file_name = 'uhnn_star_29_1M'

try:
    os.remove(f'ROUTES/{file_name}.sld')
except:
    pass


try:
    os.remove(f'KST_ROUTES/{file_name}.txt')
except:
    pass

if not os.path.exists('ROUTES'):
    os.makedirs('ROUTES')

if not os.path.exists('KST_ROUTES'):
    os.makedirs('KST_ROUTES')

trenajor = {}

draw_route(file_name, 'TEBSA1M', convert.to_gr(points.TEBSA), convert.to_gr(rnav_points.NN011),
           convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

TEBSA_1M = {
    'TEBSA1M': [
        {'TEBSA': convert.str_to_tren2(cords.TEBSA)},
        {'NN011': convert.str_to_tren2(cords.NN011)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(TEBSA_1M)

draw_route(file_name, 'TOTRU1M', convert.to_gr(points.TOTRU), convert.to_gr(rnav_points.NN011),
           convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

TOTRU_1M = {
    'TOTRU1M': [
        {'TOTRU': convert.str_to_tren2(cords.TOTRU)},
        {'NN011': convert.str_to_tren2(cords.NN011)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(TOTRU_1M)

draw_route(file_name, 'DOKIR1M', convert.to_gr(points.DOKIR), convert.to_gr(rnav_points.NN011),
           convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

DOKIR_1M = {
    'DOKIR1M': [
        {'DOKIR': convert.str_to_tren2(cords.DOKIR)},
        {'NN011': convert.str_to_tren2(cords.NN011)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(DOKIR_1M)


draw_route(file_name, 'KIZON1M', convert.to_gr(points.KIZON), convert.to_gr(rnav_points.NN017),
           convert.to_gr(rnav_points.NN011), convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009),
           convert.to_gr(points.RW29))

KIZON_1M = {
    'KIZON1M': [
        {'KIZON': convert.str_to_tren2(cords.KIZON)},
        {'NN017': convert.str_to_tren2(cords.NN017)},
        {'NN011': convert.str_to_tren2(cords.NN011)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(KIZON_1M)


draw_route(file_name, 'NOKDA1M', convert.to_gr(points.NOKDA), convert.to_gr(rnav_points.NN017),
           convert.to_gr(rnav_points.NN011),convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009),
           convert.to_gr(points.RW29))

NOKDA_1M = {
    'NOKDA1M': [
        {'NOKDA': convert.str_to_tren2(cords.NOKDA)},
        {'NN017': convert.str_to_tren2(cords.NN017)},
        {'NN011': convert.str_to_tren2(cords.NN011)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(NOKDA_1M)

draw_route(file_name, 'GIGOR1M', convert.to_gr(points.GIGOR), convert.to_gr(rnav_points.NN012),
           convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

GIGOR_1M = {
    'GIGOR1M': [
        {'GIGOR': convert.str_to_tren2(cords.GIGOR)},
        {'NN017': convert.str_to_tren2(cords.NN012)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(GIGOR_1M)

draw_route(file_name, 'OSBET1M', convert.to_gr(points.OSBET), convert.to_gr(rnav_points.NN013),
           convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

OSBET_1M = {
    'OSBET1M': [
        {'OSBET': convert.str_to_tren2(cords.OSBET)},
        {'NN013': convert.str_to_tren2(cords.NN013)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(OSBET_1M)

draw_route(file_name, 'LIRSA1M', convert.to_gr(points.LIRSA), convert.to_gr(rnav_points.NN013),
           convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

LIRSA_1M = {
    'LIRSA1M': [
        {'LIRSA': convert.str_to_tren2(cords.LIRSA)},
        {'NN013': convert.str_to_tren2(cords.NN013)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(LIRSA_1M)

draw_route(file_name, 'LEKBI1M', convert.to_gr(points.LEKBI), convert.to_gr(rnav_points.NN013),
           convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

LEKBI_1M = {
    'LEKBI1M': [
        {'LEKBI': convert.str_to_tren2(cords.LEKBI)},
        {'NN013': convert.str_to_tren2(cords.NN013)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(LEKBI_1M)

draw_route(file_name, 'RATNU1M', convert.to_gr(points.RATNU), convert.to_gr(rnav_points.NN018),
           convert.to_gr(rnav_points.NN019), convert.to_gr(rnav_points.NN013),convert.to_gr(rnav_points.NN008),
           convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

RATNU_1M = {
    'RATNU1M': [
        {'RATNU': convert.str_to_tren2(cords.RATNU)},
        {'NN018': convert.str_to_tren2(cords.NN018)},
        {'NN019': convert.str_to_tren2(cords.NN019)},
        {'NN013': convert.str_to_tren2(cords.NN013)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(RATNU_1M)

draw_route(file_name, 'PIKUS1M', convert.to_gr(points.PIKUS), convert.to_gr(rnav_points.NN018),
           convert.to_gr(rnav_points.NN019), convert.to_gr(rnav_points.NN013),convert.to_gr(rnav_points.NN008),
           convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

PIKUS_1M = {
    'PIKUS1M': [
        {'PIKUS': convert.str_to_tren2(cords.PIKUS)},
        {'NN018': convert.str_to_tren2(cords.NN018)},
        {'NN019': convert.str_to_tren2(cords.NN019)},
        {'NN013': convert.str_to_tren2(cords.NN013)},
        {'NN008': convert.str_to_tren2(cords.NN008)},
        {'NN009': convert.str_to_tren2(cords.NN009)},
        {'RW29': convert.str_to_tren2(cords.RW29)}
]
}

trenajor.update(PIKUS_1M)

draw_point(file_name, rnav_points.NN011, rnav_points.NN012, rnav_points.NN013, rnav_points.NN017, rnav_points.NN018, rnav_points.NN019, rnav_points.NN008, rnav_points.NN009, rnav_points.NN010, rnav_points.NN014)
create_trenajor_file(file_name, trenajor)