from instruments.destination_point import destination_point
from instruments.intersection_point import intersection_point
from instruments.distance import distance
from instruments.bearing import bearing
from instruments.change_angle import change_angle
from instruments.create_arc import create_arc
from instruments import converter as convert
from config import step, round_step

class HeartRoute:

    def __init__(self, **params):
        self.param_dict = {item: name for item, name in params.items()}


    def first_round(self):
        begin_arc = self.param_dict["begin_arc"]
        round_kink = self.param_dict["round_kink"]
        start_bearing = change_angle(self.param_dict["start_bearing"]-13)
        round_bearing = change_angle(self.param_dict["round_bearing"]-13)
        intersection = intersection_point(begin_arc, round_kink, start_bearing,
                                                    change_angle(round_bearing + 180))
        radius = distance(begin_arc, intersection)
        end_arc = destination_point(intersection, round_bearing, radius)
        turn1 = self.param_dict["turn1"]
        if turn1 == 'LEFT':
            center = intersection_point(end_arc, begin_arc, change_angle(round_bearing - 90),
                                                  change_angle(start_bearing - 90))
            kink_radius = distance(center, end_arc)
            big_arc = create_arc(165, change_angle(start_bearing + 90), step, center,
                                 kink_radius)
            big_arc.reverse()
            big_arc_points = [convert.to_gr(big_arc[num]) for num, item in enumerate(big_arc)]
            return big_arc_points
        else:
            center = intersection_point(end_arc, begin_arc, change_angle(round_bearing + 90),
                                                  change_angle(start_bearing + 90))
            kink_radius = distance(center, end_arc)
            big_arc = create_arc(change_angle(start_bearing - 90), 40, step, center,
                                 kink_radius)
            big_arc_points = [convert.to_gr(big_arc[num]) for num, item in enumerate(big_arc)]
            return big_arc_points

    def glob_round(self):
        kink = self.param_dict["kink"]
        glob_center = self.param_dict["glob_center"]
        glob_rad = self.param_dict["glob_rad"]
        turn_bearing = int(change_angle(bearing(glob_center, kink)))
        turn2 = self.param_dict["turn2"]
        az_turn = self.param_dict["az_turn"]
        if turn2 == 'LEFT':
            glob_arc = create_arc(change_angle(az_turn + 90), turn_bearing, step, glob_center, glob_rad)
            glob_arc.reverse()
            glob_arc_points = [convert.to_gr(glob_arc[num]) for num, item in enumerate(glob_arc)]
        else:
            glob_arc = create_arc(turn_bearing, change_angle(az_turn - 90), step,
                                  glob_center, glob_rad)
            glob_arc_points = [convert.to_gr(glob_arc[num]) for num, item in enumerate(glob_arc)]
        return glob_arc_points

    def second_turn(self):
        par = self.glob_round()
        cord1 = convert.slds_to_gr(par[-1])
        cord2 = convert.slds_to_gr(par[-2])
        turn_bearing = int(change_angle(bearing(cord2, cord1)))
        end_point = self.param_dict["end_point"]
        end_bearing = change_angle(self.param_dict["end_bearing"] - 13)
        intersection = intersection_point(cord1, end_point, turn_bearing,
                                                    change_angle(end_bearing + 180))
        radius = distance(cord1, intersection)
        end_arc = destination_point(intersection, end_bearing, radius)
        last_turn = self.param_dict["last_turn"]
        if last_turn == 'LEFT':
            center = intersection_point(cord1, end_arc, change_angle(turn_bearing+90), change_angle(end_bearing+90))
            kink_radius = distance(center, end_arc)
            arc = create_arc(change_angle(turn_bearing - 90), change_angle(end_bearing - 90), step, center,
                             kink_radius)
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            return arc_points
        else:
            center = intersection_point(cord1, end_arc, change_angle(turn_bearing - 90),
                                                  change_angle(end_bearing - 90))
            kink_radius = distance(center, end_arc)
            arc = create_arc(change_angle(end_bearing+90), change_angle(turn_bearing+90), step, center,
                             kink_radius)
            arc_points = [convert.to_gr(arc[num]) for num, item in enumerate(arc)]
            arc_points.reverse()
            return arc_points
