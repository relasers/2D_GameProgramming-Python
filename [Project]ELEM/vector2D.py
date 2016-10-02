# for Calculate Vector
import math
EFFECT_EFFER = 0.0001


class Vec2D:
    x = 0
    y = 0

    def __init__(self, point_x, point_y):
        self.x = point_x
        self.x = point_y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    __radd__ = __add__

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y
    __rsub__ = __sub__

    def __mul__(self, other):
        return self.x * other, self.y * other
    __rmul__ = __mul__

    def __eq__(self, other):
        return (math.fabs(self.x - other.x) < EFFECT_EFFER) and (math.fabs(self.y - other.y) < EFFECT_EFFER)

    def _normalize(self):
        flength = self._length()
        if flength != 0:
            self.x /= flength
            self.y /= flength

    def _length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
