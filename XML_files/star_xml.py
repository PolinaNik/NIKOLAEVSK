with open('../STAR/uhnn_star(1l)_tr.txt', 'r') as file:
    star_1l = file.read()
    
with open('../STAR/uhnn_star(1M)_tr.txt', 'r') as file:
    star_1m = file.read()

all_1l = star_1l.split('NNNN')
parts_1l = [list(filter(None, x.split('\n'))) for x in all_1l]

all_1m = star_1m.split('NNNN')
parts_1m = [list(filter(None, x.split('\n'))) for x in all_1m]


def fill_prlet(cords, sign, RW):
    for item in cords:
        if item != []:
            str_01 = '        <rec>\n'
            str_02 = f'            <c i="name" v="{item[0].split(" ")[0]}" />\n'
            str_03 = f'            <c i="kurs" v="{RW} UHNN" />\n'
            str_04 = f'            <c i="namei" v="{item[0].split(" ")[0]}{sign} " />\n'
            str_05 = '            <dtable i="points">\n'
            first_part = [str_01, str_02, str_03, str_04, str_05]
            points = []
            for point in item:
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

test = list(fill_prlet(parts_1l, '1L', '11'))
with open('star_1L.xml', 'w') as file:
    for item in test:
        for elem in item:
            file.write(elem)

test = list(fill_prlet(parts_1m, '1M', '29'))
with open('star_1M.xml', 'w') as file:
    for item in test:
        for elem in item:
            file.write(elem)




