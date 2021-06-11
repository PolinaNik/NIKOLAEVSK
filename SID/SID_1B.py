import points
from instruments.route import Route
from instruments.paralel_route import ParalelRoute
from instruments.round_route import RoundRoute
from instruments import converter as convert
from instruments.draw_route import draw_route
import SID.kinks.kinks_sid1b as kinks
import os

start_point = convert.str_to_gr('530917'), convert.str_to_gr('1403816')
begin_arc = convert.str_to_gr('530845'), convert.str_to_gr('1404750')

gl_center = points.glob_center_sid1b
gl_rad = points.glob_radius_sid1b

gl_center_down = points.glob_center_sid1b_down
gl_rad_down = points.glob_radius_sid1b_down

gl_center_up = points.glob_center_sid1b_up
gl_rad_up = points.glob_radius_sid1b_up

file_name = 'uhnn_sid(1b)'

try:
    os.remove(f'{file_name}.sld')
except:
    pass

TEBSA = RoundRoute(start_point=start_point, start_bearing=108,
                   begin_arc=begin_arc, turn1='RIGHT', glob_center=gl_center_down, glob_rad=gl_rad_down,
                   kink=points.VOR_DME,
                   glob_center2=gl_center, glob_rad2=gl_rad, turn2='LEFT', end_bearing=311, end_point=points.TEBSA)

TOTRU = ParalelRoute(start_point=start_point, start_bearing=108,
                     begin_arc=begin_arc, turn1='LEFT', glob_center=gl_center_up, glob_rad=gl_rad_up, kink=kinks.totru,
                     kink_bearing=277, turn2='RIGHT', end_bearing=349, end_point=points.TOTRU)

DOKIR = Route(start_point=start_point, start_bearing=108,
              begin_arc=begin_arc, turn1='LEFT', kink=kinks.dokir,
              kink_bearing=323, turn2='RIGHT', end_bearing=23, end_point=points.DOKIR)

KIZON = Route(start_point=start_point, start_bearing=108,
              begin_arc=begin_arc, turn1='LEFT', kink=kinks.kizon,
              kink_bearing=358, turn2='RIGHT', end_bearing=45, end_point=points.KIZON)

NOKDA = Route(start_point=start_point, start_bearing=108,
              begin_arc=begin_arc, turn1='LEFT', kink=kinks.nokda,
              kink_bearing=15, turn2='RIGHT', end_bearing=54, end_point=points.NOKDA)

GIGOR = Route(start_point=start_point, start_bearing=108,
              begin_arc=begin_arc, turn1='LEFT', kink=kinks.gigor,
              kink_bearing=71, turn2='RIGHT', end_bearing=87, end_point=points.GIGOR)

OSBET = Route(start_point=start_point, start_bearing=108,
              begin_arc=begin_arc, turn1='RIGHT', kink=kinks.osbet,
              kink_bearing=204, turn2='LEFT', end_bearing=163, end_point=points.OSBET)

LIRSA = Route(start_point=start_point, start_bearing=108,
              begin_arc=begin_arc, turn1='RIGHT', kink=kinks.lirsa,
              kink_bearing=270, turn2='LEFT', end_bearing=204, end_point=points.LIRSA)

LEKBI = ParalelRoute(start_point=start_point, start_bearing=108,
                     begin_arc=begin_arc, turn1='RIGHT', glob_center=gl_center_down, glob_rad=gl_rad_down,
                     kink=kinks.lekbi,
                     kink_bearing=302, turn2='LEFT', end_bearing=230, end_point=points.LEKBI)

RATNU = RoundRoute(start_point=start_point, start_bearing=108,
                   begin_arc=begin_arc, turn1='LEFT', glob_center=gl_center_up, glob_rad=gl_rad_up, kink=points.LOM,
                   glob_center2=gl_center, glob_rad2=gl_rad, turn2='RIGHT', end_bearing=275, end_point=points.RATNU)

PIKUS = RoundRoute(start_point=start_point, start_bearing=108,
                   begin_arc=begin_arc, turn1='LEFT', glob_center=gl_center_up, glob_rad=gl_rad_up, kink=points.LOM,
                   glob_center2=gl_center, glob_rad2=gl_rad, turn2='RIGHT', end_bearing=286, end_point=points.PIKUS)

draw_route(file_name, 'TEBSA1B', convert.to_gr(start_point), convert.to_gr(begin_arc), TEBSA.first_turn(),
           convert.to_gr(points.LOM),
           TEBSA.glob_round(), TEBSA.second_turn(), convert.to_gr(points.TEBSA))

draw_route(file_name, 'TOTRU1B', convert.to_gr(start_point), convert.to_gr(begin_arc), TOTRU.first_turn(),
           convert.to_gr(kinks.totru),
           TOTRU.second_turn(), convert.to_gr(points.TOTRU))

draw_route(file_name, 'DOKIR1B', convert.to_gr(start_point), convert.to_gr(begin_arc), DOKIR.first_turn(),
           convert.to_gr(kinks.dokir),
           DOKIR.second_turn(), convert.to_gr(points.DOKIR))

draw_route(file_name, 'KIZON1B', convert.to_gr(start_point), convert.to_gr(begin_arc), KIZON.first_turn(),
           convert.to_gr(kinks.kizon),
           KIZON.second_turn(), convert.to_gr(points.KIZON))

draw_route(file_name, 'NOKDA1B', convert.to_gr(start_point), convert.to_gr(begin_arc), NOKDA.first_turn(),
           convert.to_gr(kinks.nokda),
           NOKDA.second_turn(), convert.to_gr(points.NOKDA))

draw_route(file_name, 'GIGOR1B', convert.to_gr(start_point), convert.to_gr(begin_arc), GIGOR.first_turn(),
           convert.to_gr(kinks.gigor),
           GIGOR.second_turn(), convert.to_gr(points.GIGOR))

draw_route(file_name, 'OSBET1B', convert.to_gr(start_point), convert.to_gr(begin_arc), OSBET.first_turn(),
           convert.to_gr(kinks.osbet),
           OSBET.second_turn(), convert.to_gr(points.OSBET))

draw_route(file_name, 'LIRSA1B', convert.to_gr(start_point), convert.to_gr(begin_arc), LIRSA.first_turn(),
           convert.to_gr(kinks.lirsa),
           LIRSA.second_turn(), convert.to_gr(points.LIRSA))

draw_route(file_name, 'LEKBI1B', convert.to_gr(start_point), convert.to_gr(begin_arc), LEKBI.first_turn(),
           convert.to_gr(kinks.lekbi),
           LEKBI.second_turn(), convert.to_gr(points.LEKBI))

draw_route(file_name, 'RATNU1B', convert.to_gr(start_point), convert.to_gr(begin_arc), RATNU.first_turn(),
           convert.to_gr(points.LOM),
           RATNU.glob_round(), RATNU.second_turn(), convert.to_gr(points.RATNU))

draw_route(file_name, 'PIKUS1B', convert.to_gr(start_point), convert.to_gr(begin_arc), PIKUS.first_turn(),
           convert.to_gr(points.LOM),
           PIKUS.glob_round(), PIKUS.second_turn(), convert.to_gr(points.PIKUS))
