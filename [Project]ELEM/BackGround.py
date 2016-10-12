from pico2d import *
from RES import *
import FrameWork
import random


class BackGround:
    pass


class BKStage1(BackGround):
    def __init__(self):
        self.switch_uptosky = False
        self.spd_back_1_1 = 1
        self.y_spd_back_1_1 = 20
        self.y_spdr_back_1_1 = 0.14
        self.spd_back_1_1_2 = 14
        self.spd_back_1_1_3 = 12
        self.spd_back_1_2 = 8
        self.spd_back_1_3 = 6
        self.spd_back_1_4 = 4
        self.spd_back_1_5 = 2

        self.x_back_1_1 = FrameWork.CLIENT_WIDTH
        self.y_back_1_1 = 0
        self.x_back_1_1_2 = FrameWork.CLIENT_WIDTH
        self.x_back_1_1_3 = FrameWork.CLIENT_WIDTH
        self.x_back_1_2 = FrameWork.CLIENT_WIDTH
        self.x_back_1_3 = FrameWork.CLIENT_WIDTH
        self.x_back_1_4 = FrameWork.CLIENT_WIDTH
        self.x_back_1_5 = FrameWork.CLIENT_WIDTH

    def update(self):
        self.x_back_1_1 = (self.x_back_1_1 - self.spd_back_1_1) % FrameWork.CLIENT_WIDTH
        self.x_back_1_1_2 = (self.x_back_1_1_2 - self.spd_back_1_1_2) % (FrameWork.CLIENT_WIDTH * 2)
        self.x_back_1_1_3 = (self.x_back_1_1_3 - self.spd_back_1_1_3) % (FrameWork.CLIENT_WIDTH * 2)
        self.x_back_1_2 = (self.x_back_1_2 - self.spd_back_1_2) % FrameWork.CLIENT_WIDTH
        self.x_back_1_3 = (self.x_back_1_3 - self.spd_back_1_3) % (FrameWork.CLIENT_WIDTH * 2)
        self.x_back_1_4 = (self.x_back_1_4 - self.spd_back_1_4) % (FrameWork.CLIENT_WIDTH * 2)
        self.x_back_1_5 = (self.x_back_1_5 - self.spd_back_1_5) % (FrameWork.CLIENT_WIDTH * 2)
        if self.switch_uptosky is True:
            self.y_back_1_1 -= self.y_spd_back_1_1
            self.spd_back_1_1 = 24
            if self.y_spd_back_1_1 >= 0:
                self.y_spd_back_1_1 -= self.y_spdr_back_1_1
                if self.y_spd_back_1_1 < 0:
                    self.y_spd_back_1_1 = 0

    def draw(self):

        self.scrollingBG(FrameWork.sprite.spr_back_1_5, self.x_back_1_5, 0, FrameWork.CLIENT_WIDTH * 2,FrameWork.CLIENT_HEIGHT)
        self.scrollingBG(FrameWork.sprite.spr_back_1_4, self.x_back_1_4, 0, FrameWork.CLIENT_WIDTH * 2,FrameWork.CLIENT_HEIGHT)
        self.scrollingBG(FrameWork.sprite.spr_back_1_3, self.x_back_1_3, 0, FrameWork.CLIENT_WIDTH*2,FrameWork.CLIENT_HEIGHT)
        self.scrollingBG(FrameWork.sprite.spr_back_1_2, self.x_back_1_2, -1200, FrameWork.CLIENT_WIDTH,FrameWork.CLIENT_HEIGHT*2)
        FrameWork.sprite.spr_back_1_1_2.opacify(random.randint(3, 5) / 10)
        self.scrollingBG(FrameWork.sprite.spr_back_1_1_2, self.x_back_1_1_2, 0, FrameWork.CLIENT_WIDTH * 2,FrameWork.CLIENT_HEIGHT)
        FrameWork.sprite.spr_back_1_1_3.opacify(random.randint(1, 2) / 10)
        self.scrollingBG(FrameWork.sprite.spr_back_1_1_3, self.x_back_1_1_3, 0, FrameWork.CLIENT_WIDTH*2,FrameWork.CLIENT_HEIGHT)
        self.scrollingBG(FrameWork.sprite.spr_back_1_1,self.x_back_1_1,self.y_back_1_1,FrameWork.CLIENT_WIDTH,FrameWork.CLIENT_HEIGHT*2)


    def scrollingBG(self,img,x,y,width,height):
        img.clip_draw_to_origin(0, 0, width, height, x, y)
        if x < width:
            img.clip_draw_to_origin(0, 0, width, height, x - width,y)