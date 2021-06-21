from instruments import converter as convert
import inspect
import re


def draw_point(file_name, *cords):
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    args = string[string.find('(') + 1:-1].split(',')
    names = []
    for i in args:
        if i.find('=') != -1:
            names.append(i.split('=')[1].strip())
        else:
            names.append(i)
    names = names[1:]
    pat = re.compile(r'NN.+')
    with open(f"{file_name}.sld", 'a+') as file:
        file.write('L: <BLACK>' + '\n')
    for i, arg in enumerate(cords):
        cord = convert.to_gr(arg)
        res = pat.search(names[i])
        name = res.group()
        with open(f"{file_name}.sld", 'a+') as file:
            file.write(f'S: "2" <R1> {cord}' + '\n')
            file.write(f'T: <R2> {cord} / {name} /' + '\n')
