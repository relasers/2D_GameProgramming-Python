from pico2d import *
from vector2D import *
import RES

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


