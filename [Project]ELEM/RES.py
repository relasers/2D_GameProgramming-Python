from pico2d import *

res = None


def loading_data():
    global res
    res = Res()



class Res:

    font_elem = None

    spr_ruby = None

    spr_item = None

    spr_player_bullet = None
    spr_bullet32 = None
    spr_bullet64 = None
    spr_Fire192 = None

    spr_enemy64 = None
    spr_fairy = None
    spr_carrier = None

    spr_boss1 = None
    spr_boss2 = None

    spr_ring = None
    spr_core = None
    spr_explode = None
    spr_Warning = None
    spr_magicblast = None

    spr_pause = None
    spr_UIbar = None
    spr_powerbar = None

    spr_back_mainTitle = None
    spr_back_mainTitle_gray = None
    spr_press_start = None

    spr_back_gameover = None
    spr_back_gameover_gray = None
    spr_press_backto = None

    spr_ranklens = None
    spr_back_rankpage = None

    spr_back_logo = None
    spr_back_black = None
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

    snd_main = None
    snd_gameover = None
    snd_back_1 = None
    snd_back_boss_1 = None

    snd_shoot = None
    snd_ruby_bomb = None
    snd_e_shoot = None
    snd_destroy = None
    snd_alarm = None
    def __init__(self):

        # self.font_elem = Font('Resources/Fonts/tennobet.ttf',30)
        self.font_elem = Font('Resources/Fonts/chemrea.ttf', 16)
        self.spr_ruby = load_image('Resources/images/Characters/Ally/Ruby_set.png')

        self.spr_item = load_image('Resources/images/Misc/item.png')

        self.spr_player_bullet = load_image('Resources/Images/Bullets/RBullet.png')
        self.spr_bullet32 = load_image('Resources/Images/Bullets/Bullet32.png')
        self.spr_enemy64 = load_image('Resources/Images/Characters/Enemy/enemy_64.png')
        self.spr_fairy = load_image('Resources/Images/Characters/Enemy/Fairy.png')
        self.spr_carrier = load_image('Resources/Images/Characters/Enemy/Gilbert.png')

        self.spr_bullet64 = load_image('Resources/Images/Bullets/Bullet64.png')
        self.spr_Fire192 = load_image('Resources/Images/Bullets/Fire_192.png')


        self.spr_boss1 = load_image('Resources/Images/Characters/Enemy/Boss1.png')
        self.spr_boss2 = load_image('Resources/Images/Characters/Enemy/Boss1.png')

        self.spr_ring = load_image('Resources/Images/Effects/tunelring.png')
        self.spr_core = load_image('Resources/Images/Effects/Core256.png')
        self.spr_explode = load_image('Resources/Images/Effects/Core256.png')
        self.spr_Warning = load_image('Resources/Images/Effects/Warning.png')
        self.spr_magicblast = load_image('Resources/Images/Effects/MagicBlast.png')

        self.spr_pause = load_image('Resources/Images/BackGrounds/Main/Pause.png')
        self.spr_UIbar = load_image('Resources/Images/BackGrounds/Main/UI.png')
        self.spr_powerbar = load_image('Resources/Images/BackGrounds/Main/PowerBar.png')

        self.spr_back_logo = load_image('Resources/Images/BackGrounds/Main/Logo.png')
        self.spr_back_black = load_image('Resources/Images/BackGrounds/Main/Blackscn.png')

        self.spr_back_mainTitle = load_image('Resources/Images/BackGrounds/Main/MainTitle.png')
        self.spr_back_mainTitle_gray = load_image('Resources/Images/BackGrounds/Main/MainTitle_gray.png')
        self.spr_press_start = load_image('Resources/Images/BackGrounds/Main/Start.png')

        self.spr_back_gameover = load_image('Resources/Images/BackGrounds/Main/GameOver.png')
        self.spr_back_gameover_gray = load_image('Resources/Images/BackGrounds/Main/GameOver-gray.png')
        self.spr_press_backto = load_image('Resources/Images/BackGrounds/Main/BackTo.png')

        self.spr_ranklens =  load_image('Resources/Images/BackGrounds/Main/800lens.png')
        self.spr_back_rankpage =  load_image('Resources/Images/BackGrounds/Main/RankPage.png')

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

        self.snd_main = load_music('Resources/Sounds/BGM/fogotten_temple.ogg')
        self.snd_back_1 = load_music('Resources/Sounds/BGM/Fable-Mili.ogg')
        self.snd_back_boss_1 = load_music('Resources/Sounds/BGM/Nemesis.ogg')
        self.snd_gameover = load_music('Resources/Sounds/BGM/Aases_Death.ogg')

        self.snd_shoot = load_wav('Resources/Sounds/SE/plst00.wav')
        self.snd_shoot.set_volume(10)

        self.snd_ruby_bomb = load_wav('Resources/Sounds/SE/crystal2.wav')
        self.snd_ruby_bomb.set_volume(40)

        self.snd_e_shoot = load_wav('Resources/Sounds/SE/tan01.wav')
        self.snd_e_shoot.set_volume(1)

        self.snd_destroy = load_wav('Resources/Sounds/SE/tan00.wav')
        self.snd_destroy.set_volume(20)

        self.snd_alarm = load_wav('Resources/Sounds/SE/Alarm.wav')






        # Resource