from vector2D import *
from pico2d import *
import RES
import GameManager
import math


class Bullet(Actor):
    SpriteID = None
    SpriteColor = None
    Size = 0
    Angle = 0
    AngleRate = 0
    Speed = 0
    SpeedRate = 0
    rad = 0

    iscollisioned = False
    HIT = 4

    def __init__(self, spriteid, spritecolor, x, y, angle, anglerate, speed, speedrate, size = int(32)):
        self.SpriteID = spriteid
        self.SpriteColor = spritecolor
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate
        self.Size = size
        self.iscollisioned = False

    def update(self):
        self.rad = self.Angle * math.pi / 180

        self.point.x += self.Speed * math.cos(self.rad)
        self.point.y += self.Speed * math.sin(self.rad)

        self.Angle += self.AngleRate
        self.Speed += self.SpeedRate

    # Check Bullet Out of Client
    def isDestroy(self):
        if GameManager.CLIENT_WIDTH < self.point.x - self.Size or self.point.x + self.Size < 0 or GameManager.CLIENT_HEIGHT < self.point.y - self.Size or self.point.y + self.Size < 0:
            return True
        if self.iscollisioned is True:
            return True


###########################<Player's Bullet>###########################################################################
class PlayerBullet(Bullet):
    Damage = 1

    def draw(self):
        RES.res.spr_player_bullet.opacify(0.7)
        if self.SpriteColor == 0:
            RES.res.spr_player_bullet.clip_rotate_draw(self.rad, 0, 32, 32, 16, self.point.x, self.point.y,self.Size,self.Size)
        elif self.SpriteColor == 1:
            RES.res.spr_player_bullet.clip_rotate_draw(self.rad, 0, 48, 32, 16, self.point.x, self.point.y,self.Size,self.Size)
        drawhitbox(self.point, self.HIT)


class PlayerBulletChaser(PlayerBullet):
    Damage = 2

    def __init__(self, spriteid, spritecolor, x, y, angle, anglerate, speed, speedrate, size=int(32)):
        self.SpriteID = spriteid
        self.SpriteColor = spritecolor
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate
        self.Size = size

    def draw(self):
        RES.res.spr_player_bullet.opacify(0.7)
        RES.res.spr_player_bullet.clip_rotate_draw(self.rad, 0, 0, 32, 32, self.point.x, self.point.y,self.Size,self.Size)
        drawhitbox(self.point, self.HIT)

########################################################################################################################
class PlayerBomb(PlayerBullet):
    pass

class EnemyBullet(Bullet):
    def draw(self):
        RES.res.spr_bullet32.clip_rotate_draw(self.rad, self.SpriteColor*32, self.SpriteID*32, 32, 32, self.point.x, self.point.y,self.Size,self.Size)
        drawhitbox(self.point, self.HIT)

