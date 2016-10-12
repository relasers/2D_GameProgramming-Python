from pico2d import *


class Res:

    spr_ruby = None
    spr_player_bullet = None

    spr_back_1_1 = None
    spr_back_1_1_2 = None
    spr_back_1_1_3 = None
    spr_back_1_2 = None
    spr_back_1_3 = None
    spr_back_1_4 = None
    spr_back_1_5 = None

    spr_back_2_0_0 = None
    spr_back_2_0_1 = None
    spr_back_2_1_day = None
    spr_back_2_1_night = None
    spr_back_2_2_day = None
    spr_back_2_2_night = None
    spr_back_2_3_day = None
    spr_back_2_3_night = None
    spr_back_2_4_day = None
    spr_back_2_4_night = None

    def __init__(self):

        self.spr_ruby = load_image('Resources/images/Characters/Ally/Ruby_set.png')
        self.spr_player_bullet = load_image('Resources/Images/Bullets/RBullet.png')
        self.spr_back_1_1 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1.png')
        self.spr_back_1_1_2 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1_2.png')
        self.spr_back_1_1_3 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1_3.png')
        self.spr_back_1_2 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_2.png')
        self.spr_back_1_3 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_3.png')
        self.spr_back_1_4 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_4.png')
        self.spr_back_1_5 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_5.png')

        self.spr_back_2_0_0 = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_0_0.png')
        self.spr_back_2_0_1 = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_0_1.png')
        self.spr_back_2_1_day = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_1_day.png')
        self.spr_back_2_1_night = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_1_night.png')
        self.spr_back_2_2_day = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_2_day.png')
        self.spr_back_2_2_night = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_2_night.png')
        self.spr_back_2_3_day = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_3_day.png')
        self.spr_back_2_3_night = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_3_night.png')
        self.spr_back_2_4_day = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_4_day.png')
        self.spr_back_2_4_night = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_4_night.png')








# Resource