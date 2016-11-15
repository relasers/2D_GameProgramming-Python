from pico2d import *
from vector2D import *
import RES
import math
import random

class Particle(Actor):
    MOD_PLUS, MOD_MINUS = 0,1

    opacify = 1
    MX_frame = 4

    isExpension = False
    ExpensionMode = MOD_PLUS

    spr_id = 0
    spr_color = 0

    img_frame = 0
    img_Size = 0
    img_Rad = 0
    img_ExpSize = 0
    img_SizRate = 0 # Expension image Size Rate

    Fade_out = False
    def __init__(self, spriteid, spritecolor, x, y,fadeout,size,isExpansion,Expansionmode,ExpSize,ExpRate):
        self.point.x = x
        self.point.y = y

        self.spr_id = spriteid
        self.spr_color = spritecolor

        self.Fade_out = fadeout
        self.img_Size = size

        self.isExpension = isExpansion
        self.ExpensionMode = Expansionmode

        self.img_ExpSize = ExpSize
        self.SizRate = ExpRate

        pass
    def isDestroy(self):
        if self.img_frame == self.MX_frame:
            return True
        if self.opacify < 0:
            return True
    def update(self):

        if self.Fade_out is True:
            self.opacify -= 0.1
        if self.isExpension is True:
            if self.ExpensionMode is self.MOD_PLUS:
                self.img_Size += self.img_ExpSize
            elif self.ExpensionMode is self.MOD_MINUS:
                self.img_Size -= self.img_ExpSize

        self.img_ExpSize += self.img_SizRate


class ExplodeEnemy(Particle):
    def update(self):
        self.img_Rad = (self.img_Rad + 12) % 360
        if self.Fade_out is True:
            self.opacify -= 0.1
        if self.isExpension is True:
            if self.ExpensionMode is self.MOD_PLUS:
                self.img_Size += self.img_ExpSize
            elif self.ExpensionMode is self.MOD_MINUS:
                self.img_Size -= self.img_ExpSize

        self.img_ExpSize += self.img_SizRate

    def draw(self):
        RES.res.spr_explode.opacify(self.opacify)
        RES.res.spr_explode.clip_rotate_draw(self.img_Rad, self.spr_color*256,self.spr_id*256 , 256, 256, self.point.x, self.point.y, self.img_Size,
                                                   self.img_Size)

class MagicBlast(Actor):

    def __init__(self,x,y,israndom):
        self.MX_frame = 16
        self.img_frame = 0
        self.img_tick = 0

        self.point.x = x
        self.point.y = y

        if israndom is True:
            self.point.x += random.randint(-128, 128)
            self.point.y += random.randint(-128, 128)


    def update(self):
        self.img_tick += 1

        if self.img_tick > 2:
            self.img_frame += 1
            self.img_tick = 0

    def draw(self):
        RES.res.spr_magicblast.clip_rotate_draw(0, self.img_frame*256, 0  , 128, 128, self.point.x, self.point.y, 256,
                                                  256)
    def isDestroy(self):
        if self.img_frame > 16:
            return True

class Warning(Particle):
    LIFE = 360
    img_Rad = 0
    def update(self):
        self.img_Rad = (self.img_Rad + 4) % 360
        self.LIFE -= 1

        if self.LIFE % 100 == 0:
            RES.res.snd_alarm.play()

        self.opacify = max(0,math.sin(self.img_Rad * math.pi / 180.0))


    def draw(self):
        RES.res.spr_Warning.opacify(self.opacify)
        RES.res.spr_Warning.draw(GameManager.CLIENT_WIDTH/2, (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE)/2 )


    def isDestroy(self):
        if self.LIFE < 0:
            return True