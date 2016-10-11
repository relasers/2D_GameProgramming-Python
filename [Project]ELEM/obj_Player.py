from vector2D import *
from pico2d import *
from obj_Bullet import *
import GameManager
import random
import math


class Player:
    ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD = 0, 1, 2
    ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = 3, 4, 5

    HIGH_SPEED = 10
    LOW_SPEED = 4

    TICK_FRAME = 5
    TICK_SHOT = 5
    pass


class Ruby(Player):
    image = None

    def __init__(self, point_x, point_y):
        self.point = Vec2D(point_x, point_y)
        self.frame = random.randint(0, 4)
        self.xdir = self.ST_X_NONE
        self.ydir = self.ST_Y_NONE

        self.key_xstack = 0
        self.key_ystack = 0
        # check keyinput

        # set delay
        self.frametick = 0
        self.shottick = 0

        self.speed = self.HIGH_SPEED
        self.slowmode = False

        if Ruby.image is None:
            Ruby.image = load_image('Resources/images/Characters/Ally/Ruby_set.png')

        self.hit = 3
        self.isshooting = False
        self.isalive = True

    def draw(self):
        if self.isalive is True:
            if self.xdir == self.ST_X_BAKWARD:
                self.image.clip_draw(self.frame * 64, 0, 64, 64, self.point.x, self.point.y)
            else:
                self.image.clip_draw(self.frame * 64, 64, 64, 64, self.point.x, self.point.y)

    def update(self):
        self.frametick += 1

        if self.isalive is True and self.isshooting is True:
            self.shottick += 1

        if self.frametick % self.TICK_FRAME == 0:
            self.frame = (self.frame + 1) % 4
            self.frametick = 0

        # speed control
        if self.slowmode is False:
            self.speed = self.HIGH_SPEED
        else:
            self.speed = self.LOW_SPEED

        if self.xdir != self.ST_X_NONE and self.ydir != self.ST_Y_NONE:
            self.speed /= math.sqrt(2)

        self.move()

        if self.shottick % self.TICK_SHOT == 0 and self.isshooting is True and self.isalive is True:
            self.shoot()
            self.shottick = 0

    def shoot(self):
        if GameManager.Player_Power < 1:
            GameManager.p_bullet += [PlayerBullet(0, self.point.x, self.point.y, 0, 0, 5, 0.5)]

        elif 1 <= GameManager.Player_Power < 2:
            GameManager.p_bullet += [PlayerBullet(0, self.point.x, self.point.y + 5, 1, 0, 5, 0.5),
                                     PlayerBullet(0, self.point.x, self.point.y - 5, -1, 0, 5, 0.5)]

        elif 2 <= GameManager.Player_Power < 3:
            GameManager.p_bullet += [
                PlayerBulletChaser(0, self.point.x, self.point.y, 0, 0, 5, 0.5),
                PlayerBullet(0, self.point.x, self.point.y + 6, 1, 0, 5, 0.5),
                PlayerBullet(0, self.point.x, self.point.y - 6, -1, 0, 5, 0.5)]

        elif 3 <= GameManager.Player_Power < 4:
            GameManager.p_bullet += [
                PlayerBulletChaser(0, self.point.x, self.point.y+10, 0, 0, 5, 0.5),
                PlayerBulletChaser(0, self.point.x, self.point.y-10, 0, 0, 5, 0.5),
                PlayerBullet(0, self.point.x, self.point.y + 4, 1, 0, 5, 0.5),
                PlayerBullet(0, self.point.x, self.point.y - 4, -1, 0, 5, 0.5)]

        elif 4 <= GameManager.Player_Power:
            GameManager.p_bullet += [
                PlayerBulletChaser(0, self.point.x, self.point.y, random.randint(-3, 3), 0, 5, 0.5),
                PlayerBulletChaser(0, self.point.x-3, self.point.y + 16, 0, 0, 5, 0.5),
                PlayerBulletChaser(0, self.point.x-3, self.point.y - 16, 0, 0, 5, 0.5),
                PlayerBullet(0, self.point.x, self.point.y + 6, 1, 0, 5, 0.5),
                PlayerBullet(0, self.point.x, self.point.y - 6, -1, 0, 5, 0.5),
                PlayerBullet(0, self.point.x, self.point.y + 18, random.randint(-3, 3), 0, 5, 0.5),
                PlayerBullet(0, self.point.x, self.point.y - 18, random.randint(-3, 3), 0, 5, 0.5)
            ]

    def move(self):
        if self.xdir == self.ST_X_FORWARD:
            self.point.x += self.speed
        elif self.xdir == self.ST_X_BAKWARD:
            self.point.x -= self.speed

        if self.ydir == self.ST_Y_DOWN:
            self.point.y -= self.speed
        elif self.ydir == self.ST_Y_UP:
            self.point.y += self.speed

        if self.point.x < 0:
            self.point.x = 0
        if FrameWork.CLIENT_WIDTH < self.point.x:
            self.point.x = FrameWork.CLIENT_WIDTH
        if self.point.y < 0:
            self.point.y = 0
        if FrameWork.CLIENT_HEIGHT - FrameWork.UI_SIZE < self.point.y + 64:
            self.point.y = FrameWork.CLIENT_HEIGHT - FrameWork.UI_SIZE - 64

    def handle_chara(self, event):

        # handle kry down

        if event.type == SDL_KEYDOWN:

            if event.key == SDLK_UP:
                if self.ydir in (self.ST_Y_NONE, self.ST_Y_DOWN):
                    self.ydir = self.ST_Y_UP
                self.key_ystack += 1

            if event.key == SDLK_DOWN:
                if self.ydir in (self.ST_Y_NONE, self.ST_Y_UP):
                    self.ydir = self.ST_Y_DOWN
                self.key_ystack += 1

            if event.key == SDLK_RIGHT:
                if self.xdir in (self.ST_X_NONE, self.ST_X_BAKWARD):
                    self.xdir = self.ST_X_FORWARD
                self.key_xstack += 1

            if event.key == SDLK_LEFT:
                if self.xdir in (self.ST_X_NONE, self.ST_X_FORWARD):
                    self.xdir = self.ST_X_BAKWARD
                self.key_xstack += 1

            if event.key == SDLK_LSHIFT:
                self.slowmode = True

            if event.key == SDLK_z:
                self.isshooting = True

        # handle key Up

        if event.type == SDL_KEYUP:

            if event.key == SDLK_UP:
                self.key_ystack -= 1
                if self.key_ystack > 0:
                    self.ydir = self.ST_Y_DOWN
                else:
                    self.ydir = self.ST_Y_NONE

            if event.key == SDLK_DOWN:
                self.key_ystack -= 1
                if self.key_ystack > 0:
                    self.ydir = self.ST_Y_UP
                else:
                    self.ydir = self.ST_Y_NONE

            if event.key == SDLK_LEFT:
                self.key_xstack -= 1
                if self.key_xstack > 0:
                    self.xdir = self.ST_X_FORWARD
                else:
                    self.xdir = self.ST_X_NONE

            if event.key == SDLK_RIGHT:
                self.key_xstack -= 1
                if self.key_xstack > 0:
                    self.xdir = self.ST_X_BAKWARD
                else:
                    self.xdir = self.ST_X_NONE

            if event.key == SDLK_LSHIFT:
                self.slowmode = False

            if event.key == SDLK_z:
                self.isshooting = False