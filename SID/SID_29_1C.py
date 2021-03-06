import points
from instruments.route import Route
from instruments.heart_route import HeartRoute
from instruments import converter as convert
from instruments.draw_route import draw_route, draw_route_tr
import SID.kinks.kinks_sid1c as kinks
import os

start_point = convert.str_to_gr('530900'), convert.str_to_gr('1403945')
begin_arc = convert.str_to_gr('530925'), convert.str_to_gr('1403110')

gl_center_down = points.glob_center_sid1c_down
gl_rad_down = points.glob_radius_sid1c_down

gl_center_up = points.glob_center_sid1c_up
gl_rad_up = points.glob_radius_sid1c_up

file_name = 'uhnn_sid_29_1C'

try:
    os.remove(f'{file_name}.sld')
except:
    pass


try:
    os.remove(f'{file_name}.txt')
except:
    pass

if not os.path.exists('ROUTES'):
    os.makedirs('ROUTES')

if not os.path.exists('KST_ROUTES'):
    os.makedirs('KST_ROUTES')

TEBSA = Route(start_point=start_point, start_bearing=288,
              begin_arc=begin_arc, turn1='RIGHT', kink=kinks.tebsa,
              kink_bearing=339, turn2='LEFT', end_bearing=310, end_point=points.TEBSA)

TOTRU = Route(start_point=start_point, start_bearing=288,
              begin_arc=begin_arc, turn1='RIGHT', kink=kinks.totru,
              kink_bearing=70, turn2='LEFT', end_bearing=347, end_point=points.TOTRU)

DOKIR = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="LEFT", kink=points.LOM,
                   turn2="LEFT", round_kink=kinks.lekbi, round_bearing=155,
                   glob_center=gl_center_up, glob_rad=gl_rad_up, last_turn="LEFT",
                   az_turn=340, end_bearing=21, end_point=points.DOKIR)

KIZON = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="LEFT", kink=points.LOM,
                   turn2="LEFT", round_kink=kinks.lekbi, round_bearing=155,
                   glob_center=gl_center_up, glob_rad=gl_rad_up, last_turn="LEFT",
                   az_turn=340, end_bearing=43, end_point=points.KIZON)

NOKDA = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="LEFT", kink=points.LOM,
                   turn2="LEFT", round_kink=kinks.lekbi, round_bearing=155,
                   glob_center=gl_center_up, glob_rad=gl_rad_up, last_turn="LEFT",
                   az_turn=340, end_bearing=53, end_point=points.NOKDA)

GIGOR = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="LEFT", kink=points.LOM,
                   turn2="LEFT", round_kink=kinks.lekbi, round_bearing=155,
                   glob_center=gl_center_up, glob_rad=gl_rad_up, last_turn="LEFT",
                   az_turn=340, end_bearing=86, end_point=points.GIGOR)

OSBET = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="RIGHT", kink=points.LOM,
                   turn2="RIGHT", round_kink=kinks.totru, round_bearing=70,
                   glob_center=gl_center_down, glob_rad=gl_rad_down, last_turn="RIGHT",
                   az_turn=250, end_bearing=165, end_point=points.OSBET)

LIRSA = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="RIGHT", kink=points.LOM,
                   turn2="RIGHT", round_kink=kinks.totru, round_bearing=70,
                   glob_center=gl_center_down, glob_rad=gl_rad_down, last_turn="RIGHT",
                   az_turn=250, end_bearing=207, end_point=points.LIRSA)

LEKBI = Route(start_point=start_point, start_bearing=288,
              begin_arc=begin_arc, turn1='LEFT', kink=kinks.lekbi,
              kink_bearing=155, turn2='RIGHT', end_bearing=232, end_point=points.LEKBI)

RATNU = Route(start_point=start_point, start_bearing=288,
              begin_arc=begin_arc, turn1='LEFT', kink=kinks.ratnu,
              kink_bearing=248, turn2='RIGHT', end_bearing=276, end_point=points.RATNU)

PIKUS = Route(start_point=start_point, start_bearing=288,
              begin_arc=begin_arc, turn1='LEFT', kink=kinks.ratnu,
              kink_bearing=248, turn2='RIGHT', end_bearing=286, end_point=points.PIKUS)

draw_route(file_name, 'TEBSA1C', convert.to_gr(start_point), convert.to_gr(begin_arc), TEBSA.first_turn(),
           convert.to_gr(kinks.tebsa),
           TEBSA.second_turn(), convert.to_gr(points.TEBSA))

draw_route(file_name, 'TOTRU1C', convert.to_gr(start_point), convert.to_gr(begin_arc), TOTRU.first_turn(),
           convert.to_gr(kinks.totru),
           TOTRU.second_turn(), convert.to_gr(points.TOTRU))

draw_route(file_name, 'DOKIR1C', convert.to_gr(start_point), convert.to_gr(begin_arc), DOKIR.first_round(),
           convert.to_gr(points.LOM),
           DOKIR.glob_round(), DOKIR.second_turn(), convert.to_gr(points.DOKIR))

