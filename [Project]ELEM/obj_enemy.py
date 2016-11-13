from pico2d import *
from vector2D import *
from obj_Bullet import *
from obj_Particle import *
import GameManager
import random
import RES


class Enemy(Actor):
    SpriteID = None
    Size = 0
    point = 0
    Angle = 0
    AngleRate = 0
    Speed = 0
    SpeedRate = 0
    ishold = False
    HIT = 32

    HP = 0

    def __init__(self, spriteid, x, y, angle, anglerate, speed, speedrate, hold=False):
        self.SpriteID = spriteid
        self.point = Vec2D(x, y)
        self.Angle = angle
        self.AngleRate = anglerate
        self.Speed = speed
        self.SpeedRate = speedrate
        self.ishold = hold
    def move(self):
        self.rad = self.Angle * math.pi / 180

        self.point.x += self.Speed * math.cos(self.rad)
        self.point.y += self.Speed * math.sin(self.rad)

        self.Angle += self.AngleRate
        self.Speed += self.SpeedRate

        if self.ishold is True:
            if self.Speed < 0:
                self.Speed = 0


    def isDestroy(self):
        if GameManager.CLIENT_WIDTH < self.point.x - self.Size or self.point.x + self.Size < 0 or GameManager.CLIENT_HEIGHT < self.point.y - self.Size or self.point.y + self.Size < 0:
            return True
        if self.HP < 0:
            return True

########################################################################################################################
class Enemy64(Enemy):
    ST_STAND, ST_SHOOT = 0, 1

    img_rad = 0
    img_frame = 0
    img_tick = 0

    Size = 64

    stand_frame = 0
    shoot_frame = 0
    state = ST_STAND

    HP = 1

    def draw(self):
        RES.res.spr_enemy64.opacify(0.7)
        RES.res.spr_enemy64.clip_rotate_draw(self.img_rad, self.img_frame * 64, self.SpriteID * 64, 64, 64,
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
        self.img_rad = (self.img_rad + 0.1) % 360
        self.img_tick += 1
        if self.img_tick > 10:
            self.img_frame = (self.img_frame + 1) % 8
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

########################################################################################################################
class Enemy_spiral(Enemy64):
    ST_STAND, ST_SHOOT = 0, 1
    HP = 20
    def shoot(self):
        for i in range(4):
            GameManager.e_bullet += [
                # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
                EnemyBullet(1, 1, self.point.x, self.point.y - 18,
                            self.img_rad*5 + 90 * i + self.shoot_frame,
                            0, 4, 0.01)
            ]

    def handle_stand(self):
        self.stand_frame += 1
        if self.stand_frame > 50:
            self.shoot_frame = 0
            self.state = self.ST_SHOOT

    def handle_shoot(self):
        self.shoot_frame += 1
        if self.shoot_frame % 5 == 0:
            self.shoot()
        if self.shoot_frame > 300:
            self.stand_frame = 0
            self.state = self.ST_STAND

    handle_state = {
        ST_STAND: handle_stand,
        ST_SHOOT: handle_shoot
    }

    def update(self):
        self.img_rad = (self.img_rad + 0.1) % 360
        self.img_tick += 1
        if self.img_tick > 10:
            self.img_frame = (self.img_frame + 1) % 8
            self.img_tick = 0

        self.handle_state[self.state](self)
        self.move()

########################################################################################################################
class Enemy_Gorgon(Enemy64):
    ST_STAND, ST_SHOOT = 0, 1
    HP = 3
    def shoot(self):
        for i in range(4):
            GameManager.e_bullet += [
                # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
                EnemyBullet(3, 4, self.point.x, self.point.y - 18,
                            calcangle(self.point.x, self.point.y, GameManager.Player.point.x,
                                      GameManager.Player.point.y)+random.randint(-20,20),
                            0, random.randint(2,5), 0.01)
            ]

    def handle_stand(self):
        self.stand_frame += 1
        if self.stand_frame > 100:
            self.shoot_frame = 0
            self.state = self.ST_SHOOT

    def handle_shoot(self):
        self.shoot_frame += 1
        if self.shoot_frame % 15 == 0:
            self.shoot()
        if self.shoot_frame > 100:
            self.stand_frame = 0
            self.state = self.ST_STAND

    handle_state = {
        ST_STAND: handle_stand,
        ST_SHOOT: handle_shoot
    }

    def update(self):
        self.img_rad = (self.img_rad + 0.1) % 360
        self.img_tick += 1
        if self.img_tick > 10:
            self.img_frame = (self.img_frame + 1) % 8
            self.img_tick = 0

        self.handle_state[self.state](self)
        self.move()
########################################################################################################################
class Enemy_Rounder(Enemy64):
    ST_STAND, ST_SHOOT = 0, 1
    HP = 10
    def shoot(self):
        for i in range(8):
            GameManager.e_bullet += [
                # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
                EnemyBullet(5, 1, self.point.x, self.point.y - 18,
                            self.img_rad * 5 + 45 * i + self.shoot_frame,
                            random.randint(1,2)/100, 6, 0.05)
            ]

    def handle_stand(self):
        self.stand_frame += 1
        if self.stand_frame > 25:
            self.shoot_frame = 0
            self.state = self.ST_SHOOT

    def handle_shoot(self):
        self.shoot_frame += 1
        if self.shoot_frame % 30 == 0:
            self.shoot()
        if self.shoot_frame > 300:
            self.stand_frame = 0
            self.state = self.ST_STAND

    handle_state = {
        ST_STAND: handle_stand,
        ST_SHOOT: handle_shoot
    }

    def update(self):
        self.img_rad = (self.img_rad + 0.1) % 360
        self.img_tick += 1
        if self.img_tick > 10:
            self.img_frame = (self.img_frame + 1) % 8
            self.img_tick = 0

        self.handle_state[self.state](self)
        self.move()
class Enemy_shotgun(Enemy):
    pass
########################################################################################################################



class Enemy_fairy(Enemy):
    ST_STAND, ST_SHOOT = 0, 1

    img_rad = 0
    img_frame = 0
    img_tick = 0

    Size = 64

    stand_frame = 0
    shoot_frame = 0
    state = ST_STAND
    HIT = 64
    HP = 750

    def draw(self):
        RES.res.spr_fairy.opacify(0.7)
        RES.res.spr_fairy.clip_rotate_draw(self.img_rad, self.img_frame * 128, 128*3, 128, 128,
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
        if self.shoot_frame % 2 == 0:
            self.shoot()
        if self.shoot_frame > 100:
            self.stand_frame = 0
            self.state = self.ST_STAND
        pass

    handle_state = {
        ST_STAND: handle_stand,
        ST_SHOOT: handle_shoot
    }

    def update(self):
        self.img_tick += 1
        if self.img_tick > 1:
            self.img_frame = (self.img_frame + 1) % 32
            self.img_tick = 0

        self.handle_state[self.state](self)
        self.move()
        pass

    def shoot(self):
        GameManager.e_bullet += [
            # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
            EneBulletReAngler(3, 2, self.point.x, self.point.y - 18,
                        random.randint(0,359),
                        0, 3, -0.3),
            EneBulletReAngler(3, 3, self.point.x, self.point.y - 18,
                              calcangle(self.point.x, self.point.y, GameManager.Player.point.x,
                                        GameManager.Player.point.y),
                              random.randint(-1,1), 5, -0.2)
        ]
