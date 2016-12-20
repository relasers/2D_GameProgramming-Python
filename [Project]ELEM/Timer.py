import GameManager
from obj_enemy import *
from obj_boss import *
import random

class Timer:
    PHASE_1, PHASE_2 = 0, 1
    t_frame = 0
    t_phase_frame = 0
    state = 0
    counter = 0

    isDebug = False


class T_Stage1(Timer):
    PHASE_1, PHASE_2, PHASE_3, PHASE_4,PHASE_5 = 0, 1, 2, 3,4
    PHASE_6, PHASE_7, PHASE_8 = 5,6,7

    t_frame = 0
    t_phase_frame = 0
    state = 0
    counter = 0

    def __init__(self):
        self.t_frame = 0
        self.state = self.PHASE_1
    pass

    def handle_phase_1(self):


        if self.isDebug is True:
            if self.t_frame == 10:
                GameManager.enemy += [
                    Plask(GameManager.CLIENT_WIDTH, (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE)/2,
                            180, 0, 7, -0.1)
                ]


        else:

            if self.t_frame < 900:
                if self.t_phase_frame % 60 == 0:
                    GameManager.enemy += [
                        Enemy64(0, GameManager.CLIENT_WIDTH, random.randint(0, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE),
                            180, 0, 10, -0.1),
                ]
            elif 900 < self.t_frame:
                if self.t_phase_frame % 16 == 0:
                    GameManager.enemy += [
                    Enemy64(2, GameManager.CLIENT_WIDTH, random.randint(0, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE),
                            180, 0, 10, -0.1),
                ]
            if self.t_frame > 1600:
                self.t_phase_frame = 349
                self.state = self.PHASE_2

    def handle_phase_2(self):
        if self.t_phase_frame % 350 == 0:
            GameManager.enemy += [
                Enemy_spiral(3, GameManager.CLIENT_WIDTH,
                             300, 180, 0, 5, -0.02, False),
                Enemy_spiral(3, GameManager.CLIENT_WIDTH,
                             600, 180, 0, 5, -0.02, False)
            ]
        if self.t_frame > 2300:
            self.t_phase_frame = 49
            self.state = self.PHASE_3

    def handle_phase_3(self):
        if self.t_phase_frame % 20 == 0:
            GameManager.enemy += [
                Enemy_Gorgon(1, GameManager.CLIENT_WIDTH,
                             random.randint(0, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE*3), 180, 0, 10, -0.1)
            ]
        if self.t_frame > 3270:
            self.t_phase_frame = 49
            self.state = self.PHASE_4
    def handle_phase_4(self):
        if self.t_phase_frame % 25 == 0:
            GameManager.enemy += [
                Enemy_Rounder(4, GameManager.CLIENT_WIDTH,
                              (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE)/2+random.randint(-250,250), 180, 0, 10, -0.1,random.randint(0,1)),
            ]
            if self.t_frame > 4450:
                self.t_phase_frame = 499
                self.state = self.PHASE_5

    def handle_phase_5(self):
        if self.t_phase_frame == 500:
            GameManager.enemy += [
                Enemy_fairy(0, GameManager.CLIENT_WIDTH,
                         (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE) / 2, 180, 0, 10,
                         -0.1, True)
            ]
        if self.t_frame > 5200:
            self.t_phase_frame = 29
            self.state = self.PHASE_6

    def handle_phase_6(self):

        if self.t_phase_frame % 30 == 0:

            GameManager.enemy += [
                Enemy_Linear(1, GameManager.CLIENT_WIDTH,
                             max(10,GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE - self.counter*30),
                             180, 0, 10, -0.1),
            ]

            self.counter += 1

            if self.t_frame > 5600:
                GameManager.enemy += [
                    Enemy_shotgun(0, GameManager.CLIENT_WIDTH,
                                  random.randint(0, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE),
                                  180, 0, 10, -0.1),
                ]




        if self.t_frame > 5800:
            self.t_phase_frame = 499
            self.state = self.PHASE_7

        pass
    def handle_phase_7(self):
        if self.t_phase_frame == 500:

            for i in range(6):
                GameManager.enemy += [
            Enemy_stright_spr(2, GameManager.CLIENT_WIDTH,
                          (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE)/2 - i*50,
                          180, 0, 3+i, -0.1),
            ]
            for i in range(6):
                GameManager.enemy += [
                    Enemy_stright_spr(2, GameManager.CLIENT_WIDTH,
                                          (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE) / 2 + i * 50,
                                          180, 0, 3 + i, -0.1),
                    ]


        if self.t_frame > 6000:
            self.t_phase_frame = 0
            GameManager.particle += [
                Warning(0, 0, 0, 0, True, 0, True, 0, 12, 1)]
            self.state = self.PHASE_8
        pass
    def handle_phase_8(self):
        if self.t_phase_frame == 500:
            GameManager.enemy += [
            Plask(GameManager.CLIENT_WIDTH, (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE) / 2,
                  180, 0, 7, -0.1)
        ]
        pass

    handle_state = {
        PHASE_1: handle_phase_1,
        PHASE_2: handle_phase_2,
        PHASE_3: handle_phase_3,
        PHASE_4: handle_phase_4,
        PHASE_5: handle_phase_5,
        PHASE_6: handle_phase_6,
        PHASE_7: handle_phase_7,
        PHASE_8: handle_phase_8
    }

    def update(self):
        self.t_frame += 1
        self.t_phase_frame += 1
        self.handle_state[self.state](self)

    def CreateNormalEnemy(self):
        pass


