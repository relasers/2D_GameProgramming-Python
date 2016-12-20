from pico2d import *
import GameManager
import FrameWork
import RES
import random
import math


class BackGround:
    pass

class BKStage1(BackGround):

    PHASE1, PHASE2, PHASE3, PHASE4 , PHASE5 = 0, 1, 2, 3, 4
    def __init__(self):

        self.state = self.PHASE1
        self.switch_boss = False
        self.spd_back_1_1 = 1
        self.y_spd_back_1_1 = 47.5
        self.y_spdr_back_1_1 = 0.55 # BackGrond 1's SpeedRate

        self.black_opac = 1.0

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
        if self.black_opac > 0:
            self.black_opac = max(0,self.black_opac - 0.01)
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

    def handle_phase_5(self):
        if self.black_opac < 1:
            self.black_opac = min(1,self.black_opac + 0.01)
        pass

    handle_state = {
        PHASE1: handle_phase_1,
        PHASE2: handle_phase_2,
        PHASE3: handle_phase_3,
        PHASE4: handle_phase_4,
        PHASE5: handle_phase_5
    }

    def update(self):
        if GameManager.maintime == 0:
            RES.res.snd_back_1.set_volume(100)
            RES.res.snd_back_1.play()

        self.x_back_1_1 = (self.x_back_1_1 - self.spd_back_1_1) % GameManager.CLIENT_WIDTH
        self.x_back_1_2 = (self.x_back_1_2 - self.spd_back_1_2) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_1_3 = (self.x_back_1_3 - self.spd_back_1_3) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_1_4 = (self.x_back_1_4 - self.spd_back_1_4) % GameManager.CLIENT_WIDTH
        self.x_back_1_5 = (self.x_back_1_5 - self.spd_back_1_5) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_1_6 = (self.x_back_1_6 - self.spd_back_1_6) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_1_7 = (self.x_back_1_7 - self.spd_back_1_7) % (GameManager.CLIENT_WIDTH * 2)
        self.handle_state[self.state](self)

        if GameManager.maintime == 2380:
            self.state += 1
        if GameManager.maintime == 3200:
            self.state += 1
        if GameManager.maintime == 6500:
            RES.res.snd_back_boss_1.set_volume(100)
            RES.res.snd_back_boss_1.play()
            self.state += 1


    def draw(self):
        self.scrollingBG(RES.res.spr_back_1_7, self.x_back_1_7, 0, GameManager.CLIENT_WIDTH * 2,1200)
        self.scrollingBG(RES.res.spr_back_1_6, self.x_back_1_6, -200, GameManager.CLIENT_WIDTH * 2,1200)
        self.scrollingBG(RES.res.spr_back_1_5, self.x_back_1_5, 0, GameManager.CLIENT_WIDTH*2,1200)
        self.scrollingBG(RES.res.spr_back_1_4, self.x_back_1_4, -1800, GameManager.CLIENT_WIDTH,2400)
        if self.switch_boss is True:
            RES.res.spr_back_1_2.opacify(random.randint(3, 5) / 10)
            self.scrollingBG(RES.res.spr_back_1_2, self.x_back_1_2, 0, GameManager.CLIENT_WIDTH * 2,1200)
            RES.res.spr_back_1_3.opacify(random.randint(5, 7) / 10)
            self.scrollingBG(RES.res.spr_back_1_3, self.x_back_1_3, 0, GameManager.CLIENT_WIDTH*2,1200)
        self.scrollingBG(RES.res.spr_back_1_1,self.x_back_1_1,self.y_back_1_1,GameManager.CLIENT_WIDTH,2400)
        RES.res.spr_back_blackscreen.opacify(self.black_opac)
        RES.res.spr_back_blackscreen.draw(600, 384)


    def scrollingBG(self,img,x,y,width,height):
        img.clip_draw_to_origin(0, 0, width, height, x, y)
        if x < width:
            img.clip_draw_to_origin(0, 0, width, height, x - width,y)

    def pauseMusic(self):
        RES.res.snd_back_1.pause()

    def resumeMusic(self):
        RES.res.snd_back_1.resume()


