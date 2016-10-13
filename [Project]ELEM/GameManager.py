from pico2d import *
from obj_Bullet import *
from obj_Player import *
from BackGround import *

CLIENT_WIDTH = 1200
CLIENT_HEIGHT = 800
UI_SIZE = 64

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


def calcangle(cx, cy, tx, ty):
    #  center point ~ target point
    return math.atan2(ty - cy, tx - cx) * math.pi / 180
