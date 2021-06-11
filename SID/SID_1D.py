import points
from instruments.route import Route
from instruments.heart_route import HeartRoute
from instruments import converter as convert
from instruments.draw_route import draw_route
import SID.kinks.kinks_sid1d as kinks
import os

start_point = convert.str_to_gr('530900'), convert.str_to_gr('1403945')
begin_arc = convert.str_to_gr('530925'), convert.str_to_gr('1403110')

gl_center_down = points.glob_center_sid1d_down
gl_rad_down = points.glob_radius_sid1d_down

gl_center_up = points.glob_center_sid1d_up
gl_rad_up = points.glob_radius_sid1d_up

file_name = 'uhnn_sid(1d)'

try:
    os.remove(f'{file_name}.sld')
except:
    pass

TEBSA = Route(start_point=start_point, start_bearing=288,
              begin_arc=begin_arc, turn1='RIGHT', kink=kinks.tebsa,
              kink_bearing=335, turn2='LEFT', end_bearing=311, end_point=points.TEBSA)

TOTRU = Route(start_point=start_point, start_bearing=288,
              begin_arc=begin_arc, turn1='RIGHT', kink=kinks.totru,
              kink_bearing=55, turn2='LEFT', end_bearing=349, end_point=points.TOTRU)

DOKIR = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="LEFT", kink=points.VOR_DME,
                   turn2="LEFT", round_kink=kinks.lekbi, round_bearing=167,
                   glob_center=gl_center_up, glob_rad=gl_rad_up, last_turn="LEFT",
                   az_turn=350, end_bearing=23, end_point=points.DOKIR)

KIZON = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="LEFT", kink=points.VOR_DME,
                   turn2="LEFT", round_kink=kinks.lekbi, round_bearing=167,
                   glob_center=gl_center_up, glob_rad=gl_rad_up, last_turn="LEFT",
                   az_turn=350, end_bearing=45, end_point=points.KIZON)

NOKDA = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="LEFT", kink=points.VOR_DME,
                   turn2="LEFT", round_kink=kinks.lekbi, round_bearing=167,
                   glob_center=gl_center_up, glob_rad=gl_rad_up, last_turn="LEFT",
                   az_turn=350, end_bearing=54, end_point=points.NOKDA)

GIGOR = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="LEFT", kink=points.VOR_DME,
                   turn2="LEFT", round_kink=kinks.lekbi, round_bearing=167,
                   glob_center=gl_center_up, glob_rad=gl_rad_up, last_turn="LEFT",
                   az_turn=350, end_bearing=87, end_point=points.GIGOR)

OSBET = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="RIGHT", kink=points.VOR_DME,
                   turn2="RIGHT", round_kink=kinks.totru, round_bearing=55,
                   glob_center=gl_center_down, glob_rad=gl_rad_down, last_turn="RIGHT",
                   az_turn=230, end_bearing=163, end_point=points.OSBET)

LIRSA = HeartRoute(start_point=start_point, start_bearing=288,
                   begin_arc=begin_arc, turn1="RIGHT", kink=points.VOR_DME,
                   turn2="RIGHT", round_kink=kinks.totru, round_bearing=55,
                   glob_center=gl_center_down, glob_rad=gl_rad_down, last_turn="RIGHT",
                   az_turn=230, end_bearing=204, end_point=points.LIRSA)

LEKBI = Route(start_point=start_point, start_bearing=288,
              begin_arc=begin_arc, turn1='LEFT', kink=kinks.lekbi,
              kink_bearing=167, turn2='RIGHT', end_bearing=230, end_point=points.LEKBI)

RATNU = Route(start_point=start_point, start_bearing=288,
              begin_arc=begin_arc, turn1='LEFT', kink=kinks.ratnu,
              kink_bearing=248, turn2='RIGHT', end_bearing=275, end_point=points.RATNU)

PIKUS = Route(start_point=start_point, start_bearing=288,
              begin_arc=begin_arc, turn1='LEFT', kink=kinks.ratnu,
              kink_bearing=248, turn2='RIGHT', end_bearing=286, end_point=points.PIKUS)

draw_route(file_name, 'TEBSA1D', convert.to_gr(start_point), convert.to_gr(begin_arc), TEBSA.first_turn(),
           convert.to_gr(kinks.tebsa),
           TEBSA.second_turn(), convert.to_gr(points.TEBSA))

draw_route(file_name, 'TOTRU1D', convert.to_gr(start_point), convert.to_gr(begin_arc), TOTRU.first_turn(),
           convert.to_gr(kinks.totru),
           TOTRU.second_turn(), convert.to_gr(points.TOTRU))

draw_route(file_name, 'DOKIR1D', convert.to_gr(start_point), convert.to_gr(begin_arc), DOKIR.first_round(),
           convert.to_gr(points.VOR_DME),
           DOKIR.glob_round(), DOKIR.second_turn(), convert.to_gr(points.DOKIR))

draw_route(file_name, 'KIZON1D', convert.to_gr(start_point), convert.to_gr(begin_arc), KIZON.first_round(),
           convert.to_gr(points.VOR_DME),
           convert.to_gr(points.KIZON))

draw_route(file_name, 'NOKDA1D', convert.to_gr(start_point), convert.to_gr(begin_arc), NOKDA.first_round(),
           convert.to_gr(points.VOR_DME),
           convert.to_gr(points.NOKDA))

draw_route(file_name, 'GIGOR1D', convert.to_gr(start_point), convert.to_gr(begin_arc), GIGOR.first_round(),
           convert.to_gr(points.VOR_DME),
           convert.to_gr(points.GIGOR))

draw_route(file_name, 'OSBET1D', convert.to_gr(start_point), convert.to_gr(begin_arc), OSBET.first_round(),
           convert.to_gr(points.VOR_DME),
           convert.to_gr(points.OSBET))

draw_route(file_name, 'LIRSA1D', convert.to_gr(start_point), convert.to_gr(begin_arc), LIRSA.first_round(),
           convert.to_gr(points.VOR_DME),
           LIRSA.glob_round(), LIRSA.second_turn(), convert.to_gr(points.LIRSA))

draw_route(file_name, 'LEKBI1D', convert.to_gr(start_point), convert.to_gr(begin_arc), LEKBI.first_turn(),
           convert.to_gr(kinks.lekbi),
           LEKBI.second_turn(), convert.to_gr(points.LEKBI))

draw_route(file_name, 'RATNU1D', convert.to_gr(start_point), convert.to_gr(begin_arc), RATNU.first_turn(),
           convert.to_gr(kinks.ratnu),
           RATNU.second_turn(), convert.to_gr(points.RATNU))

draw_route(file_name, 'PIKUS1D', convert.to_gr(start_point), convert.to_gr(begin_arc), PIKUS.first_turn(),
           convert.to_gr(kinks.pikus),
           PIKUS.second_turn(), convert.to_gr(points.PIKUS))
