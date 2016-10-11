from pico2d import *


class BackGround:
    back_1_1 = None
    back_1_1_2 = None
    back_1_1_3 = None
    back_1_2 = None
    back_1_3 = None
    back_1_4 = None
    back_1_5 = None


class BKStage1(BackGround):
    def __init__(self):
        if BackGround.back_1_1 is None:
            BackGround.back_1_1 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1.png')
        if BackGround.back_1_1_2 is None:
            BackGround.back_1_1_2 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1_2.png')
        if BackGround.back_1_1_3 is None:
            BackGround.back_1_1_3 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1_3.png')
        if BackGround.back_1_2 is None:
            BackGround.back_1_2 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_2.png')
        if BackGround.back_1_3 is None:
            BackGround.back_1_3 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_3.png')
        if BackGround.back_1_4 is None:
            BackGround.back_1_4 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_4.png')
        if BackGround.back_1_5 is None:
            BackGround.back_1_5 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_5.png')

    def update(self):
        pass

    def draw(self):
        pass