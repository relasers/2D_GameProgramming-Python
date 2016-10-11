from obj_Bullet import *
from obj_Player import *


Player = None
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

    Player = Ruby(600, 600)
    p_bullet = []
    enemy = []
    live = 3
    Player_Power = 0

