from vector2D import *


class ActiveObj:
    def __init__(self, point_x, point_y):
        self.point = Vec2D(point_x, point_y)
        self.hit = 3

    def check_hit(self,other):
        dx = self.point.x - other.point.x
        dy = self.point.x - other.point.y


