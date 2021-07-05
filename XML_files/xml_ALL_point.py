import re
from XML_files import converter as cv
import os

list_of_files = os.listdir('../STAR/KST_ROUTES')

all_parts = []
for file in list_of_files:
    with open(f'../STAR/KST_ROUTES/{file}', 'r') as text:
        star = text.read()
        all_star = star.split('NNNN')
        parts = [list(filter(None, x.split('\n'))) for x in all_star]
        all_parts.append(parts)

def fill_pnt(cords):
    for item in cords:
        for element in item:
            if element != []:
                for num, cord in enumerate(element):
                    if num != 0:
                        line = cord.split(" ")
                        str_01 = '        <rec>\n'
                        str_02 = f'            <c i="name" v="{line[0]}" />\n'
                        str_03 = '            <c i="region" v="" />\n'
                        str_04 = '            <c i="prizn" v="" />\n'
                        str_05 = '            <c i="attr" v="" />\n'
                        str_06 = '            <c i="base" v="" />\n'
                        str_07 = f'            <c i="x" v="{line[3]}" />\n'
                        str_08 = f'            <c i="y" v="{line[4]}" />\n'
                        str_09 = '            <c i="kurs_lur" v="" />\n'
                        str_10 = '            <c i="nmtrvzl" v="" />\n'
                        str_11 = '            <c i="cmt" v="" />\n'
                        str_12 = '            <c i="dmv" v="" />\n'
                        str_13 = '        </rec>\n'
                        lst = [str_01, str_02, str_03, str_04, str_05, str_06, str_07,
                               str_08, str_09, str_10, str_11, str_12, str_13]
                        yield lst

result = list(fill_pnt(all_parts))

with open('STAR_points.xml', 'w') as file:
    for lst in result:
        for item in lst:
            file.write(item)







