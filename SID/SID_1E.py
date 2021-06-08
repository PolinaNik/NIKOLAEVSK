import points
from instruments.simple_route import SimpleRoute
from instruments.paralel_route import ParalelRoute
from instruments import converter as convert
from instruments.draw_route import draw_route
import SID.kinks.kinks_sid1e as kinks
import os

start_point = convert.str_to_gr('530917'), convert.str_to_gr('1403816')
begin_arc = convert.str_to_gr('530845'), convert.str_to_gr('1404720')
gl_center_down = points.glob_center_sid1e_down
gl_rad_down = points.glob_radius_sid1e_down

gl_center_up = points.glob_center_sid1e_up
gl_rad_up = points.glob_radius_sid1e_up

file_name = 'uhnn_sid(1e)'

try:
    os.remove(f'{file_name}.sld')
except:
    pass

TEBSA = ParalelRoute(start_point=start_point, start_bearing=108,
              begin_arc=begin_arc, turn1='LEFT', glob_center=gl_center_up, glob_rad=gl_rad_up, kink=kinks.tebsa,
              kink_bearing=290, turn2='RIGHT', end_bearing=347, end_point=points.TEBSA)

TOTRU = SimpleRoute(start_point=start_point, start_bearing=108,
                    begin_arc=begin_arc, turn="LEFT", kink=kinks.totru, end_point=points.TOTRU)

DOKIR = SimpleRoute(start_point=start_point, start_bearing=108,
                    begin_arc=begin_arc, turn="LEFT", kink=kinks.dokir, end_point=points.DOKIR)

KIZON = SimpleRoute(start_point=start_point, start_bearing=108,
                    begin_arc=begin_arc, turn="LEFT", kink=kinks.kizon, end_point=points.KIZON)

NOKDA = SimpleRoute(start_point=start_point, start_bearing=108,
                    begin_arc=begin_arc, turn="LEFT", kink=kinks.nokda, end_point=points.NOKDA)

GIGOR = SimpleRoute(start_point=start_point, start_bearing=108,
                    begin_arc=begin_arc, turn="LEFT", kink=kinks.gigor, end_point=points.GIGOR)

OSBET = SimpleRoute(start_point=start_point, start_bearing=108,
                    begin_arc=begin_arc, turn="RIGHT", kink=kinks.osbet, end_point=points.OSBET)

LIRSA = SimpleRoute(start_point=start_point, start_bearing=108,
                    begin_arc=begin_arc, turn="RIGHT", kink=kinks.lirsa, end_point=points.LIRSA)

LEKBI = SimpleRoute(start_point=start_point, start_bearing=108,
                    begin_arc=begin_arc, turn="RIGHT", kink=kinks.lekbi, end_point=points.LEKBI)

RATNU = ParalelRoute(start_point=start_point, start_bearing=108,
              begin_arc=begin_arc, turn1='RIGHT', glob_center=gl_center_down, glob_rad=gl_rad_down, kink=kinks.ratnu,
              kink_bearing=290, turn2='RIGHT', end_bearing=347, end_point=points.RATNU)

PIKUS = ParalelRoute(start_point=start_point, start_bearing=108,
              begin_arc=begin_arc, turn1='RIGHT', glob_center=gl_center_down, glob_rad=gl_rad_down, kink=kinks.pikus,
              kink_bearing=290, turn2='RIGHT', end_bearing=347, end_point=points.PIKUS)


draw_route(file_name, 'TEBSA1E', convert.to_gr(start_point), convert.to_gr(begin_arc), TEBSA.first_turn(), convert.to_gr(points.TEBSA))

draw_route(file_name, 'TOTRU1E', convert.to_gr(start_point), convert.to_gr(begin_arc), TOTRU.first_turn(), convert.to_gr(points.TOTRU))

draw_route(file_name, 'DOKIR1E', convert.to_gr(start_point), convert.to_gr(begin_arc), DOKIR.first_turn(), convert.to_gr(points.DOKIR))

draw_route(file_name, 'KIZON1E', convert.to_gr(start_point), convert.to_gr(begin_arc), KIZON.first_turn(), convert.to_gr(points.KIZON))

draw_route(file_name, 'NOKDA1E', convert.to_gr(start_point), convert.to_gr(begin_arc), NOKDA.first_turn(), convert.to_gr(points.NOKDA))

draw_route(file_name, 'GIGOR1E', convert.to_gr(start_point), convert.to_gr(begin_arc), GIGOR.first_turn(), convert.to_gr(points.GIGOR))

draw_route(file_name, 'OSBET1E', convert.to_gr(start_point), convert.to_gr(begin_arc), OSBET.first_turn(), convert.to_gr(points.OSBET))

draw_route(file_name, 'LIRSA1E', convert.to_gr(start_point), convert.to_gr(begin_arc), LIRSA.first_turn(), convert.to_gr(points.LIRSA))

draw_route(file_name, 'LEKBI1E', convert.to_gr(start_point), convert.to_gr(begin_arc), LEKBI.first_turn(), convert.to_gr(points.LEKBI))

draw_route(file_name, 'RATNU1E', convert.to_gr(start_point), convert.to_gr(begin_arc), RATNU.first_turn(), convert.to_gr(points.RATNU))

draw_route(file_name, 'PIKUS1E', convert.to_gr(start_point), convert.to_gr(begin_arc), PIKUS.first_turn(), convert.to_gr(points.PIKUS))


