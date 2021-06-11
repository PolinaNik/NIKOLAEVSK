from instruments.destination_point import destination_point
from instruments.intersection_point import intersection_point
from instruments.distance import distance
from instruments.change_angle import change_angle
from instruments.create_arc import create_arc
from instruments import converter as convert
from config import step, round_step

class Hippo_left:

    def __init__(self, **params):
        self.param_dict = {item: name for item, name in params.items()}

    def first_turn(self):
        start_bearing = change_angle(self.param_dict["start_bearing"] - 13)
        intersection = self.param_dict["intersection"]
        sector = self.param_dict["sector"]
        small_bearing = change_angle(start_bearing+180-30)
        begin_arc = destination_point(intersection, small_bearing, 7)
        end_arc = destination_point(intersection, start_bearing+180, 7)
        center = intersection_point(begin_arc, end_arc, change_angle(small_bearing+90), (start_bearing+90))
        rad = distance(center, end_arc)
        small_arc = create_arc((small_bearing-90), change_angle(start_bearing-90), step, center, rad)
        arc_points = [convert.to_gr(small_arc[num]) for num, item in enumerate(small_arc)]
        if sector == 1:
            arc_points.reverse()
            return arc_points
        else:
            return arc_points


class Hippo_right:

    def __init__(self, **params):
        self.param_dict = {item: name for item, name in params.items()}

    def first_turn(self):
        start_bearing = change_angle(self.param_dict["start_bearing"] - 13)
        intersection = self.param_dict["intersection"]
        sector = self.param_dict["sector"]
        small_bearing = change_angle(start_bearing-180+30)
        begin_arc = destination_point(intersection, small_bearing, 5.5)
        end_arc = destination_point(intersection, start_bearing-180, 5.5)
        center = intersection_point(begin_arc, end_arc, change_angle(small_bearing-90), (start_bearing-90))
        rad = distance(center, end_arc)
        small_arc = create_arc(change_angle(start_bearing+90), change_angle(small_bearing+90), step, center, rad)
        arc_points = [convert.to_gr(small_arc[num]) for num, item in enumerate(small_arc)]
        if sector == 2:
            arc_points.reverse()
            return arc_points
        else:
            return arc_points



