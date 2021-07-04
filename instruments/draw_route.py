from instruments import converter as convert

def draw_route(file_name, route_name, *args):
    draw_list = []
    for arg in args:
        if type(arg) is str:
            draw_list += [arg]
        else:
            draw_list += arg
    three_points = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
    result = three_points(draw_list, 3)
    to_list = [', '.join(item) for item in result]
    with open(f"ROUTES/{file_name}.sld", 'a+') as file:
        file.write(f'L: *{route_name}* ' + to_list[0] + '\n')
        for item in to_list[1:]:
            file.write(', ' + item + '\n')


def draw_route_tr(file_name, route_name, *args):
    draw_list = []
    for arg in args:
        if type(arg) is str:
            draw_list += [arg]
        else:
            lenght = len(arg)
            middle = int(lenght/2)
            draw_list += [arg[0]]
            draw_list += [arg[middle]]
            draw_list += [arg[-1]]
    with open(f"KST_ROUTES/{file_name}.txt", 'a+') as file:
        file.write(f'{route_name}\n')
        for num, item in enumerate(draw_list):
            file.write(f'{route_name}{num}   ' + convert.str_to_tren(item) + '\n')
        file.write('NNNN\n')