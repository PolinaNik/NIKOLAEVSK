from instruments.hippodrome_sector import Hippo
import points
from STAR.kinks import kinks_star_1g as kinks
from instruments import converter as convert
from instruments.paralel_route import ParalelRoute
import os
from instruments.draw_route import draw_route

file_name = 'uhnn_star(1g_11)'
center = points.center_star_1g_11
left_center = points.left_center_star_1g_11
right_center = points.right_center_star_1g_11
start_point = convert.str_to_gr('530917'), convert.str_to_gr('1403945')
rad = points.rad_star_1g_11

try:
    os.remove(f'{file_name}.sld')
except:
    pass


right_turn1 = ParalelRoute(start_bearing=108, begin_arc=points.VOR_DME, turn1='RIGHT', glob_center=center, glob_rad=rad)
right_turn2 = ParalelRoute(start_bearing=288, begin_arc=kinks.kink_left_down, turn1='RIGHT', glob_center=left_center, glob_rad=rad)
#right_turn3 = ParalelRoute(start_bearing=108, begin_arc=kinks.kink_right_up, turn1='RIGHT', glob_center=right_center, glob_rad=rad)
hippo2 = Hippo(start_bearing=108, intersection=points.VOR_DME, sector=2)
hippo1 = Hippo(start_bearing=108, intersection=points.VOR_DME, sector=1)

draw_route(file_name, 'RATNU1G', convert.to_gr(points.RATNU), convert.to_gr(kinks.ratnu_kink), convert.to_gr(points.VOR_DME), right_turn1.first_turn(),
           convert.to_gr(kinks.kink_left_down), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'PIKUS1G', convert.to_gr(points.PIKUS), convert.to_gr(kinks.pikus_kink), convert.to_gr(start_point))

draw_route(file_name, 'TEBSA1G', convert.to_gr(points.TEBSA), convert.to_gr(kinks.tebsa_kink), convert.to_gr(points.VOR_DME), right_turn1.first_turn(),
           convert.to_gr(kinks.kink_left_down), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'TOTRU1G', convert.to_gr(points.TOTRU), convert.to_gr(points.VOR_DME), hippo2.first_turn(), right_turn1.first_turn(),
           right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'DOKIR1G', convert.to_gr(points.DOKIR), convert.to_gr(points.VOR_DME), hippo2.first_turn(), right_turn1.first_turn(),
           right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'KIZON1G', convert.to_gr(points.KIZON), convert.to_gr(points.VOR_DME), hippo2.first_turn(), right_turn1.first_turn(),
           right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'NOKDA1G', convert.to_gr(points.NOKDA), convert.to_gr(points.VOR_DME), hippo2.first_turn(), right_turn1.first_turn(),
           right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'GIGOR1G', convert.to_gr(points.GIGOR), convert.to_gr(points.VOR_DME), hippo2.first_turn(), right_turn1.first_turn(),
           right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'OSBET1G', convert.to_gr(points.OSBET), convert.to_gr(points.VOR_DME), hippo1.first_turn(), right_turn1.first_turn(),
           right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'LIRSA1G', convert.to_gr(points.LIRSA), convert.to_gr(points.VOR_DME), hippo1.first_turn(), right_turn1.first_turn(),
           right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'LEKBI1G', convert.to_gr(points.LEKBI), convert.to_gr(points.VOR_DME), hippo1.first_turn(), right_turn1.first_turn(),
           right_turn2.first_turn(), convert.to_gr(start_point))








