import points
import rnav_points
import os
from instruments import converter as convert
from instruments.draw_route import draw_route
from instruments.draw_point import draw_point

file_name = 'uhnn_star(1M)'

try:
    os.remove(f'{file_name}.sld')
except:
    pass

draw_route(file_name, 'TEBSA1M', convert.to_gr(points.TEBSA), convert.to_gr(rnav_points.NN011))
draw_route(file_name, 'TOTRU1M', convert.to_gr(points.TOTRU), convert.to_gr(rnav_points.NN011))
draw_route(file_name, 'DOKIR1M', convert.to_gr(points.DOKIR), convert.to_gr(rnav_points.NN011))
draw_route(file_name, 'KIZON1M', convert.to_gr(points.KIZON), convert.to_gr(rnav_points.NN017),
           convert.to_gr(rnav_points.NN011))
draw_route(file_name, 'NOKDA1M', convert.to_gr(points.NOKDA), convert.to_gr(rnav_points.NN017),
           convert.to_gr(rnav_points.NN011))
draw_route(file_name, 'GIGOR1M', convert.to_gr(points.GIGOR), convert.to_gr(rnav_points.NN012))
draw_route(file_name, 'OSBET1M', convert.to_gr(points.OSBET), convert.to_gr(rnav_points.NN013))
draw_route(file_name, 'LIRSA1M', convert.to_gr(points.LIRSA), convert.to_gr(rnav_points.NN013))
draw_route(file_name, 'LEKBI1M', convert.to_gr(points.LEKBI), convert.to_gr(rnav_points.NN013))
draw_route(file_name, 'RATNU1M', convert.to_gr(points.RATNU), convert.to_gr(rnav_points.NN018),
           convert.to_gr(rnav_points.NN019), convert.to_gr(rnav_points.NN013))
draw_route(file_name, 'PIKUS1M', convert.to_gr(points.PIKUS), convert.to_gr(rnav_points.NN018),
           convert.to_gr(rnav_points.NN019), convert.to_gr(rnav_points.NN013))

draw_point(file_name, rnav_points.NN011, rnav_points.NN012, rnav_points.NN013, rnav_points.NN017, rnav_points.NN018)