class T_Stage2(Timer):
    PHASE_1, PHASE_2, PHASE_3, PHASE_4,PHASE_5 = 0, 1, 2, 3,4
    PHASE_6, PHASE_7, PHASE_8 = 5,6,7

    t_frame = 0
    t_phase_frame = 0
    state = 0
    counter = 0

    def __init__(self):
        self.t_frame = 0
        self.state = self.PHASE_1

    pass

    def handle_phase_1(self):


        if self.isDebug is True:
            if self.t_frame == 10:
                GameManager.enemy += [
                    Plask(GameManager.CLIENT_WIDTH, (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE)/2,
                            180, 0, 7, -0.1)
                ]


        else:

            if self.t_frame < 900:
                if self.t_phase_frame % 60 == 0:
                    GameManager.enemy += [
                        Enemy64(0, GameManager.CLIENT_WIDTH, random.randint(0, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE),
                            180, 0, 10, -0.1),
                ]
            elif 900 < self.t_frame:
                if self.t_phase_frame % 16 == 0:
                    GameManager.enemy += [
                    Enemy64(2, GameManager.CLIENT_WIDTH, random.randint(0, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE),
                            180, 0, 10, -0.1),
                ]
            if self.t_frame > 1600:
                self.t_phase_frame = 349
                self.state = self.PHASE_2

    def handle_phase_2(self):
        if self.t_phase_frame % 350 == 0:
            GameManager.enemy += [
                Enemy_spiral(3, GameManager.CLIENT_WIDTH,
                             300, 180, 0, 5, -0.02, False),
                Enemy_spiral(3, GameManager.CLIENT_WIDTH,
                             600, 180, 0, 5, -0.02, False)
            ]
        if self.t_frame > 2300:
            self.t_phase_frame = 49
            self.state = self.PHASE_3

    def handle_phase_3(self):
        if self.t_phase_frame % 20 == 0:
            GameManager.enemy += [
                Enemy_Gorgon(1, GameManager.CLIENT_WIDTH,
                             random.randint(0, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE*3), 180, 0, 10, -0.1)
            ]
        if self.t_frame > 3270:
            self.t_phase_frame = 49
            self.state = self.PHASE_4
    def handle_phase_4(self):
        if self.t_phase_frame % 25 == 0:
            GameManager.enemy += [
                Enemy_Rounder(4, GameManager.CLIENT_WIDTH,
                              (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE)/2+random.randint(-250,250), 180, 0, 10, -0.1,random.randint(0,1)),
            ]
            if self.t_frame > 4450:
                self.t_phase_frame = 499
                self.state = self.PHASE_5

    def handle_phase_5(self):
        if self.t_phase_frame == 500:
            GameManager.enemy += [
                Enemy_fairy(0, GameManager.CLIENT_WIDTH,
                         (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE) / 2, 180, 0, 10,
                         -0.1, True)
            ]
        if self.t_frame > 5200:
            self.t_phase_frame = 29
            self.state = self.PHASE_6

    def handle_phase_6(self):

        if self.t_phase_frame % 30 == 0:

            GameManager.enemy += [
                Enemy_Linear(1, GameManager.CLIENT_WIDTH,
                             max(10,GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE - self.counter*30),
                             180, 0, 10, -0.1),
            ]

            self.counter += 1

            if self.t_frame > 5600:
                GameManager.enemy += [
                    Enemy_shotgun(0, GameManager.CLIENT_WIDTH,
                                  random.randint(0, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE),
                                  180, 0, 10, -0.1),
                ]




        if self.t_frame > 5800:
            self.t_phase_frame = 499
            self.state = self.PHASE_7

        pass
    def handle_phase_7(self):
        if self.t_phase_frame == 500:

            for i in range(6):
                GameManager.enemy += [
            Enemy_stright_spr(2, GameManager.CLIENT_WIDTH,
                          (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE)/2 - i*50,
                          180, 0, 3+i, -0.1),
            ]
            for i in range(6):
                GameManager.enemy += [
                    Enemy_stright_spr(2, GameManager.CLIENT_WIDTH,
                                          (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE) / 2 + i * 50,
                                          180, 0, 3 + i, -0.1),
                    ]


        if self.t_frame > 6800:
            self.t_phase_frame = 0
            GameManager.particle += [
                Warning(0, 0, 0, 0, True, 0, True, 0, 12, 1)]
            self.state = self.PHASE_8
        pass
    def handle_phase_8(self):
        if self.t_phase_frame == 1850:
            GameManager.enemy += [
            Plask(GameManager.CLIENT_WIDTH, (GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE) / 2,
                  180, 0, 7, -0.1)
        ]
        pass

    handle_state = {
        PHASE_1: handle_phase_1,
        PHASE_2: handle_phase_2,
        PHASE_3: handle_phase_3,
        PHASE_4: handle_phase_4,
        PHASE_5: handle_phase_5,
        PHASE_6: handle_phase_6,
        PHASE_7: handle_phase_7,
        PHASE_8: handle_phase_8
    }

    def update(self):
        self.t_frame += 1
        self.t_phase_frame += 1
        self.handle_state[self.state](self)

    def CreateNormalEnemy(self):
        pass