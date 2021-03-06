import points
import rnav_points
import os
from instruments.route import Route
from instruments import converter as convert
from instruments.draw_route import draw_route, draw_route_tr


file_name = 'uhnn_star_smooth_29_1M'

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

left_turn = Route(start_point=rnav_points.NN013, start_bearing=18,
              begin_arc=rnav_points.NN013, turn1='LEFT', kink=rnav_points.NN009,
              kink_bearing=288).first_turn()

right_turn = Route(start_point=rnav_points.NN011, start_bearing=198,
              begin_arc=rnav_points.NN011, turn1='RIGHT', kink=rnav_points.NN009,
              kink_bearing=288).first_turn()

draw_route(file_name, 'TEBSA1M', convert.to_gr(points.TEBSA), convert.to_gr(rnav_points.NN011),
           right_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route(file_name, 'TOTRU1M', convert.to_gr(points.TOTRU), convert.to_gr(rnav_points.NN011),
           right_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route(file_name, 'DOKIR1M', convert.to_gr(points.DOKIR), convert.to_gr(rnav_points.NN011),
           right_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route(file_name, 'KIZON1M', convert.to_gr(points.KIZON), convert.to_gr(rnav_points.NN017),
           convert.to_gr(rnav_points.NN011),
           right_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route(file_name, 'NOKDA1M', convert.to_gr(points.NOKDA), convert.to_gr(rnav_points.NN017),
           convert.to_gr(rnav_points.NN011),
           right_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route(file_name, 'GIGOR1M', convert.to_gr(points.GIGOR), convert.to_gr(rnav_points.NN012),
           convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route(file_name, 'OSBET1M', convert.to_gr(points.OSBET), convert.to_gr(rnav_points.NN013),
           left_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route(file_name, 'LIRSA1M', convert.to_gr(points.LIRSA), convert.to_gr(rnav_points.NN013),
           left_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route(file_name, 'LEKBI1M', convert.to_gr(points.LEKBI), convert.to_gr(rnav_points.NN013),
           left_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route(file_name, 'RATNU1M', convert.to_gr(points.RATNU), convert.to_gr(rnav_points.NN018),
           convert.to_gr(rnav_points.NN019), convert.to_gr(rnav_points.NN013),
           left_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route(file_name, 'PIKUS1M', convert.to_gr(points.PIKUS), convert.to_gr(rnav_points.NN018),
           convert.to_gr(rnav_points.NN019), convert.to_gr(rnav_points.NN013),
           left_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

#############################################################################################################

draw_route_tr(file_name, 'TEBSA1M', convert.to_gr(points.TEBSA), convert.to_gr(rnav_points.NN011),
           right_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route_tr(file_name, 'TOTRU1M', convert.to_gr(points.TOTRU), convert.to_gr(rnav_points.NN011),
           right_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route_tr(file_name, 'DOKIR1M', convert.to_gr(points.DOKIR), convert.to_gr(rnav_points.NN011),
           right_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route_tr(file_name, 'KIZON1M', convert.to_gr(points.KIZON), convert.to_gr(rnav_points.NN017),
           convert.to_gr(rnav_points.NN011),
           right_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route_tr(file_name, 'NOKDA1M', convert.to_gr(points.NOKDA), convert.to_gr(rnav_points.NN017),
           convert.to_gr(rnav_points.NN011),
           right_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route_tr(file_name, 'GIGOR1M', convert.to_gr(points.GIGOR), convert.to_gr(rnav_points.NN012),
           convert.to_gr(rnav_points.NN008), convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route_tr(file_name, 'OSBET1M', convert.to_gr(points.OSBET), convert.to_gr(rnav_points.NN013),
           left_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route_tr(file_name, 'LIRSA1M', convert.to_gr(points.LIRSA), convert.to_gr(rnav_points.NN013),
           left_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route_tr(file_name, 'LEKBI1M', convert.to_gr(points.LEKBI), convert.to_gr(rnav_points.NN013),
           left_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route_tr(file_name, 'RATNU1M', convert.to_gr(points.RATNU), convert.to_gr(rnav_points.NN018),
           convert.to_gr(rnav_points.NN019), convert.to_gr(rnav_points.NN013),
           left_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))

draw_route_tr(file_name, 'PIKUS1M', convert.to_gr(points.PIKUS), convert.to_gr(rnav_points.NN018),
           convert.to_gr(rnav_points.NN019), convert.to_gr(rnav_points.NN013),
           left_turn, convert.to_gr(rnav_points.NN009), convert.to_gr(points.RW29))
