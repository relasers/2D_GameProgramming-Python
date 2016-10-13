from vector2D import *
from pico2d import *
import RES
import GameManager
import math


class Bullet:
    SpriteID = None
    Size = 0
    Angle = 0
    AngleRate = 0
    Speed = 0
    SpeedRate = 0
    rad = 0

    def __init__(self, spriteid, x, y, angle, anglerate, speed, speedrate):
        self.SpriteID = spriteid
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate

    def update(self):
        self.rad = self.Angle * math.pi / 180

        self.point.x += self.Speed * math.cos(self.rad)
        self.point.y += self.Speed * math.sin(self.rad)

        self.Angle += self.AngleRate
        self.Speed += self.SpeedRate

    # Check Bullet Out of Client
    def isout(self):
        if GameManager.CLIENT_WIDTH < self.point.x - self.Size or self.point.x + self.Size < 0 or GameManager.CLIENT_HEIGHT < self.point.y - self.Size or self.point.y + self.Size < 0:
            return True


class PlayerBullet(Bullet):
    def __init__(self, spriteid, x, y, angle, anglerate, speed, speedrate):
        self.SpriteID = spriteid
        self.Size = 32
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate

    def draw(self):
        RES.res.spr_player_bullet.opacify(0.5)
        if self.SpriteID == 0:
            RES.res.spr_player_bullet.clip_rotate_draw(self.rad, 0, 32, 32, 16, self.point.x, self.point.y)
        elif self.SpriteID == 1:
            RES.res.spr_player_bullet.clip_rotate_draw(self.rad, 0, 48, 32, 16, self.point.x, self.point.y)


class PlayerBulletChaser(PlayerBullet):
    def __init__(self, spriteid, x, y, angle, anglerate, speed, speedrate):
        self.SpriteID = spriteid
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate

    def draw(self):
        RES.res.spr_player_bullet.opacify(0.5)
        RES.res.spr_player_bullet.clip_rotate_draw(self.rad, 0, 0, 32, 32, self.point.x, self.point.y)

    def update(self):
        if len(GameManager.enemy) is 0:
            self.rad = self.Angle * math.pi / 180

            self.point.x += self.Speed * math.cos(self.rad)
            self.point.y += self.Speed * math.sin(self.rad)

            self.Angle += self.AngleRate
            self.Speed += self.SpeedRate
        else:
            self.target = Vec2D(0, 0)
            self.target += self.point
            self.target -= GameManager.enemy[0].point
            self.target._normalize()
            self.point += self.target * self.Speed
