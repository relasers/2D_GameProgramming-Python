from vector2D import *
from pico2d import *
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
        self.rad = self.Angle*math.pi/180

        self.point.x += self.Speed * math.cos(self.rad)
        self.point.y += self.Speed * math.sin(self.rad)

        self.Angle += self.AngleRate
        self.Speed += self.SpeedRate


class PlayerBullet(Bullet):
    image = None

    def __init__(self, spriteid, x, y, angle, anglerate, speed, speedrate):
        self.SpriteID = spriteid
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate

        if PlayerBullet.image == None:
            PlayerBullet.image = load_image('Resources/Images/Bullets/RBullet.png')

    def draw(self):
        self.image.clip_rotate_draw(self.rad, 0, 32, 32, 16, self.point.x, self.point.y)
