import re
from XML_files import converter as cv
import os

list_of_files_star = os.listdir('../STAR/KST_ROUTES')
list_of_files_sid = os.listdir('../SID/KST_ROUTES')

all_parts = []
sid_parts = []
star_parts = []
for file in list_of_files_star:
    with open(f'../STAR/KST_ROUTES/{file}', 'r') as text:
        star = text.read()
        all_star = star.split('NNNN')
        parts = [list(filter(None, x.split('\n'))) for x in all_star]
        all_parts.append(parts)
        star_parts.append(parts)

for file in list_of_files_sid:
    with open(f'../SID/KST_ROUTES/{file}', 'r') as text:
        sid = text.read()
        all_sid = sid.split('NNNN')
        parts = [list(filter(None, x.split('\n'))) for x in all_sid]
        all_parts.append(parts)
        sid_parts.append(parts)


def fill_pnt(cords):
    uniqie_names = []
    for item in cords:
        for element in item:
            if element != []:
                for num, cord in enumerate(element):
                    if num != 0:
                        line = cord.split(" ")
                        if line[0] not in uniqie_names:
                            uniqie_names.append(line[0])
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

with open('ALL_points.xml', 'w') as file:
    for lst in result:
        for item in lst:
            file.write(item)


def fill_prlet(cords, list_files):
    pat = re.compile(r'\d\d')
    pat2 = re.compile(r'..(?=\.)')
    for item_num, item in enumerate(cords):
        for element in item:
            if element != []:
                name = list_files[item_num]
                rw = pat.search(name).group()
                namei = pat2.search(name).group()
                str_01 = '        <rec>\n'
                str_02 = f'            <c i="name" v="{element[0][0:5]}" />\n'
                str_03 = f'            <c i="kurs" v="{rw} UHNN" />\n'
                str_04 = f'            <c i="namei" v="{element[0][0:5]}{namei} " />\n'
                str_05 = '            <dtable i="points">\n'
                first_part = [str_01, str_02, str_03, str_04, str_05]
                points = []
                for point in element:
                    line = point.split(" ")
                    if len(line) > 2:
                        str_06 = '                <rec>\n'
                        str_07 = f'                    <c i="tname" v="{line[0]}" />\n'
                        str_08 = '                </rec>\n'
                        second_part = [str_06, str_07, str_08]
                        points = points + second_part
                result = first_part + points
                length = len(item)
                if length < 50:
                    remain = 50 - length
                    remain_zero_points = []
                    for i in range(1, remain + 1):
                        str_06 = '                <rec>\n'
                        str_07 = f'                    <c i="tname" v="" />\n'
                        str_08 = '                </rec>\n'
                        second_part = [str_06, str_07, str_08]
                        remain_zero_points = remain_zero_points + second_part
                    result += remain_zero_points
                    str_end0 = '            </dtable>\n'
                    str_end = '        </rec>\n'
                    result += str_end0
                    result += [str_end]
                    yield result




sid_routes = list(fill_prlet(sid_parts, list_of_files_sid))
with open('SID_routes.xml', 'w') as file:
    for item in sid_routes:
        for elem in item:
            file.write(elem)

star_routes = list(fill_prlet(star_parts, list_of_files_star))
with open('STAR_routes.xml', 'w') as file:
    for item in star_routes:
        for elem in item:
            file.write(elem)

