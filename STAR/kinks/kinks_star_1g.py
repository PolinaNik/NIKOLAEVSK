from instruments.destination_point import destination_point
import points
from instruments import converter as convert


tebsa_kink = destination_point(points.VOR_DME, (130+180-13), 60)
totru_kink = destination_point(points.VOR_DME, (169+180-13), 60)
dokir_kink = destination_point(points.VOR_DME, (203-180-13), 60)
kizon_kink = destination_point(points.VOR_DME, (225-180-13), 60)
nokda_kink = destination_point(points.VOR_DME, (235-180-13), 60)
gigor_kink = destination_point(points.VOR_DME, (267-180-13), 60)
osbet_kink = destination_point(points.VOR_DME, (343-180-13), 60)
lirsa_kink = destination_point(points.VOR_DME, (23+180-13), 60)
lekbi_kink = destination_point(points.VOR_DME, (49+180-13), 60)
ratnu_kink = destination_point(points.VOR_DME, (94+180-13), 60)
pikus_kink = destination_point(points.VOR_DME, (105+180-13), 60)


kink_left_down = convert.str_to_gr('530605'), convert.str_to_gr('1403550')
kink_right_up = convert.str_to_gr('530845'), convert.str_to_gr('1404430')
kink_right_down = convert.str_to_gr('530607'), convert.str_to_gr('1404200')
