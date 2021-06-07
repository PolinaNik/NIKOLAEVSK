from instruments import converter as convert
from instruments.distance import distance

DOKIR = convert.str_to_gr('534547'), convert.str_to_gr('1405221')
GIGOR = convert.str_to_gr('532035'), convert.str_to_gr('1414806')
KIZON = convert.str_to_gr('534015'), convert.str_to_gr('1411338')
NOKDA = convert.str_to_gr('533633'), convert.str_to_gr('1412157')
RATNU = convert.str_to_gr('530330'), convert.str_to_gr('1393606')
PIKUS = convert.str_to_gr('531042'), convert.str_to_gr('1393524')
LIRSA = convert.str_to_gr('524116'), convert.str_to_gr('1403230')
OSBET = convert.str_to_gr('523712'), convert.str_to_gr('1411142')
LEKBI = convert.str_to_gr('523755'), convert.str_to_gr('1400253')
TEBSA = convert.str_to_gr('532715'), convert.str_to_gr('1394303')
TOTRU = convert.str_to_gr('534406'), convert.str_to_gr('1401457')

LOM = convert.str_to_gr('530903'), convert.str_to_gr('1404329')
VOR_DME = convert.str_to_gr('530908'), convert.str_to_gr('1404117')

glob_center_sid1a = convert.str_to_gr('530905'), convert.str_to_gr('1403840')
glob_radius_sid1a = distance(glob_center_sid1a, LOM)

glob_center_sid1a_up = convert.str_to_gr('531100'), convert.str_to_gr('1404750')
glob_radius_sid1a_up = distance(glob_center_sid1a_up, (convert.str_to_gr('530845'), convert.str_to_gr('1404750')))

glob_center_sid1a_down = convert.str_to_gr('530620'), convert.str_to_gr('1404700')
glob_radius_sid1a_down = distance(glob_center_sid1a_down, (convert.str_to_gr('530845'), convert.str_to_gr('1404750')))

glob_center_sid1b = convert.str_to_gr('530905'), convert.str_to_gr('1403840')
glob_radius_sid1b = distance(glob_center_sid1b, VOR_DME)

glob_center_sid1b_up = convert.str_to_gr('531100'), convert.str_to_gr('1404750')
glob_radius_sid1b_up = distance(glob_center_sid1a_up, (convert.str_to_gr('530845'), convert.str_to_gr('1404750')))

glob_center_sid1b_down = convert.str_to_gr('530620'), convert.str_to_gr('1404700')
glob_radius_sid1b_down = distance(glob_center_sid1a_down, (convert.str_to_gr('530845'), convert.str_to_gr('1404750')))

glob_center_sid1c_down = convert.str_to_gr('530630'), convert.str_to_gr('1404040')
glob_radius_sid1c_down = distance(glob_center_sid1c_down, LOM)

glob_center_sid1c_up = convert.str_to_gr('531130'), convert.str_to_gr('1404030')
glob_radius_sid1c_up = distance(glob_center_sid1c_up, LOM)

glob_center_sid1d_down = convert.str_to_gr('530655'), convert.str_to_gr('1403750')
glob_radius_sid1d_down = distance(glob_center_sid1d_down, VOR_DME)

glob_center_sid1d_up = convert.str_to_gr('531130'), convert.str_to_gr('1403900')
glob_radius_sid1d_up = distance(glob_center_sid1d_up, VOR_DME)

glob_center_sid1e_down = convert.str_to_gr('530620'), convert.str_to_gr('1404700')
glob_radius_sid1e_down = distance(glob_center_sid1e_down, (convert.str_to_gr('530845'), convert.str_to_gr('1404720')))

glob_center_sid1e_up = convert.str_to_gr('531105'), convert.str_to_gr('1404745')
glob_radius_sid1e_up = distance(glob_center_sid1e_up, (convert.str_to_gr('530845'), convert.str_to_gr('1404720')))

glob_center_sid1f_down = convert.str_to_gr('530730'), convert.str_to_gr('1403100')
glob_radius_sid1f_down = distance(glob_center_sid1f_down, (convert.str_to_gr('530930'), convert.str_to_gr('1403115')))

glob_center_sid1f_up = convert.str_to_gr('531145'), convert.str_to_gr('1403130')
glob_radius_sid1f_up = distance(glob_center_sid1f_up, (convert.str_to_gr('530930'), convert.str_to_gr('1403115')))