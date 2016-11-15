from vector2D import *
from pico2d import *
import RES
import GameManager
import math
import random

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
    HP = 1

    def __init__(self, spriteid, spritecolor, x, y, angle, anglerate, speed, speedrate, size=int(32)):
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
        if self.HP < 0:
            return True


###########################<Player's Bullet>###########################################################################
class PlayerBullet(Bullet):
    Damage = 1

    def draw(self):
        RES.res.spr_player_bullet.opacify(0.7)
        if self.SpriteColor == 0:
            RES.res.spr_player_bullet.clip_rotate_draw(self.rad, 0, 32, 32, 16, self.point.x, self.point.y, self.Size,
                                                       self.Size)
        elif self.SpriteColor == 1:
            RES.res.spr_player_bullet.clip_rotate_draw(self.rad, 0, 48, 32, 16, self.point.x, self.point.y, self.Size,
                                                       self.Size)
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
        RES.res.spr_player_bullet.clip_rotate_draw(self.rad, 0, 0, 32, 32, self.point.x, self.point.y, self.Size,
                                                   self.Size)
        drawhitbox(self.point, self.HIT)


########################################################################################################################
class PlayerBomb(PlayerBullet):
    opacify = 1
    Damage = 10
    HIT = 128
    Size = 256
    def update(self):
        self.rad = self.Angle * math.pi / 180

        self.point.x = GameManager.Player.point.x
        self.point.y = GameManager.Player.point.y

        self.Angle += self.AngleRate
        self.Speed += self.SpeedRate
        self.HIT += 50
        self.Size += 100
        self.iscollisioned = False
        self.opacify -= 0.05
    def isDestroy(self):
        if self.opacify < 0:
            return True

    def draw(self):
        RES.res.spr_ring.opacify(self.opacify)
        RES.res.spr_ring.clip_rotate_draw(self.rad, 0, 0, 256, 256, self.point.x, self.point.y, self.Size,
                                                   self.Size)
        drawhitbox(self.point, self.HIT)


class EnemyBullet(Bullet):
    ST_MOVE, ST_STOP = 0, 1
    state = ST_MOVE
    Movetimer = 0
    Stoptimer = 0
    Rater = False

    def draw(self):
        RES.res.spr_bullet32.clip_rotate_draw(self.rad, self.SpriteColor * 32, self.SpriteID * 32, 32, 32, self.point.x,
                                              self.point.y, self.Size, self.Size)
        drawhitbox(self.point, self.HIT)


class EneBulletReAngler(EnemyBullet):
    RememberSpd = 0
    Counter = 0

    def __init__(self, spriteid, spritecolor, x, y, angle, anglerate, speed, speedrate, size=int(32)):
        self.SpriteID = spriteid
        self.SpriteColor = spritecolor
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.RememberSpd = speed
        self.SpeedRate = speedrate
        self.Size = size
        self.iscollisioned = False
        self.Counter = random.randint(3,5)
    def update(self):
        self.rad = self.Angle * math.pi / 180

        self.point.x += self.Speed * math.cos(self.rad)
        self.point.y += self.Speed * math.sin(self.rad)

        if self.Counter > 0:
            self.Speed += self.SpeedRate
            self.Angle += self.AngleRate


        if self.Speed < 0:
            self.Speed = self.RememberSpd
            self.Angle = random.randint(0,359)
            dice = [1, 2]
            random.shuffle(dice)
            if dice[0] == 1:
                self.Angle = calcangle(self.point.x, self.point.y, GameManager.Player.point.x,
                                       GameManager.Player.point.y)+random.randint(-10,10)
            self.Counter -= 1

class EneBulletAngleCleaner(EnemyBullet):
    RememberSpd = 0
    Counter = 0

    def __init__(self, spriteid, spritecolor, x, y, angle, anglerate, speed, speedrate, size=int(32)):
        self.SpriteID = spriteid
        self.SpriteColor = spritecolor
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.RememberSpd = speed
        self.SpeedRate = speedrate
        self.Size = size
        self.iscollisioned = False
    def update(self):
        self.rad = self.Angle * math.pi / 180

        self.point.x += self.Speed * math.cos(self.rad)
        self.point.y += self.Speed * math.sin(self.rad)

        if self.Counter < 100:
            self.Speed += self.SpeedRate
            self.Angle += self.AngleRate


        if self.Counter == 100:
            self.Angle = random.randint(0,360)

        self.Counter += 1



class EneBulletHatcher(EnemyBullet):
    RememberSpd = 0
    Counter = 0
    LIFE = 100
    HIT = 64
    img_Frame = 0
    def __init__(self, spriteid, spritecolor, x, y, angle, anglerate, speed, speedrate, size=int(192)):
        self.SpriteID = spriteid
        self.SpriteColor = spritecolor
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.RememberSpd = speed
        self.SpeedRate = speedrate
        self.Size = size
        self.iscollisioned = False
    def update(self):
        self.rad = self.Angle * math.pi / 180

        self.point.x += self.Speed * math.cos(self.rad)
        self.point.y += self.Speed * math.sin(self.rad)

        if self.LIFE < 0:
            for i in range(16):
                GameManager.e_bullet += [
                    # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
                    EnemyBullet(5, self.SpriteColor, self.point.x, self.point.y - 18,
                                i*22 + random.randint(-5,5),
                                random.randint(1, 2) / 100, 1, 0.01)
                ]
                self.HP = -10

        self.LIFE -= 1
        self.img_Frame = (self.img_Frame + 1) % 4

    def draw(self):
        RES.res.spr_Fire192.clip_rotate_draw(self.rad, self.img_Frame * 192, self.SpriteColor * 192, 192, 192, self.point.x,
                                              self.point.y, self.Size, self.Size)
        drawhitbox(self.point, self.HIT)




