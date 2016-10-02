from vector2D import *


class ActiveObj:
    def __init__(self, point_x, point_y):
        self._m_point = Vec2D(point_x, point_y)
        self._m_hit = 3

    def check_hit(self,other):
        dx = self._m_point.x - other._m_point.x
        dy = self._m_point.x - other._m_point.y


