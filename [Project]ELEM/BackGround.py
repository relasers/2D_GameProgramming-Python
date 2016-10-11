from pico2d import *
import FrameWork
import random

class BackGround:
    spr_back_1_1 = None
    spr_back_1_1_2 = None
    spr_back_1_1_3 = None
    spr_back_1_2 = None
    spr_back_1_3 = None
    spr_back_1_4 = None
    spr_back_1_5 = None
    pass

class BKStage1(BackGround):
    def __init__(self):
        self.spd_back_1_1 = 7
        self.y_spd_back_1_1 = 20
        self.y_spdr_back_1_1 = 0.14
        self.spd_back_1_1_2 = 9
        self.spd_back_1_1_3 = 8
        self.spd_back_1_2 = 4
        self.spd_back_1_3 = 3
        self.spd_back_1_4 = 2
        self.spd_back_1_5 = 1

        self.x_back_1_1 = FrameWork.CLIENT_WIDTH
        self.y_back_1_1 = 0
        self.x_back_1_1_2 = FrameWork.CLIENT_WIDTH
        self.x_back_1_1_3 = FrameWork.CLIENT_WIDTH
        self.x_back_1_2 = FrameWork.CLIENT_WIDTH
        self.x_back_1_3 = FrameWork.CLIENT_WIDTH
        self.x_back_1_4 = FrameWork.CLIENT_WIDTH
        self.x_back_1_5 = FrameWork.CLIENT_WIDTH

        if BackGround.spr_back_1_1 is None:
            BackGround.spr_back_1_1 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1.png')
        if BackGround.spr_back_1_1_2 is None:
            BackGround.spr_back_1_1_2 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1_2.png')
        if BackGround.spr_back_1_1_3 is None:
            BackGround.spr_back_1_1_3 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1_3.png')
        if BackGround.spr_back_1_2 is None:
            BackGround.spr_back_1_2 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_2.png')
        if BackGround.spr_back_1_3 is None:
            BackGround.spr_back_1_3 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_3.png')
        if BackGround.spr_back_1_4 is None:
            BackGround.spr_back_1_4 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_4.png')
        if BackGround.spr_back_1_5 is None:
            BackGround.spr_back_1_5 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_5.png')


    def update(self):
        self.x_back_1_1 = (self.x_back_1_1 - self.spd_back_1_1) % FrameWork.CLIENT_WIDTH
        self.y_back_1_1 -= self.y_spd_back_1_1
        self.x_back_1_1_2 = (self.x_back_1_1_2 - self.spd_back_1_1_2) % (FrameWork.CLIENT_WIDTH*2)
        self.x_back_1_1_3 = (self.x_back_1_1_3 - self.spd_back_1_1_3) % (FrameWork.CLIENT_WIDTH*2)
        self.x_back_1_2 = (self.x_back_1_2 - self.spd_back_1_2) % FrameWork.CLIENT_WIDTH
        self.x_back_1_3 = (self.x_back_1_3 - self.spd_back_1_3) % (FrameWork.CLIENT_WIDTH*2)
        self.x_back_1_4 = (self.x_back_1_4 - self.spd_back_1_4) % (FrameWork.CLIENT_WIDTH*2)
        self.x_back_1_5 = (self.x_back_1_5 - self.spd_back_1_5) % (FrameWork.CLIENT_WIDTH*2)
        if self.y_spd_back_1_1 >= 0:
            self.y_spd_back_1_1 -= self.y_spdr_back_1_1
            if self.y_spd_back_1_1 < 0:
                self.y_spd_back_1_1 = 0
    def draw(self):

        self.spr_back_1_5.clip_draw_to_origin(
            0, 0, FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT, self.x_back_1_5, 0)
        if self.x_back_1_5 < FrameWork.CLIENT_WIDTH*2:
            self.spr_back_1_5.clip_draw_to_origin(
                0, 0, FrameWork.CLIENT_WIDTH * 2, FrameWork.CLIENT_HEIGHT, self.x_back_1_5 - FrameWork.CLIENT_WIDTH*2, 0)

        self.spr_back_1_4.clip_draw_to_origin(
            0, 0, FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT, self.x_back_1_4, 0)
        if self.x_back_1_4 < FrameWork.CLIENT_WIDTH*2:
            self.spr_back_1_4.clip_draw_to_origin(
                0, 0, FrameWork.CLIENT_WIDTH * 2, FrameWork.CLIENT_HEIGHT, self.x_back_1_4 - FrameWork.CLIENT_WIDTH*2, 0)

        self.spr_back_1_3.clip_draw_to_origin(
            0, 0, FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT, self.x_back_1_3, 0)
        if self.x_back_1_3 < FrameWork.CLIENT_WIDTH*2:
            self.spr_back_1_3.clip_draw_to_origin(
                0, 0, FrameWork.CLIENT_WIDTH * 2, FrameWork.CLIENT_HEIGHT, self.x_back_1_3 - FrameWork.CLIENT_WIDTH*2, 0)

        self.spr_back_1_2.clip_draw_to_origin(
            0, 0, FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT*2, self.x_back_1_2, -1200)
        if self.x_back_1_2 < FrameWork.CLIENT_WIDTH:
            self.spr_back_1_2.clip_draw_to_origin(
                0, 0, FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT*2, self.x_back_1_2 - FrameWork.CLIENT_WIDTH, -1200)

        self.spr_back_1_1_2.opacify(random.randint(3, 5)/10)
        self.spr_back_1_1_2.clip_draw_to_origin(
            0, 0, FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT, self.x_back_1_1_2, 0)
        if self.x_back_1_1_2 < FrameWork.CLIENT_WIDTH*2:
            self.spr_back_1_1_2.clip_draw_to_origin(
                0, 0, FrameWork.CLIENT_WIDTH*2, FrameWork.CLIENT_HEIGHT, self.x_back_1_1_2 - FrameWork.CLIENT_WIDTH*2, 0)

        self.spr_back_1_1_3.opacify(random.randint(1, 2) / 10)
        self.spr_back_1_1_3.clip_draw_to_origin(
            0, 0, FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT, self.x_back_1_1_3, 0)
        if self.x_back_1_1_3 < FrameWork.CLIENT_WIDTH*2:
            self.spr_back_1_1_3.clip_draw_to_origin(
                0, 0, FrameWork.CLIENT_WIDTH*2, FrameWork.CLIENT_HEIGHT, self.x_back_1_1_3 - FrameWork.CLIENT_WIDTH*2, 0)

        self.spr_back_1_1.clip_draw_to_origin(
            0, 0, FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT * 2, self.x_back_1_1,  self.y_back_1_1)
        if self.x_back_1_1 < FrameWork.CLIENT_WIDTH:
            self.spr_back_1_1.clip_draw_to_origin(
                0, 0, FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT * 2, self.x_back_1_1 - FrameWork.CLIENT_WIDTH,
                self.y_back_1_1)
