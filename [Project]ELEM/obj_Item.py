from pico2d import *
from vector2D import *
import GameManager
import RES

class Item(Actor):
    ITEM_POWER, ITEM_BOMB, ITEM_LIVE = 0,1,2
    HIT = 32
    def __init__(self,x,y, itemcode, angle, anglerate, speed, speedrate, size=int(32)):
        self.point = Vec2D(x, y)

        self.itemtype = itemcode

        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate
        self.Size = size

    def update(self):
        self.rad = self.Angle * math.pi / 180

        self.point.x += self.Speed * math.cos(self.rad)
        self.point.y += self.Speed * math.sin(self.rad)

        self.Angle += self.AngleRate
        self.Speed += self.SpeedRate



    def draw(self):
        RES.res.spr_item.opacify(0.7)
        RES.res.spr_item.clip_draw(0, 0, 64, 64, self.point.x, self.point.y, self.Size,
                                                   self.Size)
        drawhitbox(self.point, self.HIT)
