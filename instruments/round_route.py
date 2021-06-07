from instruments.destination_point import destination_point
from instruments.intersection_point import intersection_point
from instruments.distance import distance
from instruments.bearing import bearing
from instruments.change_angle import change_angle
from instruments.create_arc import create_arc
from instruments import converter as convert
from config import step, round_step

class RoundRoute:

    def __init__(self, **params):
        self.param_dict = {item: name for item, name in params.items()}

    def first_turn(self):
        start_bearing = change_angle(self.param_dict["start_bearing"] - 13)
        glob_center = self.param_dict["glob_center"]
        glob_rad = self.param_dict["glob_rad"]
        turn1 = self.param_dict["turn1"]
        if turn1 == 'LEFT':
            arc = create_arc(change_angle(start_bearing - 170), change_angle(start_bearing + 90), round_step, glob_center,
                             glob_rad)
            arc.reverse()
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            return arc_points
        else:
            arc = create_arc(change_angle(start_bearing - 90), change_angle(start_bearing + 170), round_step, glob_center,
                             glob_rad)
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            return arc_points

    def glob_round(self):
        start_bearing = change_angle(self.param_dict['start_bearing'] - 13)
        glob_center = self.param_dict['glob_center2']
        glob_rad = self.param_dict['glob_rad2']
        turn1 = self.param_dict['turn1']
        if turn1 == 'LEFT':
            glob_arc = create_arc(start_bearing, change_angle(start_bearing+140), step, glob_center, glob_rad)
            glob_arc_points = [convert.to_gr(glob_arc[num]) for num, item in enumerate(glob_arc)]
        else:
            glob_arc = create_arc(350, start_bearing, step, glob_center, glob_rad)
            glob_arc.reverse()
            glob_arc_points = [convert.to_gr(glob_arc[num]) for num, item in enumerate(glob_arc)]
        return glob_arc_points

    def second_turn(self):
        get_last_cords = self.glob_round()
        last_cord1 = convert.slds_to_gr(get_last_cords[-1])
        last_cord2 = convert.slds_to_gr(get_last_cords[-2])
        turn_bearing = int(change_angle(bearing(last_cord2, last_cord1)))
        end_point = self.param_dict['end_point']
        end_bearing = change_angle(self.param_dict['end_bearing']-13)
        turn2 = self.param_dict['turn2']
        intersection = intersection_point(end_point, last_cord1, change_angle(end_bearing-180), turn_bearing)
        big_rad = distance(intersection, last_cord1)
        end_arc = destination_point(intersection, end_bearing, big_rad)
        if turn2 == 'LEFT':
            center = intersection_point(end_arc, last_cord1, change_angle(end_bearing+90), change_angle(turn_bearing+90))
            rad = distance(center, end_arc)
            arc = create_arc(change_angle(turn_bearing-90), change_angle(end_bearing-90), step, center, rad)
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
        else:
            center = intersection_point(end_arc, last_cord1, change_angle(end_bearing-90), change_angle(turn_bearing-90))
            rad = distance(end_arc, center)
            arc = create_arc(change_angle(end_bearing+90), change_angle(turn_bearing+90), step, center, rad)
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            arc_points.reverse()
        return arc_points

