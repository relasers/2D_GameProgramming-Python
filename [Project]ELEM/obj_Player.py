from vector2D import *
from pico2d import *
from obj_Bullet import *
import random
import math


class Player:
    ST_X_NONE, ST_X_FORWARD, ST_X_BAKWARD = 0, 1, 2
    ST_Y_NONE, ST_Y_UP, ST_Y_DOWN = 3, 4, 5

    HIGH_SPEED = 6
    LOW_SPEED = 3

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

        if Ruby.image == None:
            Ruby.image = load_image('Resources/images/Characters/Ally/Ruby_set.png')

        self.hit = 3
        self.live = 3
        self.isshooting = False
        self.isalive = True

    def draw(self):
        if self.xdir == self.ST_X_BAKWARD:
            self.image.clip_draw(self.frame * 64, 0, 64, 64, self.point.x, self.point.y)
        else:
            self.image.clip_draw(self.frame * 64, 64, 64, 64, self.point.x, self.point.y)

    def shoot(self):
        return PlayerBullet(0, self.point.x, self.point.y, 0, 7, 5, 1)

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
            self.shottick = 0
            return True

        return False

    def move(self):
        if self.xdir == self.ST_X_FORWARD:
            self.point.x += self.speed
        elif self.xdir == self.ST_X_BAKWARD:
            self.point.x -= self.speed

        if self.ydir == self.ST_Y_DOWN:
            self.point.y -= self.speed
        elif self.ydir == self.ST_Y_UP:
            self.point.y += self.speed

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
