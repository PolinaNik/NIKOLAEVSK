import points
import rnav_points
import os
from instruments import converter as convert
from instruments.draw_route import draw_route
from instruments.draw_point import draw_point
from instruments.add_trenajor import create_trenajor_file

file_name = 'uhnn_star(1l)'

try:
    os.remove(f'{file_name}.sld')
except:
    pass

trenajor = {}

draw_route(file_name, 'TEBSA1L', convert.to_gr(points.TEBSA), convert.to_gr(rnav_points.NN002),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

TEBSA_1L = {
    'TEBSA1L': [
        {'TEBSA': convert.to_gr_tren(points.TEBSA)},
        {'NN002': convert.to_gr_tren(rnav_points.NN002)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(TEBSA_1L)

draw_route(file_name, 'TOTRU1L', convert.to_gr(points.TOTRU), convert.to_gr(rnav_points.NN003),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

TOTRU_1L = {
    'TOTRU1L': [
        {'TOTRU': convert.to_gr_tren(points.TOTRU)},
        {'NN003': convert.to_gr_tren(rnav_points.NN003)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(TOTRU_1L)

draw_route(file_name, 'DOKIR1L', convert.to_gr(points.DOKIR), convert.to_gr(rnav_points.NN003),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

DOKIR_1L = {
    'DOKIR1L': [
        {'DOKIR': convert.to_gr_tren(points.DOKIR)},
        {'NN003': convert.to_gr_tren(rnav_points.NN003)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(DOKIR_1L)

draw_route(file_name, 'KIZON1L', convert.to_gr(points.KIZON), convert.to_gr(rnav_points.NN015),
           convert.to_gr(rnav_points.NN003), convert.to_gr(rnav_points.NN004),
           convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

KIZON_1L = {
    'KIZON1L': [
        {'KIZON': convert.to_gr_tren(points.KIZON)},
        {'NN015': convert.to_gr_tren(rnav_points.NN015)},
        {'NN003': convert.to_gr_tren(rnav_points.NN003)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(KIZON_1L)

draw_route(file_name, 'NOKDA1L', convert.to_gr(points.NOKDA), convert.to_gr(rnav_points.NN015),
           convert.to_gr(rnav_points.NN003), convert.to_gr(rnav_points.NN004),
           convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

NOKDA_1L = {
    'NOKDA1L': [
        {'NOKDA': convert.to_gr_tren(points.NOKDA)},
        {'NN015': convert.to_gr_tren(rnav_points.NN015)},
        {'NN003': convert.to_gr_tren(rnav_points.NN003)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(NOKDA_1L)

draw_route(file_name, 'GIGOR1L', convert.to_gr(points.GIGOR), convert.to_gr(rnav_points.NN003),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

GIGOR_1L = {
    'GIGOR1L': [
        {'GIGOR': convert.to_gr_tren(points.GIGOR)},
        {'NN003': convert.to_gr_tren(rnav_points.NN003)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(GIGOR_1L)

draw_route(file_name, 'OSBET1L', convert.to_gr(points.OSBET), convert.to_gr(rnav_points.NN016),
           convert.to_gr(rnav_points.NN001), convert.to_gr(rnav_points.NN004),
           convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

OSBET_1L = {
    'OSBET1L': [
        {'OSBET': convert.to_gr_tren(points.OSBET)},
        {'NN016': convert.to_gr_tren(rnav_points.NN016)},
        {'NN001': convert.to_gr_tren(rnav_points.NN001)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(OSBET_1L)

draw_route(file_name, 'LIRSA1L', convert.to_gr(points.LIRSA), convert.to_gr(rnav_points.NN016),
           convert.to_gr(rnav_points.NN001),convert.to_gr(rnav_points.NN004),
           convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

LIRSA_1L = {
    'LIRSA1L': [
        {'LIRSA': convert.to_gr_tren(points.LIRSA)},
        {'NN016': convert.to_gr_tren(rnav_points.NN016)},
        {'NN001': convert.to_gr_tren(rnav_points.NN001)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(LIRSA_1L)

draw_route(file_name, 'LEKBI1L', convert.to_gr(points.LEKBI), convert.to_gr(rnav_points.NN001),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

LEKBI_1L = {
    'LEKBI1L': [
        {'LEKBI': convert.to_gr_tren(points.LEKBI)},
        {'NN001': convert.to_gr_tren(rnav_points.NN001)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(LEKBI_1L)

draw_route(file_name, 'RATNU1L', convert.to_gr(points.RATNU), convert.to_gr(rnav_points.NN002),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

RATNU_1L = {
    'RATNU1L': [
        {'RATNU': convert.to_gr_tren(points.RATNU)},
        {'NN002': convert.to_gr_tren(rnav_points.NN002)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(RATNU_1L)

draw_route(file_name, 'PIKUS1L', convert.to_gr(points.PIKUS), convert.to_gr(rnav_points.NN002),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

PIKUS_1L = {
    'PIKUS1L': [
        {'PIKUS': convert.to_gr_tren(points.PIKUS)},
        {'NN001': convert.to_gr_tren(rnav_points.NN002)},
        {'NN004': convert.to_gr_tren(rnav_points.NN004)},
        {'NN005': convert.to_gr_tren(rnav_points.NN005)},
        {'RW11': convert.to_gr_tren(points.RW11)}
]
}

trenajor.update(PIKUS_1L)

draw_point(file_name, rnav_points.NN001, rnav_points.NN002, rnav_points.NN003, rnav_points.NN015, rnav_points.NN016, rnav_points.NN006, rnav_points.NN007)

create_trenajor_file(file_name, trenajor)
