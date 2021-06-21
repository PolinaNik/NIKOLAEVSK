import points
from instruments.simple_route import SimpleRoute
from instruments.paralel_route import ParalelRoute
from instruments import converter as convert
from instruments.draw_route import draw_route, draw_route_tr
import SID.kinks.kinks_sid1f as kinks
import os

start_point = convert.str_to_gr('530917'), convert.str_to_gr('1403945')
begin_arc = convert.str_to_gr('530930'), convert.str_to_gr('1403115')
gl_center_down = points.glob_center_sid1f_down
gl_rad_down = points.glob_radius_sid1f_down
gl_center_up = points.glob_center_sid1f_up
gl_rad_up = points.glob_radius_sid1f_up

file_name = 'uhnn_sid(1f)'

try:
    os.remove(f'{file_name}.sld')
except:
    pass

file_name_tr = 'uhnn_sid(1f)_tr'

try:
    os.remove(f'{file_name_tr}.txt')
except:
    pass

TOTRU = SimpleRoute(start_point=start_point, start_bearing=288,
                    begin_arc=begin_arc, turn="RIGHT", kink=kinks.totru, end_point=points.TOTRU)

DOKIR = SimpleRoute(start_point=start_point, start_bearing=288,
                    begin_arc=begin_arc, turn="RIGHT", kink=kinks.dokir, end_point=points.DOKIR)

KIZON = SimpleRoute(start_point=start_point, start_bearing=288,
                    begin_arc=begin_arc, turn="RIGHT", kink=kinks.kizon, end_point=points.KIZON)

NOKDA = SimpleRoute(start_point=start_point, start_bearing=288,
                    begin_arc=begin_arc, turn="RIGHT", kink=kinks.nokda, end_point=points.NOKDA)

GIGOR = ParalelRoute(start_point=start_point, start_bearing=288,
                     begin_arc=begin_arc, turn1='RIGHT', glob_center=gl_center_up, glob_rad=gl_rad_up, kink=kinks.ratnu,
                     kink_bearing=290, turn2='RIGHT', end_bearing=347, end_point=points.GIGOR)

OSBET = ParalelRoute(start_point=start_point, start_bearing=288,
                     begin_arc=begin_arc, turn1='LEFT', glob_center=gl_center_down, glob_rad=gl_rad_down,
                     kink=kinks.ratnu,
                     kink_bearing=290, turn2='RIGHT', end_bearing=347, end_point=points.OSBET)

LIRSA = SimpleRoute(start_point=start_point, start_bearing=288,
                    begin_arc=begin_arc, turn="LEFT", kink=kinks.lirsa, end_point=points.LIRSA)

LEKBI = SimpleRoute(start_point=start_point, start_bearing=288,
                    begin_arc=begin_arc, turn="LEFT", kink=kinks.lekbi, end_point=points.LEKBI)

draw_route(file_name, 'TEBSA1F', convert.to_gr(start_point), convert.to_gr(begin_arc), convert.to_gr(points.TEBSA))

draw_route(file_name, 'TOTRU1F', convert.to_gr(start_point), convert.to_gr(begin_arc), TOTRU.first_turn(),
           convert.to_gr(points.TOTRU))

draw_route(file_name, 'DOKIR1F', convert.to_gr(start_point), convert.to_gr(begin_arc), DOKIR.first_turn(),
           convert.to_gr(points.DOKIR))

draw_route(file_name, 'KIZON1F', convert.to_gr(start_point), convert.to_gr(begin_arc), KIZON.first_turn(),
           convert.to_gr(points.KIZON))

draw_route(file_name, 'NOKDA1F', convert.to_gr(start_point), convert.to_gr(begin_arc), NOKDA.first_turn(),
           convert.to_gr(points.NOKDA))

draw_route(file_name, 'GIGOR1F', convert.to_gr(start_point), convert.to_gr(begin_arc), GIGOR.first_turn(),
           convert.to_gr(points.GIGOR))

draw_route(file_name, 'OSBET1F', convert.to_gr(start_point), convert.to_gr(begin_arc), OSBET.first_turn()[:-2],
           convert.to_gr(points.OSBET))

draw_route(file_name, 'LIRSA1F', convert.to_gr(start_point), convert.to_gr(begin_arc), LIRSA.first_turn(),
           convert.to_gr(points.LIRSA))

draw_route(file_name, 'LEKBI1F', convert.to_gr(start_point), convert.to_gr(begin_arc), LEKBI.first_turn(),
           convert.to_gr(points.LEKBI))

draw_route(file_name, 'RATNU1F', convert.to_gr(start_point), convert.to_gr(begin_arc), convert.to_gr(points.RATNU))

draw_route(file_name, 'PIKUS1F', convert.to_gr(start_point), convert.to_gr(begin_arc), convert.to_gr(points.PIKUS))

###################################################################################################################

draw_route_tr(file_name_tr, 'TEBSA1F', convert.to_gr(start_point), convert.to_gr(begin_arc), convert.to_gr(points.TEBSA))

draw_route_tr(file_name_tr, 'TOTRU1F', convert.to_gr(start_point), convert.to_gr(begin_arc), TOTRU.first_turn(),
           convert.to_gr(points.TOTRU))

draw_route_tr(file_name_tr, 'DOKIR1F', convert.to_gr(start_point), convert.to_gr(begin_arc), DOKIR.first_turn(),
           convert.to_gr(points.DOKIR))

draw_route_tr(file_name_tr, 'KIZON1F', convert.to_gr(start_point), convert.to_gr(begin_arc), KIZON.first_turn(),
           convert.to_gr(points.KIZON))

draw_route_tr(file_name_tr, 'NOKDA1F', convert.to_gr(start_point), convert.to_gr(begin_arc), NOKDA.first_turn(),
           convert.to_gr(points.NOKDA))

draw_route_tr(file_name_tr, 'GIGOR1F', convert.to_gr(start_point), convert.to_gr(begin_arc), GIGOR.first_turn(),
           convert.to_gr(points.GIGOR))

draw_route_tr(file_name_tr, 'OSBET1F', convert.to_gr(start_point), convert.to_gr(begin_arc), OSBET.first_turn()[:-2],
           convert.to_gr(points.OSBET))

draw_route_tr(file_name_tr, 'LIRSA1F', convert.to_gr(start_point), convert.to_gr(begin_arc), LIRSA.first_turn(),
           convert.to_gr(points.LIRSA))

draw_route_tr(file_name_tr, 'LEKBI1F', convert.to_gr(start_point), convert.to_gr(begin_arc), LEKBI.first_turn(),
           convert.to_gr(points.LEKBI))

draw_route_tr(file_name_tr, 'RATNU1F', convert.to_gr(start_point), convert.to_gr(begin_arc), convert.to_gr(points.RATNU))

draw_route_tr(file_name_tr, 'PIKUS1F', convert.to_gr(start_point), convert.to_gr(begin_arc), convert.to_gr(points.PIKUS))