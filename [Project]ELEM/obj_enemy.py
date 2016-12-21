from pico2d import *
from vector2D import *
from obj_Bullet import *
from obj_Item import *
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

    def KIA(self):
        GameManager.particle += [
            ExplodeEnemy(0, self.SpriteID, self.point.x, self.point.y, True, self.Size, True, 0, 12, 1)]
        pass

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
class Enemy_carrier(Enemy64):
    ST_STAND, ST_SHOOT = 0, 1
    HP = 15
    HIT = 64
    def shoot(self):
        pass

    def handle_stand(self):
        self.stand_frame += 1
        if self.stand_frame > 50:
            self.shoot_frame = 0
            self.state = self.ST_SHOOT

    def handle_shoot(self):
        self.shoot_frame += 1
        if self.shoot_frame % 10 == 0:
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
            self.img_frame = (self.img_frame + 1) % 6
            self.img_tick = 0

        self.handle_state[self.state](self)
        self.move()
    def draw(self):
        RES.res.spr_carrier.opacify(0.7)
        RES.res.spr_carrier.clip_rotate_draw(0, self.img_frame * 128, self.SpriteID * 128, 128, 128,
                                             self.point.x, self.point.y)
        drawhitbox(self.point, self.HIT)

    def KIA(self):
        for i in range(5):
            GameManager.item += [
            Item(self.point.x, self.point.y,0,random.randint(0,360),0,5,-0.1,32),
        ]

        dice = random.randint(0,10)
        if dice == 0:
                GameManager.item += [
                    Item(self.point.x, self.point.y, 1, random.randint(0, 360), 0, 5, -0.1, 32),
                ]

        GameManager.particle += [
            ExplodeEnemy(0, self.SpriteID, self.point.x, self.point.y, True, self.Size, True, 0, 12, 1)]
########################################################################################################################
class Enemy_spiral(Enemy64):
    ST_STAND, ST_SHOOT = 0, 1
    HP = 15
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
        if self.shoot_frame % 10 == 0:
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

    def KIA(self):
        for i in range(5):
            GameManager.item += [
            Item(self.point.x, self.point.y,0,random.randint(0,360),0,5,-0.1,32),
        ]
        GameManager.particle += [
            ExplodeEnemy(0, self.SpriteID, self.point.x, self.point.y, True, self.Size, True, 0, 12, 1)]
############################################################################################################################
class Enemy_stright_spr(Enemy64):
    ST_STAND, ST_SHOOT = 0, 1
    HP = 15

    def shoot(self):
        for i in range(5):
            GameManager.e_bullet += [
                # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
                EnemyBullet(1, 4, self.point.x, self.point.y - 18,
                            150 + 20*i,
                            0, 8, 0.01)
            ]

    def handle_stand(self):
        self.stand_frame += 1
        if self.stand_frame > 50:
            self.shoot_frame = 0
            self.state = self.ST_SHOOT

    def handle_shoot(self):
        self.shoot_frame += 1
        if self.shoot_frame % 10 == 0:
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

    def KIA(self):
        for i in range(5):
            GameManager.item += [
                Item(self.point.x, self.point.y, 0, random.randint(0, 360), 0, 5, -0.1, 32),
            ]
        GameManager.particle += [
            ExplodeEnemy(0, self.SpriteID, self.point.x, self.point.y, True, self.Size, True, 0, 12, 1)]

