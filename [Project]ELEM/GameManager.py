from pico2d import *
from obj_Bullet import *
from obj_Player import *
from BackGround import *

Player = None
background = None
p_bullet = []
enemy = []
live = 0
Player_Power = 0


def buildgame():
    global Player
    global p_bullet
    global enemy
    global live
    global Player_Power
    global background

    Player = Ruby(600, 600)
    background = BKStage1()
    p_bullet = []
    enemy = []
    live = 3
    Player_Power = 0
