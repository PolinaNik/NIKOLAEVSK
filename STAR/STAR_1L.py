import points
import rnav_points
import os
from instruments import converter as convert
from instruments.draw_route import draw_route
from instruments.draw_point import draw_point

file_name = 'uhnn_star(1l)'

try:
    os.remove(f'{file_name}.sld')
except:
    pass

draw_route(file_name, 'TEBSA1L', convert.to_gr(points.TEBSA), convert.to_gr(rnav_points.NN002))
draw_route(file_name, 'TOTRU1L', convert.to_gr(points.TOTRU), convert.to_gr(rnav_points.NN003))
draw_route(file_name, 'DOKIR1L', convert.to_gr(points.DOKIR), convert.to_gr(rnav_points.NN003))
draw_route(file_name, 'KIZON1L', convert.to_gr(points.KIZON), convert.to_gr(rnav_points.NN015),
           convert.to_gr(rnav_points.NN003))
draw_route(file_name, 'NOKDA1L', convert.to_gr(points.NOKDA), convert.to_gr(rnav_points.NN015),
           convert.to_gr(rnav_points.NN003))
draw_route(file_name, 'GIGOR1L', convert.to_gr(points.GIGOR), convert.to_gr(rnav_points.NN003))
draw_route(file_name, 'OSBET1L', convert.to_gr(points.OSBET), convert.to_gr(rnav_points.NN016),
           convert.to_gr(rnav_points.NN001))
draw_route(file_name, 'LIRSA1L', convert.to_gr(points.LIRSA), convert.to_gr(rnav_points.NN016),
           convert.to_gr(rnav_points.NN001))
draw_route(file_name, 'LEKBI1L', convert.to_gr(points.LEKBI), convert.to_gr(rnav_points.NN001))
draw_route(file_name, 'RATNU1L', convert.to_gr(points.RATNU), convert.to_gr(rnav_points.NN002))
draw_route(file_name, 'PIKUS1L', convert.to_gr(points.PIKUS), convert.to_gr(rnav_points.NN002))

draw_point(file_name, rnav_points.NN001, rnav_points.NN002, rnav_points.NN003, rnav_points.NN015, rnav_points.NN016)
