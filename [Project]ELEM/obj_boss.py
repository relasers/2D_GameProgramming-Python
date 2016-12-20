from pico2d import *
from vector2D import *
from obj_Bullet import *
from obj_Particle import *
from obj_enemy import *

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

    Pattern = 0

    HP = 7000


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
        for i in range(48):
            GameManager.particle += [
            MagicBlast(self.point.x, self.point.y , True)]

        GameManager.GameClear = True
        GameManager.background.state += 1
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

    MAXHP = 5000
    HP = MAXHP

    shoot_rad = 0
    shoot_counter = 0

    def draw(self):
        RES.res.spr_boss1.opacify(1.0)
        if self.HP < 2500 :
            RES.res.spr_boss1.clip_rotate_draw(270+math.sin(self.img_rad*math.pi/180.0)*2, self.img_frame*256, 256, 256, 256,
                                             self.point.x, self.point.y)
        else:
            RES.res.spr_boss1.clip_rotate_draw(270+math.sin(self.img_rad*math.pi/180.0), self.img_frame * 256, 0, 256, 256,
                                                 self.point.x, self.point.y)
        RES.res.font_elem.draw(self.point.x, self.point.y+128, " %d " % self.HP, (255-(int)(self.HP*0.051), (int)(self.HP*0.051) , 0))
        drawhitbox(self.point, self.HIT)

    def handle_stand(self):
        self.stand_frame += 1
        if self.stand_frame > 50:
            self.shoot_frame = 0
            self.Pattern = random.randint(0,4)
            self.state = self.ST_SHOOT
            GameManager.enemy += [
                Enemy_carrier(0, GameManager.CLIENT_WIDTH, random.randint(0, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE),
                        180, random.randint(-1,1), 4, 0),
            ]

        pass

    def handle_shoot(self):
        if self.Pattern == 0:
            self.Pattern_1()
        elif self.Pattern == 1:
            self.Pattern_2()
        elif self.Pattern == 2:
            self.Pattern_3()
        elif self.Pattern == 3:
            self.Pattern_4()
        elif self.Pattern == 4:
            self.Pattern_5()

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

    def shoot_Linear(self,hardmode):

        color = 3
        if hardmode is True:
            color = 0

        for i in range(4):
            GameManager.e_bullet += [
                EnemyBullet(3, color, self.point.x, self.point.y - 18,
                        calcangle(self.point.x, self.point.y, GameManager.Player.point.x, GameManager.Player.point.y),
                        0, -5+i, 0.05)
                        ]

    def shoot_Rounder(self,counter,hardmode):
        color = 3
        if hardmode is True:
            color = 0
        for i in range(45):
            GameManager.e_bullet += [
                EnemyBullet(3, color, self.point.x, self.point.y - 18,
                        i*8+counter*2 ,
                        0, 5, 0.05)
                        ]

    def shoot_Hatcher(self,hardmode):
        color = 3
        counter = 4
        if hardmode is True:
            counter*= 2
            color = 0
        for i in range(counter):
            GameManager.e_bullet += [
                EneBulletHatcher(0, color, self.point.x, self.point.y - 18,
                        90+i*10 ,
                        2, i+1, -0.05, 128)
                        ]
        for i in range(counter):
            GameManager.e_bullet += [
                EneBulletHatcher(0, color, self.point.x, self.point.y - 18,
                        270-i*10 ,
                        -2, i+1, -0.05, 128)
                        ]

    def shoot_ToxicRain(self,hardmode):
        color = 3
        if hardmode is True:
            color = 0
        for i in range(3):
            GameManager.e_bullet += [
            EnemyBullet(1, color, self.point.x, self.point.y - 18,
                        90+random.randint(0,180),
                        random.randint(-1,1), random.randint(5,7), 0.01)
        ]

    def shoot_Hurrycane(self,hardmode):
        color = 3
        if hardmode is True:
            color = 0
        for i in range(8):
            GameManager.e_bullet += [
                EneBulletAngleCleaner(4, color, self.point.x, self.point.y - 18,
                        i * 8,
                        3, 3, 0.01)
        ]

    def Pattern_1(self):
        if 2500 < self.HP:

            self.shoot_frame += 1
            if self.shoot_frame % 10 == 0:
                self.shoot_Linear(False)
            if self.shoot_frame > 200:
                self.stand_frame = 0
                self.state = self.ST_STAND
        else:

            self.shoot_frame += 1
            if self.shoot_frame % 4 == 0:
                self.shoot_Linear(True)
            if self.shoot_frame > 200:
                self.stand_frame = 0
                self.state = self.ST_STAND

            pass
    def Pattern_2(self):

        if 2500 < self.HP:
            self.shoot_frame += 1
            if self.shoot_frame % 20 == 0:
                self.shoot_Rounder(self.shoot_counter,False)
                self.shoot_counter = (self.shoot_counter+1)%3
            if self.shoot_frame > 200:
                self.stand_frame = 0
                self.state = self.ST_STAND
        else:

            self.shoot_frame += 1
            if self.shoot_frame % 10 == 0:
                self.shoot_Rounder(self.shoot_counter,True)
                self.shoot_counter = (self.shoot_counter + 1) % 3
            if self.shoot_frame > 200:
                self.stand_frame = 0
                self.state = self.ST_STAND


    def Pattern_3(self):


        if 2500 < self.HP:
            self.shoot_frame += 1
            if self.shoot_frame % 100 == 0:
                self.shoot_Hatcher(False)
                self.shoot_counter = (self.shoot_counter+1)%3
            if self.shoot_frame > 101:
                self.stand_frame = 0
                self.state = self.ST_STAND
        else:

            self.shoot_frame += 1
            if self.shoot_frame % 100 == 0:
                self.shoot_Hatcher(True)
                self.shoot_counter = (self.shoot_counter + 1) % 3
            if self.shoot_frame > 101:
                self.stand_frame = 0
                self.state = self.ST_STAND

    def Pattern_4(self):

        if 2500 < self.HP:
            self.shoot_frame += 1
            if self.shoot_frame % 2 == 0:
                self.shoot_ToxicRain(False)
            if self.shoot_frame > 200:
                self.stand_frame = 0
                self.state = self.ST_STAND
        else:

            self.shoot_frame += 1
            if self.shoot_frame % 1 == 0:
                self.shoot_ToxicRain(True)
            if self.shoot_frame > 200:
                self.stand_frame = 0
                self.state = self.ST_STAND

    def Pattern_5(self):

        if 2500 < self.HP:
            self.shoot_frame += 1
            if self.shoot_frame % 8 == 0:
                self.shoot_Hurrycane(False)
            if self.shoot_frame > 200:
                self.stand_frame = 0
                self.state = self.ST_STAND
        else:

            self.shoot_frame += 1
            if self.shoot_frame % 5 == 0:
                self.shoot_Hurrycane(True)
            if self.shoot_frame > 200:
                self.stand_frame = 0
                self.state = self.ST_STAND


class Nikola(Boss):
    pass

