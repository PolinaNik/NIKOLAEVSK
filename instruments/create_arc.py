from instruments.destination_point import destination_point

def create_arc(start_angle, end_angle, step, center, radius):
    point_list = []
    if start_angle < end_angle:
        for az in range(start_angle, end_angle, step):
            point = destination_point(center, az, radius)
            point_list.append(point)
        return point_list
    else:
        for az in range(start_angle, 360, step):
            point = destination_point(center, az, radius)
            point_list.append(point)
        for az in range(0, end_angle, step):
            point = destination_point(center, az, radius)
            point_list.append(point)
        return point_list

