import points
import rnav_points
import os
from instruments.route import RNAVRoute
from instruments import converter as convert
from instruments.draw_route import draw_route, draw_route_tr


file_name = 'uhnn_star(1l)_smooth'

try:
    os.remove(f'{file_name}.sld')
except:
    pass

file_name_tr = 'uhnn_star(1l)_smooth_tr'

try:
    os.remove(f'{file_name_tr}.txt')
except:
    pass

if not os.path.exists('ROUTES'):
    os.makedirs('ROUTES')

if not os.path.exists('KST_ROUTES'):
    os.makedirs('KST_ROUTES')

left_turn = RNAVRoute(start_point=rnav_points.NN003, start_bearing=198,
              begin_arc=rnav_points.NN003, turn1='LEFT', kink=rnav_points.NN005,
              kink_bearing=107).first_turn()

right_turn = RNAVRoute(start_point=rnav_points.NN001, start_bearing=18,
              begin_arc=rnav_points.NN001, turn1='RIGHT', kink=rnav_points.NN005,
              kink_bearing=107).first_turn()

draw_route(file_name, 'TOTRU1L', convert.to_gr(points.TOTRU), convert.to_gr(rnav_points.NN003),
           left_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route(file_name, 'DOKIR1L', convert.to_gr(points.DOKIR), convert.to_gr(rnav_points.NN003),
           left_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route(file_name, 'KIZON1L', convert.to_gr(points.KIZON), convert.to_gr(rnav_points.NN015),
           convert.to_gr(rnav_points.NN003), left_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route(file_name, 'GIGOR1L', convert.to_gr(points.KIZON), convert.to_gr(rnav_points.NN015),
           convert.to_gr(rnav_points.NN003), left_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route(file_name, 'LEKBI1L', convert.to_gr(points.LEKBI), convert.to_gr(rnav_points.NN001),
           right_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route(file_name, 'LIRSA1L', convert.to_gr(points.LIRSA), convert.to_gr(rnav_points.NN016),
           convert.to_gr(rnav_points.NN001), right_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route(file_name, 'OSBET1L', convert.to_gr(points.OSBET), convert.to_gr(rnav_points.NN016),
           convert.to_gr(rnav_points.NN001), right_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))


draw_route(file_name, 'TEBSA1L', convert.to_gr(points.TEBSA), convert.to_gr(rnav_points.NN002),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route(file_name, 'PIKUS1L', convert.to_gr(points.PIKUS), convert.to_gr(rnav_points.NN002),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route(file_name, 'RATNU1L', convert.to_gr(points.RATNU), convert.to_gr(rnav_points.NN002),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

###################################################################################################

draw_route_tr(file_name_tr, 'TOTRU1L', convert.to_gr(points.TOTRU), convert.to_gr(rnav_points.NN003),
           left_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route_tr(file_name_tr, 'DOKIR1L', convert.to_gr(points.DOKIR), convert.to_gr(rnav_points.NN003),
           left_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route_tr(file_name_tr, 'KIZON1L', convert.to_gr(points.KIZON), convert.to_gr(rnav_points.NN015),
           convert.to_gr(rnav_points.NN003), left_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route_tr(file_name_tr, 'GIGOR1L', convert.to_gr(points.KIZON), convert.to_gr(rnav_points.NN015),
           convert.to_gr(rnav_points.NN003), left_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route_tr(file_name_tr, 'LEKBI1L', convert.to_gr(points.LEKBI), convert.to_gr(rnav_points.NN001),
           right_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route_tr(file_name_tr, 'LIRSA1L', convert.to_gr(points.LIRSA), convert.to_gr(rnav_points.NN016),
           convert.to_gr(rnav_points.NN001), right_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route_tr(file_name_tr, 'OSBET1L', convert.to_gr(points.OSBET), convert.to_gr(rnav_points.NN016),
           convert.to_gr(rnav_points.NN001), right_turn, convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))


draw_route_tr(file_name_tr, 'TEBSA1L', convert.to_gr(points.TEBSA), convert.to_gr(rnav_points.NN002),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route_tr(file_name_tr, 'PIKUS1L', convert.to_gr(points.PIKUS), convert.to_gr(rnav_points.NN002),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))

draw_route_tr(file_name_tr, 'RATNU1L', convert.to_gr(points.RATNU), convert.to_gr(rnav_points.NN002),
           convert.to_gr(rnav_points.NN004), convert.to_gr(rnav_points.NN005), convert.to_gr(points.RW11))
