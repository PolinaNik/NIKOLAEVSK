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
    with open(f"{file_name}.sld", 'a+') as file:
        file.write(f'L: *{route_name}* ' + to_list[0] + '\n')
        for item in to_list[1:]:
            file.write(', ' + item + '\n')
