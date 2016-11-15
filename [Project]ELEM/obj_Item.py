from pico2d import *
from vector2D import *
import GameManager
import RES

class Item(Actor):
    ITEM_POWER, ITEM_BOMB, ITEM_LIVE = 0,1,2
    HIT = 32
    HP = 1
    iscollisioned = False

    def __init__(self,x,y, itemcode, angle, anglerate, speed, speedrate, size=int(64)):
        self.point = Vec2D(x, y)

        self.itemtype = itemcode

        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate
        self.Size = size

        self.Just_Created = True

    def update(self):
        self.rad = self.Angle * math.pi / 180

        self.point.x += self.Speed * math.cos(self.rad)
        self.point.y += self.Speed * math.sin(self.rad)

        self.Angle += self.AngleRate
        self.Speed += self.SpeedRate

        if self.Just_Created is True and self.Speed < 0:
            self.Just_Created = False
            self.SpeedRate = 0.05
            self.Angle = 180



    def draw(self):
        RES.res.spr_item.opacify(0.9)
        RES.res.spr_item.clip_draw(64*self.itemtype, 0, 64, 64, self.point.x, self.point.y, self.Size,
                                                   self.Size)
        drawhitbox(self.point, self.HIT)

    def isDestroy(self):
        if GameManager.CLIENT_WIDTH < self.point.x - self.Size or self.point.x + self.Size < 0 or GameManager.CLIENT_HEIGHT < self.point.y - self.Size or self.point.y + self.Size < 0:
            return True
        if self.iscollisioned is True:
            return True
        if self.HP < 0:
            return True

    def KIA(self):
        if self.itemtype == self.ITEM_POWER:
            GameManager.Player_Power = min(500,GameManager.Player_Power + 10)
        elif self.itemtype == self.ITEM_BOMB:
            GameManager.curr_bomb += 1
        elif self.itemtype == self.ITEM_LIVE:
            GameManager.live += 1
