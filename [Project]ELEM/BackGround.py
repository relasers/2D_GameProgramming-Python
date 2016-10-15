from pico2d import *
import GameManager
import FrameWork
import RES
import random


class BackGround:
    pass


class BKStage1(BackGround):

    PHASE1, PHASE2, PHASE3, PHASE4 = 0, 1, 2, 3
    Timer = 0
    def __init__(self):
        self.Timer = 0
        self.state = self.PHASE1
        self.switch_boss = False
        self.spd_back_1_1 = 1
        self.y_spd_back_1_1 = 40
        self.y_spdr_back_1_1 = 0.55 # BackGrond 1's SpeedRate

        self.spd_back_1_2 = 14
        self.spd_back_1_3 = 12
        self.spd_back_1_4 = 8
        self.spd_back_1_5 = 6
        self.spd_back_1_6 = 4
        self.spd_back_1_7 = 2

        self.x_back_1_1 = GameManager.CLIENT_WIDTH
        self.y_back_1_1 = 0
        self.x_back_1_2 = GameManager.CLIENT_WIDTH
        self.x_back_1_3 = GameManager.CLIENT_WIDTH
        self.x_back_1_4 = GameManager.CLIENT_WIDTH
        self.x_back_1_5 = GameManager.CLIENT_WIDTH
        self.x_back_1_6 = GameManager.CLIENT_WIDTH
        self.x_back_1_7 = GameManager.CLIENT_WIDTH

    def handle_phase_1(self):
        pass
    def handle_phase_2(self):
        if self.spd_back_1_1 < 24:
                self.spd_back_1_1 += 0.1
        pass
    def handle_phase_3(self):
        self.y_back_1_1 -= self.y_spd_back_1_1
        self.spd_back_1_1 = 24
        if self.y_spd_back_1_1 >= 0:
            self.y_spd_back_1_1 -= self.y_spdr_back_1_1
            if self.y_spd_back_1_1 < 0:
                self.y_spd_back_1_1 = 0
        pass

    def handle_phase_4(self):
        self.switch_boss = True
        pass

    handle_state = {
        PHASE1: handle_phase_1,
        PHASE2: handle_phase_2,
        PHASE3: handle_phase_3,
        PHASE4: handle_phase_4
    }

    def update(self):
        if self.Timer == 0:
            RES.res.snd_back_1.set_volume(100)
            RES.res.snd_back_1.play()
        self.Timer += 1
        self.x_back_1_1 = (self.x_back_1_1 - self.spd_back_1_1) % GameManager.CLIENT_WIDTH
        self.x_back_1_2 = (self.x_back_1_2 - self.spd_back_1_2) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_1_3 = (self.x_back_1_3 - self.spd_back_1_3) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_1_4 = (self.x_back_1_4 - self.spd_back_1_4) % GameManager.CLIENT_WIDTH
        self.x_back_1_5 = (self.x_back_1_5 - self.spd_back_1_5) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_1_6 = (self.x_back_1_6 - self.spd_back_1_6) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_1_7 = (self.x_back_1_7 - self.spd_back_1_7) % (GameManager.CLIENT_WIDTH * 2)
        self.handle_state[self.state](self)

        if self.Timer == 2380:
            self.state += 1
        if self.Timer == 3200:
            self.state += 1


    def draw(self):
        self.scrollingBG(RES.res.spr_back_1_7, self.x_back_1_7, 0, GameManager.CLIENT_WIDTH * 2,GameManager.CLIENT_HEIGHT)
        self.scrollingBG(RES.res.spr_back_1_6, self.x_back_1_6, 0, GameManager.CLIENT_WIDTH * 2,GameManager.CLIENT_HEIGHT)
        self.scrollingBG(RES.res.spr_back_1_5, self.x_back_1_5, 0, GameManager.CLIENT_WIDTH*2,GameManager.CLIENT_HEIGHT)
        self.scrollingBG(RES.res.spr_back_1_4, self.x_back_1_4, -1200, GameManager.CLIENT_WIDTH,GameManager.CLIENT_HEIGHT*2)
        if self.switch_boss is True:
            RES.res.spr_back_1_2.opacify(random.randint(0, 1) / 10)
            self.scrollingBG(RES.res.spr_back_1_2, self.x_back_1_2, 0, GameManager.CLIENT_WIDTH * 2,GameManager.CLIENT_HEIGHT)
            RES.res.spr_back_1_3.opacify(random.randint(1, 2) / 10)
            self.scrollingBG(RES.res.spr_back_1_3, self.x_back_1_3, 0, GameManager.CLIENT_WIDTH*2,GameManager.CLIENT_HEIGHT)
        self.scrollingBG(RES.res.spr_back_1_1,self.x_back_1_1,self.y_back_1_1,GameManager.CLIENT_WIDTH,GameManager.CLIENT_HEIGHT*2)

        RES.res.font_elem.draw(300, 780, " Timer :: %s " % self.Timer, (255, 0, 255))
    def scrollingBG(self,img,x,y,width,height):
        img.clip_draw_to_origin(0, 0, width, height, x, y)
        if x < width:
            img.clip_draw_to_origin(0, 0, width, height, x - width,y)