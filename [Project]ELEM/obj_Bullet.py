from vector2D import *
from pico2d import *
import GameManager
import FrameWork
import math


class Bullet:
    SpriteID = None
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
        if FrameWork.CLIENT_WIDTH < self.point.x or self.point.x < 0 or FrameWork.CLIENT_HEIGHT < self.point.y or self.point.y < 0:
            return True


class PlayerBullet(Bullet):
    def __init__(self, spriteid, x, y, angle, anglerate, speed, speedrate):
        self.SpriteID = spriteid
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate

    def draw(self):
        FrameWork.sprite.spr_player_bullet.opacify(0.5)
        FrameWork.sprite.spr_player_bullet.clip_rotate_draw(self.rad, 0, 32, 32, 16, self.point.x, self.point.y)


class PlayerBulletChaser(PlayerBullet):
    def __init__(self, spriteid, x, y, angle, anglerate, speed, speedrate):
        self.SpriteID = spriteid
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate

    def draw(self):
        FrameWork.sprite.spr_player_bullet.opacify(0.5)
        FrameWork.sprite.spr_player_bullet.clip_rotate_draw(self.rad, 0, 0, 32, 32, self.point.x, self.point.y)

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
            self.point += self.target * self.speed
