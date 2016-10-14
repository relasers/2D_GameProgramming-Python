from pico2d import *
from obj_Bullet import *
from obj_Player import *
from BackGround import *

CLIENT_WIDTH = 1200
CLIENT_HEIGHT = 800
UI_SIZE = 48

CollisionBox = False

Player = None
background = None
p_bullet = []
e_bullet = []
enemy = []
live = 0
Player_Power = 0


def buildgame():
    global Player
    global p_bullet
    global e_bullet
    global enemy
    global live
    global Player_Power
    global background

    Player = Ruby(600, 600)
    background = BKStage1()
    p_bullet = []
    e_bullet = []
    enemy = []
    live = 3
    Player_Power = 0
