from instruments.hippodrome_sector import Hippo_left
import points
from STAR.kinks import kinks_star_1g as kinks
from instruments import converter as convert
from instruments.paralel_route import ParalelRoute
import os
from instruments.draw_route import draw_route, draw_route_tr

file_name = 'uhnn_star(1k_11)'
right_center = points.right_center_star_1g_11
left_center = points.left_center_star_1g_11
start_point = convert.str_to_gr('530917'), convert.str_to_gr('1403945')
rad = points.rad_star_1g_11

try:
    os.remove(f'{file_name}.sld')
except:
    pass

file_name_tr = 'uhnn_star(1k_11)_tr'

try:
    os.remove(f'{file_name_tr}.txt')
except:
    pass

if not os.path.exists('ROUTES'):
    os.makedirs('ROUTES')

if not os.path.exists('KST_ROUTES'):
    os.makedirs('KST_ROUTES')

right_turn1 = ParalelRoute(start_bearing=108, begin_arc=points.VOR_DME, turn1='RIGHT', glob_center=right_center,
                           glob_rad=rad)
right_turn2 = ParalelRoute(start_bearing=288, begin_arc=kinks.kink_left_down, turn1='RIGHT', glob_center=left_center,
                           glob_rad=rad)
hippo2 = Hippo_left(start_bearing=108, intersection=points.VOR_DME, sector=2)
hippo1 = Hippo_left(start_bearing=108, intersection=points.VOR_DME, sector=1)

draw_route(file_name, 'RATNU1K_11', convert.to_gr(points.RATNU), convert.to_gr(points.VOR_DME),
           right_turn1.first_turn(), convert.to_gr(kinks.kink_left_down), right_turn2.first_turn(),
           convert.to_gr(start_point))

draw_route(file_name, 'PIKUS1K_11', convert.to_gr(points.PIKUS), convert.to_gr(start_point))

draw_route(file_name, 'TEBSA1K_11', convert.to_gr(points.TEBSA), convert.to_gr(points.VOR_DME),
           right_turn1.first_turn(), convert.to_gr(kinks.kink_left_down), right_turn2.first_turn(),
           convert.to_gr(start_point))

draw_route(file_name, 'TOTRU1K_11', convert.to_gr(points.TOTRU), convert.to_gr(points.VOR_DME), hippo2.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'DOKIR1K_11', convert.to_gr(points.DOKIR), convert.to_gr(points.VOR_DME), hippo2.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'KIZON1K_11', convert.to_gr(points.KIZON), convert.to_gr(points.VOR_DME), hippo2.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'NOKDA1K_11', convert.to_gr(points.NOKDA), convert.to_gr(points.VOR_DME), hippo2.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'GIGOR1K_11', convert.to_gr(points.GIGOR), convert.to_gr(points.VOR_DME), hippo2.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'OSBET1K_11', convert.to_gr(points.OSBET), convert.to_gr(points.VOR_DME), hippo1.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'LIRSA1K_11', convert.to_gr(points.LIRSA), convert.to_gr(points.VOR_DME), hippo1.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route(file_name, 'LEKBI1K_11', convert.to_gr(points.LEKBI), convert.to_gr(points.VOR_DME), hippo1.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

#####################################################################################################################

draw_route_tr(file_name_tr, 'RATNU1K_11', convert.to_gr(points.RATNU), convert.to_gr(points.VOR_DME),
           right_turn1.first_turn(), convert.to_gr(kinks.kink_left_down), right_turn2.first_turn(),
           convert.to_gr(start_point))

draw_route_tr(file_name_tr, 'PIKUS1K_11', convert.to_gr(points.PIKUS), convert.to_gr(start_point))

draw_route_tr(file_name_tr, 'TEBSA1K_11', convert.to_gr(points.TEBSA), convert.to_gr(points.VOR_DME),
           right_turn1.first_turn(), convert.to_gr(kinks.kink_left_down), right_turn2.first_turn(),
           convert.to_gr(start_point))

draw_route_tr(file_name_tr, 'TOTRU1K_11', convert.to_gr(points.TOTRU), convert.to_gr(points.VOR_DME), hippo2.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route_tr(file_name_tr, 'DOKIR1K_11', convert.to_gr(points.DOKIR), convert.to_gr(points.VOR_DME), hippo2.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route_tr(file_name_tr, 'KIZON1K_11', convert.to_gr(points.KIZON), convert.to_gr(points.VOR_DME), hippo2.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route_tr(file_name_tr, 'NOKDA1K_11', convert.to_gr(points.NOKDA), convert.to_gr(points.VOR_DME), hippo2.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route_tr(file_name_tr, 'GIGOR1K_11', convert.to_gr(points.GIGOR), convert.to_gr(points.VOR_DME), hippo2.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route_tr(file_name_tr, 'OSBET1K_11', convert.to_gr(points.OSBET), convert.to_gr(points.VOR_DME), hippo1.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route_tr(file_name_tr, 'LIRSA1K_11', convert.to_gr(points.LIRSA), convert.to_gr(points.VOR_DME), hippo1.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))

draw_route_tr(file_name_tr, 'LEKBI1K_11', convert.to_gr(points.LEKBI), convert.to_gr(points.VOR_DME), hippo1.first_turn(),
           right_turn1.first_turn(), right_turn2.first_turn(), convert.to_gr(start_point))
