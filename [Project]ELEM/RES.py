from pico2d import *

res = None


def loading_data():
    global res
    res = Res()



class Res:

    font_elem = None

    spr_ruby = None

    spr_player_bullet = None
    spr_bullet32 = None

    spr_enemy64 = None
    spr_fairy = None


    spr_back_1_1 = None
    spr_back_1_2 = None
    spr_back_1_3 = None
    spr_back_1_4 = None
    spr_back_1_5 = None
    spr_back_1_6 = None
    spr_back_1_7 = None

    spr_back_2_0 = None
    spr_back_2_1 = None
    spr_back_2_2_d = None
    spr_back_2_2_n = None
    spr_back_2_3_d = None
    spr_back_2_3_n = None
    spr_back_2_4_d = None
    spr_back_2_4_n = None
    spr_back_2_5_d = None
    spr_back_2_5_n = None

    snd_back_1 = None

    snd_shoot = None
    snd_e_shoot = None
    snd_destroy = None
    def __init__(self):

        # self.font_elem = Font('Resources/Fonts/tennobet.ttf',30)
        self.font_elem = Font('Resources/Fonts/chemrea.ttf', 30)
        self.spr_ruby = load_image('Resources/images/Characters/Ally/Ruby_set.png')

        self.spr_player_bullet = load_image('Resources/Images/Bullets/RBullet.png')
        self.spr_bullet32 = load_image('Resources/Images/Bullets/Bullet32.png')
        self.spr_enemy64 = load_image('Resources/Images/Characters/Enemy/enemy_64.png')
        self.spr_fairy = load_image('Resources/Images/Characters/Enemy/Fairy.png')

        self.spr_back_1_1 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1.png')
        self.spr_back_1_2 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1_2.png')
        self.spr_back_1_3 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_1_3.png')
        self.spr_back_1_4 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_2.png')
        self.spr_back_1_5 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_3.png')
        self.spr_back_1_6 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_4.png')
        self.spr_back_1_7 = load_image('Resources/Images/BackGrounds/Stage_1/Back_1_5.png')

        self.spr_back_2_0 = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_0_0.png')
        self.spr_back_2_1 = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_0_1.png')
        self.spr_back_2_2_d = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_1_day.png')
        self.spr_back_2_2_n = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_1_night.png')
        self.spr_back_2_3_d = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_2_day.png')
        self.spr_back_2_3_n = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_2_night.png')
        self.spr_back_2_4_d = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_3_day.png')
        self.spr_back_2_4_n = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_3_night.png')
        self.spr_back_2_5_d = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_4_day.png')
        self.spr_back_2_5_n = load_image('Resources/Images/BackGrounds/Stage_2/Back_2_4_night.png')

        self.snd_back_1 = load_music('Resources/Sounds/BGM/Fable-Mili.ogg')

        self.snd_shoot = load_wav('Resources/Sounds/SE/plst00.wav')
        self.snd_shoot.set_volume(10)

        self.snd_e_shoot = load_wav('Resources/Sounds/SE/tan01.wav')
        self.snd_e_shoot.set_volume(1)

        self.snd_destroy = load_wav('Resources/Sounds/SE/tan00.wav')
        self.snd_destroy.set_volume(20)







        # Resource