# for Calculate Vector
import math
EffectEffer = 0.0001


class Vec2D:
    x = 0
    y = 0

    def __init__(self, point_x, point_y):
        self.x = point_x
        self.y = point_y

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
        return (math.fabs(self.x - other.x) < EffectEffer) and (math.fabs(self.y - other.y) < EffectEffer)

    def normalize(self):
        flength = self.length()
        if flength != 0:
            self.x /= flength
            self.y /= flength

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
