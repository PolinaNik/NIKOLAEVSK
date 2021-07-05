with open('../STAR/KST_ROUTES/uhnn_star(1g_11)_tr.txt', 'r') as file:
    star_1l = file.read()

with open('../STAR/KST_ROUTES/uhnn_star(1g_29)_tr.txt', 'r') as file:
    star_1m = file.read()

all_1g_11 = star_1l.split('NNNN')
parts_1g_11 = [list(filter(None, x.split('\n'))) for x in all_1g_11]

all_1g_29 = star_1m.split('NNNN')
parts_1g_29 = [list(filter(None, x.split('\n'))) for x in all_1g_29]


def fill_prlet(cords, RW):
    for item in cords:
        if item != [] :
            str_01 = '        <rec>\n'
            str_02 = f'            <c i="name" v="{item[0][0:5]}" />\n'
            str_03 = f'            <c i="kurs" v="{RW} UHNN" />\n'
            str_04 = f'            <c i="namei" v="{item[0][0:7]} " />\n'
            str_05 = '            <dtable i="points">\n'
            first_part = [str_01, str_02, str_03, str_04, str_05]
            points = []
            for num, point in enumerate(item):
                if num != 0:
                    str_06 = '                <rec>\n'
                    str_07 = f'                    <c i="tname" v="{point.split(" ")[0]}" />\n'
                    str_08 = '                </rec>\n'
                    second_part = [str_06, str_07, str_08]
                    points = points + second_part
            result = first_part+points
            length = len(item)
            if length < 50:
                remain = 50-length
                remain_zero_points = []
                for i in range(1, remain+1):
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

test = list(fill_prlet(parts_1g_11, '11'))
with open('STAR/star_1G_11.xml', 'w') as file:
    for item in test:
        for elem in item:
            file.write(elem)

test = list(fill_prlet(parts_1g_29,  '29'))
with open('STAR/star_1G_29.xml', 'w') as file:
    for item in test:
        for elem in item:
            file.write(elem)