class BKStage2(BackGround):
    PHASE1, PHASE2, PHASE3, PHASE4,PHASE5,PHASE6,PHASE7 = 0, 1, 2, 3,4,5,6
    def __init__(self):

        self.state = self.PHASE1
        self.switch_boss = False
        self.spd_back_sky = 0.5
        self.x_spd_back_mountain = 3
        self.x_spd_back_water = 5
        self.x_spd_back_city = 7
        self.x_spd_back_arch = 10

        self.y_spd_back_lake = 2

        self.black_opac = 1.0
        self.morningsky_opac = 1.0
        self.daysky_opac = 1.0

        self.lake_opac = 1.0

        self.daycity_opac = 0.0
        self.nightcity_opac = 0.0

        self.dayarch_opac = 0.0
        self.nightarch_opac = 0.0
        self.chaosarch_opac = 0.0
        self.chaosopac_angle = 0

        self.spd_back_boss_1 = 14
        self.spd_back_boss_2 = 12

        self.x_back_sky = GameManager.CLIENT_WIDTH
        self.x_back_mountain = GameManager.CLIENT_WIDTH
        self.x_back_water = GameManager.CLIENT_WIDTH
        self.y_back_lake = -800
        self.x_back_boss_1 = GameManager.CLIENT_WIDTH
        self.x_back_boss_2 = GameManager.CLIENT_WIDTH
        self.x_back_city = GameManager.CLIENT_WIDTH
        self.x_back_arch = GameManager.CLIENT_WIDTH

    def handle_phase_1(self):
        if self.black_opac > 0:
            self.black_opac = max(0,self.black_opac - 0.01)
        pass
    def handle_phase_2(self):
        if self.morningsky_opac > 0:
            self.morningsky_opac = max(0,self.morningsky_opac - 0.01)

        if self.y_back_lake < 0:
            self.y_back_lake += self.y_spd_back_lake
        pass
    def handle_phase_3(self):
        if self.spd_back_sky < 3:
            self.spd_back_sky += 0.01
            self.x_spd_back_mountain += 0.01
            self.x_spd_back_water += 0.015
        pass

    def handle_phase_4(self):
        if self.daycity_opac < 1:
            self.daycity_opac = min(1,self.daycity_opac + 0.05)

        pass

    def handle_phase_5(self):
        if self.dayarch_opac < 1:
            self.dayarch_opac = min(1,self.dayarch_opac + 0.05)
        pass

    def handle_phase_6(self):
        if self.daysky_opac > 0:
            self.daysky_opac = max(0,self.daysky_opac - 0.01)
            self.lake_opac = max(0,self.lake_opac - 0.01)
            self.daycity_opac = max(0, self.daycity_opac - 0.01)
            self.dayarch_opac = max(0, self.dayarch_opac - 0.01)
        self.nightcity_opac = 1 - self.daycity_opac
        self.nightarch_opac = 1 - self.dayarch_opac

        pass

    def handle_phase_7(self):
        self.switch_boss = True
        self.chaosopac_angle = (self.chaosopac_angle + 1) % 360
        self.chaosarch_opac = 0.5 + math.sin(self.chaosopac_angle * math.pi / 180.0)*0.5
        pass

    handle_state = {
        PHASE1: handle_phase_1,
        PHASE2: handle_phase_2,
        PHASE3: handle_phase_3,
        PHASE4: handle_phase_4,
        PHASE5: handle_phase_5,
        PHASE6: handle_phase_6,
        PHASE7: handle_phase_7
    }

    def update(self):
        if GameManager.maintime == 0:
            RES.res.snd_back_2.set_volume(100)
            RES.res.snd_back_2.play()

        self.x_back_sky = (self.x_back_sky - self.spd_back_sky) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_mountain = (self.x_back_mountain - self.x_spd_back_mountain) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_water = (self.x_back_water - self.x_spd_back_water) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_city = (self.x_back_city - self.x_spd_back_city) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_arch = (self.x_back_arch - self.x_spd_back_arch) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_boss_1 = (self.x_back_boss_1 - self.spd_back_boss_1) % (GameManager.CLIENT_WIDTH * 2)
        self.x_back_boss_2 = (self.x_back_boss_2 - self.spd_back_boss_2) % (GameManager.CLIENT_WIDTH * 2)

        self.handle_state[self.state](self)

        if GameManager.maintime == 500:
            self.state += 1
        if GameManager.maintime == 950:
            self.state += 1
        if GameManager.maintime == 2020:
            self.state += 1
        if GameManager.maintime == 2920:
            self.state += 1
        if GameManager.maintime == 5720:
            RES.res.snd_back_boss_2.set_volume(100)
            RES.res.snd_back_boss_2.play()
            self.state += 1
        if GameManager.maintime == 7350:
            self.state += 1


    def draw(self):

        RES.res.spr_back_2_morningsky.opacify(self.morningsky_opac)
        RES.res.spr_back_2_daysky.opacify(self.daysky_opac)


        self.scrollingBG(RES.res.spr_back_2_nightsky, self.x_back_sky, 0, GameManager.CLIENT_WIDTH * 2, 2400)
        self.scrollingBG(RES.res.spr_back_2_daysky, self.x_back_sky, 0, GameManager.CLIENT_WIDTH * 2, 2400)
        self.scrollingBG(RES.res.spr_back_2_morningsky , self.x_back_sky, 0, GameManager.CLIENT_WIDTH * 2,2400)

        RES.res.spr_back_2_daywater.opacify(self.lake_opac)
        RES.res.spr_back_2_nightwater.opacify(1 - self.lake_opac)
        RES.res.spr_back_2_daymountain.opacify(self.lake_opac)
        RES.res.spr_back_2_nightmountain.opacify(1 - self.lake_opac)


        self.scrollingBG(RES.res.spr_back_2_nightwater, self.x_back_water, self.y_back_lake,
                         GameManager.CLIENT_WIDTH * 2,
                         800)
        self.scrollingBG(RES.res.spr_back_2_nightmountain, self.x_back_mountain, self.y_back_lake,
                         GameManager.CLIENT_WIDTH * 2,
                         800)

        self.scrollingBG(RES.res.spr_back_2_daywater, self.x_back_water, self.y_back_lake, GameManager.CLIENT_WIDTH*2, 800)
        self.scrollingBG(RES.res.spr_back_2_daymountain, self.x_back_mountain, self.y_back_lake, GameManager.CLIENT_WIDTH*2,
                         800)

        RES.res.spr_back_2_daycity.opacify(self.daycity_opac)
        RES.res.spr_back_2_nightcity.opacify(self.nightcity_opac)
        RES.res.spr_back_2_chaoscity.opacify(self.chaosarch_opac)
        self.scrollingBG(RES.res.spr_back_2_nightcity, self.x_back_city, 0,GameManager.CLIENT_WIDTH * 2,800)
        self.scrollingBG(RES.res.spr_back_2_daycity, self.x_back_city, 0, GameManager.CLIENT_WIDTH * 2, 800)
        self.scrollingBG(RES.res.spr_back_2_chaoscity, self.x_back_city, 0, GameManager.CLIENT_WIDTH * 2, 800)

        RES.res.spr_back_2_dayarch.opacify(self.dayarch_opac)
        RES.res.spr_back_2_nightarch.opacify(self.nightarch_opac)
        RES.res.spr_back_2_chaosarch.opacify(self.chaosarch_opac)
        self.scrollingBG(RES.res.spr_back_2_nightarch, self.x_back_arch, 0, GameManager.CLIENT_WIDTH * 2, 800)
        self.scrollingBG(RES.res.spr_back_2_dayarch, self.x_back_arch, 0, GameManager.CLIENT_WIDTH * 2, 800)
        self.scrollingBG(RES.res.spr_back_2_chaosarch, self.x_back_arch, 0, GameManager.CLIENT_WIDTH * 2, 800)

        if self.switch_boss is True:
            RES.res.spr_back_2_boss_1.opacify(random.randint(3, 5) / 10)
            self.scrollingBG(RES.res.spr_back_2_boss_1, self.x_back_boss_1, 0, GameManager.CLIENT_WIDTH * 2,1200)
            RES.res.spr_back_2_boss_2.opacify(random.randint(5, 7) / 10)
            self.scrollingBG(RES.res.spr_back_2_boss_2, self.x_back_boss_2, 0, GameManager.CLIENT_WIDTH*2 ,1200)

        RES.res.spr_back_blackscreen.opacify(self.black_opac)
        RES.res.spr_back_blackscreen.draw(600, 384)

    def scrollingBG(self,img,x,y,width,height):
        img.clip_draw_to_origin(0, 0, width, height, x, y)
        if x < width:
            img.clip_draw_to_origin(0, 0, width, height, x - width,y)

    def pauseMusic(self):
        RES.res.snd_back_1.pause()

    def resumeMusic(self):
        RES.res.snd_back_1.resume()

class BKStage3(BackGround):
    pass
class BKStage4(BackGround):
    pass