############################################################################################################################
class Enemy_stright_aimer(Enemy64):
    ST_STAND, ST_SHOOT = 0, 1
    HP = 15

    def shoot(self):
        for i in range(3):
            GameManager.e_bullet += [
                # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
                EnemyBullet(1, 4, self.point.x, self.point.y - 18,
                            calcangle(self.point.x, self.point.y, GameManager.Player.point.x,
                                      GameManager.Player.point.y) -
                30 + 30 * i,
                            0, 8, 0.01)
            ]

    def handle_stand(self):
        self.stand_frame += 1
        if self.stand_frame > 50:
            self.shoot_frame = 0
            self.state = self.ST_SHOOT

    def handle_shoot(self):
        self.shoot_frame += 1
        if self.shoot_frame % 10 == 0:
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

    def KIA(self):
        for i in range(2):
            GameManager.item += [
                Item(self.point.x, self.point.y, 0, random.randint(0, 360), 0, 5, -0.1, 32),
            ]
        GameManager.particle += [
            ExplodeEnemy(0, self.SpriteID, self.point.x, self.point.y, True, self.Size, True, 0, 12, 1)]

########################################################################################################################
class Enemy_Gorgon(Enemy64):
    ST_STAND, ST_SHOOT = 0, 1
    HP = 2
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
        if self.shoot_frame % 45 == 0:
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
#####################################################################################################################
class Enemy_Linear(Enemy64):
    ST_STAND, ST_SHOOT = 0, 1
    HP = 10
    def shoot(self):
        for i in range(5):
            GameManager.e_bullet += [
                EnemyBullet(2, 2, self.point.x, self.point.y - 18,
                            calcangle(self.point.x, self.point.y, GameManager.Player.point.x,
                                      GameManager.Player.point.y),
                            0, 3 + i, 0.01)
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

###############################################################################################################

class Enemy_shotgun(Enemy64):
    ST_STAND, ST_SHOOT = 0, 1
    HP = 10

    def shoot(self):
        for i in range(6):
            GameManager.e_bullet += [
                EnemyBullet(4, 5, self.point.x, self.point.y - 18,
                            calcangle(self.point.x, self.point.y, GameManager.Player.point.x,
                                      GameManager.Player.point.y)+random.randint(-90,90),
                            0, random.randint(3,7), 0.01)
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

    def KIA(self):
        for i in range(5):
            GameManager.item += [
                Item(self.point.x, self.point.y, 0, random.randint(0, 360), 0, 5, -0.1, 32),
            ]
        GameManager.particle += [
            ExplodeEnemy(0, self.SpriteID, self.point.x, self.point.y, True, self.Size, True, 0, 12, 1)]
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
    HP = 7500

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

        if GameManager.maintime == 5200:
            self.ishold = False
            self.SpeedRate = -0.1
            self.HP = 20

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

    def KIA(self):
        for i in range(10):
            GameManager.item += [
                Item(self.point.x, self.point.y, 0, random.randint(0, 360), 0, 5, -0.1, 32),
            ]
        GameManager.item += [
            Item(self.point.x, self.point.y, 1, random.randint(0, 360), 0, 5, -0.1, 32),
        ]
        GameManager.item += [
            Item(self.point.x, self.point.y, 2, random.randint(0, 360), 0, 5, -0.1, 32),
        ]
        GameManager.particle += [
            ExplodeEnemy(0, self.SpriteID, self.point.x, self.point.y, True, self.Size, True, 0, 12, 1)]

####################################################################################################################################
class Enemy_normlamp(Enemy):
    ST_STAND, ST_SHOOT = 0, 1

    img_rad = 0
    img_frame = 0
    img_tick = 0

    Size = 64

    stand_frame = 0
    shoot_frame = 0
    state = ST_STAND
    HIT = 64
    HP = 7500

    def draw(self):
        RES.res.spr_enemy128.opacify(0.9)
        RES.res.spr_enemy128.clip_rotate_draw(0, self.img_frame * 128, 2 * 128, 128, 128,
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
        if self.shoot_frame % 5 == 0:
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
        self.img_rad = (self.img_rad + 0.1) % 360
        self.img_tick += 1
        if self.img_tick > 10:
            self.img_frame = (self.img_frame + 1) % 6
            self.img_tick = 0

        if GameManager.maintime == 2800:
            self.ishold = False
            self.SpeedRate = -0.1
            self.HP = 20

        self.handle_state[self.state](self)
        self.move()
        pass

    def shoot(self):
        GameManager.e_bullet += [
            # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
            EnemyBullet(3, 5, self.point.x, self.point.y - 18,
                        calcangle(self.point.x, self.point.y, GameManager.Player.point.x, GameManager.Player.point.y) + random.randint(-5,5),
                        0, 8, 0.01)
        ]

        for i in range(6):
            GameManager.e_bullet += [
                # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
                EnemyBullet(5, 4, self.point.x, self.point.y - 18,
                            self.img_rad*5 + 60 * i + self.shoot_frame,
                            0.01, 3, 0.01)
            ]

    def KIA(self):
        for i in range(10):
            GameManager.item += [
                Item(self.point.x, self.point.y, 0, random.randint(0, 360), 0, 5, -0.1, 32),
            ]
        GameManager.item += [
            Item(self.point.x, self.point.y, 1, random.randint(0, 360), 0, 5, -0.1, 32),
        ]
        GameManager.item += [
            Item(self.point.x, self.point.y, 2, random.randint(0, 360), 0, 5, -0.1, 32),
        ]
        GameManager.particle += [
            ExplodeEnemy(0, self.SpriteID, self.point.x, self.point.y, True, self.Size, True, 0, 12, 1)]

####################################################################################################################################
class Enemy_grnlamp(Enemy):
    ST_STAND, ST_SHOOT = 0, 1

    img_rad = 0
    img_frame = 0
    img_tick = 0
    img_opacify = 0.0
    Size = 64

    stand_frame = 0
    shoot_frame = 0
    state = ST_STAND
    HIT = 64
    HP = 7500

    def draw(self):
        RES.res.spr_enemy128.opacify(self.img_opacify)
        RES.res.spr_enemy128.clip_rotate_draw(0, self.img_frame * 128, 4 * 128, 128, 128,
                                             self.point.x, self.point.y)
        RES.res.spr_enemy128.opacify(1-self.img_opacify)
        RES.res.spr_enemy128.clip_rotate_draw(0, self.img_frame * 128, 3 * 128, 128, 128,
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
        if GameManager.maintime < 4700:
            if self.shoot_frame % 20 == 0:
                self.shoot()
        else:
            if self.shoot_frame % 12 == 0:
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
        self.img_rad = (self.img_rad + 1) % 360
        self.img_opacify = 0.5 + math.sin(self.img_rad*math.pi/180.0)*0.5
        self.img_tick += 1
        if self.img_tick > 10:
            self.img_frame = (self.img_frame + 1) % 6
            self.img_tick = 0

        if GameManager.maintime == 5700:
            self.ishold = False
            self.SpeedRate = -0.1
            self.HP = 10

        self.handle_state[self.state](self)
        self.move()
        pass

    def shoot(self):
        dice = [1, 2]
        random.shuffle(dice)
        if dice[0] == 1:
            GameManager.e_bullet += [
            EneBulletAngleCleaner(1, 0, self.point.x, self.point.y - 18,
                        90,
                        0, random.randint(5,7), -random.randint(1,2)/10)
            ]
        else:
            GameManager.e_bullet += [
                EneBulletAngleCleaner(1, 3, self.point.x, self.point.y - 18,
                                      270,
                                      0, random.randint(5, 7), -random.randint(1, 2) / 10)
            ]
        for i in range(6):
            dice = [1, 2]
            random.shuffle(dice)
            if dice[0] == 1:
                GameManager.e_bullet += [
                EneBulletAngleStraighter(2, 0, self.point.x, self.point.y - 18,
                            90,
                            0, random.randint(5,7), -random.randint(1,2)/10)
                ]
            else:
                GameManager.e_bullet += [
                    EneBulletAngleStraighter(2, 3, self.point.x, self.point.y - 18,
                                             270,
                                             0, random.randint(5, 7), -random.randint(1, 2) / 10)
                ]


    def KIA(self):
        for i in range(10):
            GameManager.item += [
                Item(self.point.x, self.point.y, 0, random.randint(0, 360), 0, 5, -0.1, 32),
            ]
        GameManager.item += [
            Item(self.point.x, self.point.y, 1, random.randint(0, 360), 0, 5, -0.1, 32),
        ]
        GameManager.item += [
            Item(self.point.x, self.point.y, 2, random.randint(0, 360), 0, 5, -0.1, 32),
        ]
        GameManager.particle += [
            ExplodeEnemy(0, self.SpriteID, self.point.x, self.point.y, True, self.Size, True, 0, 12, 1)]

####################################################################################################################################
class Enemy_alcholamp(Enemy):
    ST_STAND, ST_SHOOT = 0, 1

    img_rad = 0
    img_frame = 0
    img_tick = 0
    img_opacify = 1.0

    Size = 64

    stand_frame = 0
    shoot_frame = 0

    ignite_switch = False
    state = ST_STAND
    HIT = 64
    HP = 128

    def draw(self):
        RES.res.spr_enemy128.opacify(self.img_opacify)
        RES.res.spr_enemy128.clip_rotate_draw(self.img_rad, self.img_frame * 128, 0, 128, 128,
                                             self.point.x, self.point.y)
        drawhitbox(self.point, self.HIT)

    def move(self):
        self.rad = self.Angle * math.pi / 180

        if 0 < self.point.x < GameManager.CLIENT_WIDTH and 0 < self.point.y < GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE:
            self.point.x += self.Speed * math.cos(self.rad)
            self.point.y += self.Speed * math.sin(self.rad)
        else:
            self.ignite_switch = True
        self.Angle += self.AngleRate
        self.Speed += self.SpeedRate


    def handle_stand(self):
        self.stand_frame += 1
        if self.stand_frame > 1:
            self.shoot_frame = 0
            self.state = self.ST_SHOOT
        pass

    def handle_shoot(self):
        self.shoot_frame += 1
        if self.ignite_switch is True:
            if self.shoot_frame % 20 == 0:
                self.shoot()
            self.HP -= 10
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
        dice = [1, 2]
        random.shuffle(dice)
        if dice[0] == 1:
            GameManager.e_bullet += [
            EneBulletAngleCleaner(1, 0, self.point.x, self.point.y - 18,
                                  calcangle(self.point.x, self.point.y, GameManager.Player.point.x,
                                            GameManager.Player.point.y) + random.randint(-20, 20),
                        0, random.randint(5,10), 0.01)
            ]
        else:
            for i in range(4):
                GameManager.e_bullet += [
                    # EnemyBullet(random.randint(0, 5), random.randint(0, 6), self.point.x, self.point.y - 18, random.randint(0, 359), 0, 2, 0)
                    EnemyBullet(3, 0, self.point.x, self.point.y,
                                calcangle(self.point.x, self.point.y, GameManager.Player.point.x,
                                          GameManager.Player.point.y) + random.randint(-20, 20),
                                0, random.randint(5, 10), 0.01)
                ]
        if self.shoot_frame % 100 == 0:
            for i in range(3):
                GameManager.e_bullet += [
                EneBulletHatcher(2, 0, self.point.x, self.point.y,
                                 calcangle(self.point.x, self.point.y, GameManager.Player.point.x,
                                           GameManager.Player.point.y) + random.randint(-20, 20),
                            0, random.randint(5,8), -random.randint(1,2)/10)
                ]


    def KIA(self):
        for i in range(5):
            GameManager.item += [
                Item(self.point.x, self.point.y, 0, random.randint(0, 360), 0, 5, -0.1, 32),
            ]
            GameManager.particle += [
                ExplodeEnemy(0, self.SpriteID, self.point.x + random.randint(-8,8), self.point.y+ random.randint(-8,8), True, self.Size, True, 0, 12, 1)]
