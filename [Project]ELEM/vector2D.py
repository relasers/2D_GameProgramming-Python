# for Calculate Vector
import math
EFFECT_EFFER = 0.0001


class Vec2D:
    _m_x = 0
    _m_y = 0

    def __init__(self, point_x, point_y):
        self._m_x = point_x
        self._m_x = point_y

    def __add__(self, other):
        return self._m_x + other.x, self._m_y + other.y
    __radd__ = __add__

    def __sub__(self, other):
        return self._m_x - other.x, self._m_y - other.y
    __rsub__ = __sub__

    def __mul__(self, other):
        return self._m_x * other, self._m_y * other
    __rmul__ = __mul__

    def __eq__(self, other):
        return (math.fabs(self._m_x - other.x) < EFFECT_EFFER) and (math.fabs(self._m_y - other.y) < EFFECT_EFFER)

    def _normalize(self):
        flength = self._length()
        if flength != 0:
            self._m_x /= flength
            self._m_y /= flength

    def _length(self):
        return math.sqrt(self._m_x * self._m_x + self._m_y * self._m_y)
