# for Calculate Vector
from pico2d import *
import math
import GameManager
EFFECT_EFFER = 0.0001


def calcangle(cx, cy, tx, ty):
    #  center point ~ target point
    return math.atan2(ty - cy, tx - cx) / math.pi*180.0


def drawhitbox(point, hit):
    if GameManager.CollisionBox is True:
        draw_rectangle(point.x - hit, point.y - hit, point.x + hit,point.y + hit)

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
        return (math.fabs(self.x - other.x) < EFFECT_EFFER) and (math.fabs(self.y - other.y) < EFFECT_EFFER)

    def add(self,other):
        self.x += other.x
        self.y += other.y
    def sub(self,other):
        self.x -= other.x
        self.y -= other.y
    def mul(self,other):
        self.x *= other
        self.y *= other
    def normalize(self):
        flength = self.length()
        if flength != 0:
            self.x /= flength
            self.y /= flength

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


class Actor:
    point = Vec2D(0,0)
    Size = 0
    HIT = 0

    def isHit(self, other):
        dx = other.point.x - self.point.x
        dy = other.point.y - self.point.y
        hit = other.HIT + self.HIT

        if dx*dx+dy*dy < hit*hit:
            return True

    def isDestroy(self):
        if GameManager.CLIENT_WIDTH < self.point.x - self.Size*2 or self.point.x + self.Size*2 < 0 or GameManager.CLIENT_HEIGHT < self.point.y - self.Size*2 or self.point.y + self.Size*2 < 0:
            return True


