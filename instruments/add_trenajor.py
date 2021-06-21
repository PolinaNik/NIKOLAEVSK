def create_trenajor_file(filename, dict_with_points):
    with open(f'{filename}_tr.txt', 'w') as file:
        for key in dict_with_points.keys():
            for values in dict_with_points[key]:
                for name in values.keys():
                    file.write(f'{name}    {values[name]}'+'\n')
            file.write('\n\n')