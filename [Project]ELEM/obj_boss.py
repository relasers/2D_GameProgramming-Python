from pico2d import *
from vector2D import *
from obj_Bullet import *
import RES
import math
########################################################################################################################
class Boss(Actor):
    Size = 0
    point = 0
    Angle = 0
    AngleRate = 0
    Speed = 0
    SpeedRate = 0
    ishold = False
    HIT = 128

    HP = 5000


    def __init__(self, x, y, angle, anglerate, speed, speedrate):
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate


    def move(self):
        self.rad = self.Angle * math.pi / 180

        self.point.x += self.Speed * math.cos(self.rad)
        self.point.y += self.Speed * math.sin(self.rad)

        self.Angle += self.AngleRate
        self.Speed += self.SpeedRate

        if self.Speed < 0:
            self.Speed = 0


    def isDestroy(self):
        if self.HP < 0:
            return True


def KIA(self):
    pass


class Plask(Boss):
    ST_STAND, ST_SHOOT = 0, 1

    img_rad = 0
    img_frame = 0
    img_tick = 0

    Size = 64

    stand_frame = 0
    shoot_frame = 0
    state = ST_STAND

    HP = 5000

    def draw(self):
        RES.res.spr_boss1.opacify(1.0)
        if self.HP < 2500:
            RES.res.spr_boss1.clip_rotate_draw(270+math.sin(self.img_rad*math.pi/180.0), self.img_frame*256, 256, 256, 256,
                                             self.point.x, self.point.y)
        else:
            RES.res.spr_boss1.clip_rotate_draw(270+math.sin(self.img_rad*math.pi/180.0)*5, self.img_frame * 256, 0, 256, 256,
                                                 self.point.x, self.point.y)

        drawhitbox(self.point, self.HIT)

    def handle_stand(self):
        self.stand_frame += 1
        if self.stand_frame > 40:
            self.shoot_frame = 0
            self.state = self.ST_SHOOT
        pass

    def handle_shoot(self):
        self.shoot_frame += 1
        if self.shoot_frame % 10 == 0:
            self.shoot()
        if self.shoot_frame > 10:
            self.stand_frame = 0
            self.state = self.ST_STAND
        pass

    handle_state = {
        ST_STAND: handle_stand,
        ST_SHOOT: handle_shoot
    }

    def update(self):
        self.img_rad = (self.img_rad + 1) % 360
        self.img_tick += 1
        if self.img_tick > 10:
            self.img_frame = (self.img_frame + 1) % 6
            self.img_tick = 0

        self.handle_state[self.state](self)
        self.move()
        pass

    def shoot(self):
        GameManager.e_bullet += [
            # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
            EnemyBullet(3, 0, self.point.x, self.point.y - 18,
                        calcangle(self.point.x, self.point.y, GameManager.Player.point.x, GameManager.Player.point.y),
                        0, 3, 0.01)
        ]


class Nikola(Boss):
    pass

