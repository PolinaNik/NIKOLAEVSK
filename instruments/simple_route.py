from instruments.destination_point import destination_point
from instruments.distance import distance
from instruments.change_angle import change_angle
from instruments.intersection_point import intersection_point
from instruments.create_arc import create_arc
from instruments import converter as convert
from instruments.bearing import bearing
from config import step


class SimpleRoute:

    def __init__(self, **params):
        self.param_dict = {item: name for item, name in params.items()}

    def first_turn(self):
        end_point = self.param_dict["end_point"]
        kink = self.param_dict["kink"]
        begin_arc = self.param_dict["begin_arc"]
        turn = self.param_dict["turn"]
        start_bearing = change_angle(self.param_dict["start_bearing"] - 13)
        turn_bearing = int(change_angle(bearing(end_point, kink)))
        intersection = intersection_point(begin_arc, kink, start_bearing,
                                          turn_bearing)
        radius = distance(begin_arc, intersection)
        end_arc = destination_point(intersection, change_angle(turn_bearing + 180), radius)
        if turn == 'LEFT':
            center = intersection_point(end_arc, begin_arc, change_angle(turn_bearing + 90),
                                        change_angle(start_bearing - 90))
            kink_radius = distance(center, end_arc)

            arc = create_arc(change_angle(turn_bearing - 90), change_angle(start_bearing + 90), step, center,
                             kink_radius)
            arc.reverse()
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            return arc_points
        else:
            center = intersection_point(end_arc, begin_arc, change_angle(turn_bearing - 90),
                                        change_angle(start_bearing + 90))

            kink_radius = distance(center, end_arc)
            arc = create_arc(change_angle(start_bearing - 90), change_angle(turn_bearing + 90), step, center,
                             kink_radius)
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            return arc_points
