from instruments.destination_point import destination_point
from instruments.distance import distance
from instruments.change_angle import change_angle
from instruments.intersection_point import intersection_point
from instruments.create_arc import create_arc
from instruments import converter as convert
step = 45


class ParalelRoute:
    def __init__(self, **params):
        self.param_dict = {item: name for item, name in params.items()}

    def first_turn(self):
        start_bearing = change_angle(self.param_dict["start_bearing"] - 13)
        glob_center = self.param_dict["glob_center"]
        glob_rad = self.param_dict["glob_rad"]
        turn1 = self.param_dict["turn1"]
        if turn1 == 'LEFT':
            arc = create_arc(change_angle(start_bearing - 90), change_angle(start_bearing + 90), step, glob_center,
                             glob_rad)
            arc.reverse()
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            return arc_points
        else:
            arc = create_arc(change_angle(start_bearing - 90), change_angle(start_bearing + 90), step, glob_center,
                             glob_rad)
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            return arc_points

    def second_turn(self):
        kink = self.param_dict["kink"]
        end_point = self.param_dict["end_point"]
        kink_bearing = change_angle(self.param_dict["kink_bearing"] - 13)
        end_bearing = change_angle(self.param_dict["end_bearing"] - 13)
        turn2 = self.param_dict["turn2"]
        intersection = intersection_point(kink, end_point, kink_bearing,
                                          change_angle(end_bearing + 180))
        radius = distance(kink, intersection)
        end_arc = destination_point(intersection, end_bearing, radius)
        if turn2 == 'RIGHT':
            center = intersection_point(end_arc, kink, change_angle(end_bearing + 90),
                                        change_angle(kink_bearing + 90))
            kink_radius = distance(center, end_arc)
            arc = create_arc(change_angle(kink_bearing - 90), change_angle(end_bearing - 90), step, center,
                             kink_radius)
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            return arc_points
        else:
            center = intersection_point(end_arc, kink, change_angle(end_bearing - 90),
                                        change_angle(kink_bearing - 90))
            kink_radius = distance(center, end_arc)
            if change_angle(kink_bearing + 90) < change_angle(end_bearing + 90):
                arc1 = create_arc(change_angle(end_bearing + 90), 360, step, center, kink_radius)
                arc2 = create_arc(0, change_angle(kink_bearing + 90), step, center, kink_radius)
                arc = arc1 + arc2
            else:
                arc = create_arc(change_angle(end_bearing + 90), change_angle(kink_bearing + 90), step, center,
                                 kink_radius)
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            arc_points.reverse()
            return arc_points