draw_route(file_name, 'KIZON1C', convert.to_gr(start_point), convert.to_gr(begin_arc), KIZON.first_round(),
           convert.to_gr(points.LOM),
           convert.to_gr(points.KIZON))

draw_route(file_name, 'NOKDA1C', convert.to_gr(start_point), convert.to_gr(begin_arc), NOKDA.first_round(),
           convert.to_gr(points.LOM),
           convert.to_gr(points.NOKDA))

draw_route(file_name, 'GIGOR1C', convert.to_gr(start_point), convert.to_gr(begin_arc), GIGOR.first_round(),
           convert.to_gr(points.LOM),
           convert.to_gr(points.GIGOR))

draw_route(file_name, 'OSBET1C', convert.to_gr(start_point), convert.to_gr(begin_arc), OSBET.first_round(),
           convert.to_gr(points.LOM),
           convert.to_gr(points.OSBET))

draw_route(file_name, 'LIRSA1C', convert.to_gr(start_point), convert.to_gr(begin_arc), LIRSA.first_round(),
           convert.to_gr(points.LOM),
           LIRSA.glob_round(), LIRSA.second_turn(), convert.to_gr(points.LIRSA))

draw_route(file_name, 'LEKBI1C', convert.to_gr(start_point), convert.to_gr(begin_arc), LEKBI.first_turn(),
           convert.to_gr(kinks.lekbi),
           LEKBI.second_turn(), convert.to_gr(points.LEKBI))

draw_route(file_name, 'RATNU1C', convert.to_gr(start_point), convert.to_gr(begin_arc), RATNU.first_turn(),
           convert.to_gr(kinks.ratnu),
           RATNU.second_turn(), convert.to_gr(points.RATNU))

draw_route(file_name, 'PIKUS1C', convert.to_gr(start_point), convert.to_gr(begin_arc), PIKUS.first_turn(),
           convert.to_gr(kinks.pikus),
           PIKUS.second_turn(), convert.to_gr(points.PIKUS))

#########################################################################################################

draw_route_tr(file_name, 'TEBSA1C', convert.to_gr(start_point), convert.to_gr(begin_arc), TEBSA.first_turn(),
           convert.to_gr(kinks.tebsa),
           TEBSA.second_turn(), convert.to_gr(points.TEBSA))

draw_route_tr(file_name, 'TOTRU1C', convert.to_gr(start_point), convert.to_gr(begin_arc), TOTRU.first_turn(),
           convert.to_gr(kinks.totru),
           TOTRU.second_turn(), convert.to_gr(points.TOTRU))

draw_route_tr(file_name, 'DOKIR1C', convert.to_gr(start_point), convert.to_gr(begin_arc), DOKIR.first_round(),
           convert.to_gr(points.LOM),
           DOKIR.glob_round(), DOKIR.second_turn(), convert.to_gr(points.DOKIR))

draw_route_tr(file_name, 'KIZON1C', convert.to_gr(start_point), convert.to_gr(begin_arc), KIZON.first_round(),
           convert.to_gr(points.LOM),
           convert.to_gr(points.KIZON))

draw_route_tr(file_name, 'NOKDA1C', convert.to_gr(start_point), convert.to_gr(begin_arc), NOKDA.first_round(),
           convert.to_gr(points.LOM),
           convert.to_gr(points.NOKDA))

draw_route_tr(file_name, 'GIGOR1C', convert.to_gr(start_point), convert.to_gr(begin_arc), GIGOR.first_round(),
           convert.to_gr(points.LOM),
           convert.to_gr(points.GIGOR))

draw_route_tr(file_name, 'OSBET1C', convert.to_gr(start_point), convert.to_gr(begin_arc), OSBET.first_round(),
           convert.to_gr(points.LOM),
           convert.to_gr(points.OSBET))

draw_route_tr(file_name, 'LIRSA1C', convert.to_gr(start_point), convert.to_gr(begin_arc), LIRSA.first_round(),
           convert.to_gr(points.LOM),
           LIRSA.glob_round(), LIRSA.second_turn(), convert.to_gr(points.LIRSA))

draw_route_tr(file_name, 'LEKBI1C', convert.to_gr(start_point), convert.to_gr(begin_arc), LEKBI.first_turn(),
           convert.to_gr(kinks.lekbi),
           LEKBI.second_turn(), convert.to_gr(points.LEKBI))

draw_route_tr(file_name, 'RATNU1C', convert.to_gr(start_point), convert.to_gr(begin_arc), RATNU.first_turn(),
           convert.to_gr(kinks.ratnu),
           RATNU.second_turn(), convert.to_gr(points.RATNU))

draw_route_tr(file_name, 'PIKUS1C', convert.to_gr(start_point), convert.to_gr(begin_arc), PIKUS.first_turn(),
           convert.to_gr(kinks.pikus),
           PIKUS.second_turn(), convert.to_gr(points.PIKUS))
