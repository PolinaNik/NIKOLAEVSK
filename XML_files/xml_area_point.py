import re
from XML_files import converter as cv

with open('nik_area_points.py', 'r') as file:
    NN_points = file.readlines()

new = []
pat = re.compile(r'\d+')
pat2 = re.compile(r'nik_area')
for item in NN_points:
    spisok = pat.findall(item)
    name = pat2.search(item).group()
    lst = [name+spisok[0], cv.str_N(spisok[1]), cv.str_E(spisok[2])]
    new.append(lst)


def fill_pnt(cords):
    for item in cords:
        str_01 = '        <rec>\n'
        str_02 = f'            <c i="name" v="{item[0]}" />\n'
        str_03 = '            <c i="region" v="" />\n'
        str_04 = '            <c i="prizn" v="" />\n'
        str_05 = '            <c i="attr" v="" />\n'
        str_06 = '            <c i="base" v="" />\n'
        str_07 = f'            <c i="x" v="{item[1]}" />\n'
        str_08 = f'            <c i="y" v="{item[2]}" />\n'
        str_09 = '            <c i="kurs_lur" v="" />\n'
        str_10 = '            <c i="nmtrvzl" v="" />\n'
        str_11 = '            <c i="cmt" v="" />\n'
        str_12 = '            <c i="dmv" v="" />\n'
        str_13 = '        </rec>\n'
        lst = [str_01, str_02, str_03, str_04, str_05, str_06, str_07,
               str_08, str_09, str_10, str_11, str_12, str_13]
        yield lst

result = list(fill_pnt(new))

with open('result_pnt_area.xml', 'w') as file:
    for lst in result:
        for item in lst:
            file.write(item)







