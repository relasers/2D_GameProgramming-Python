from pico2d import *
from obj_Bullet import *
from obj_Player import *
from BackGround import *
from Timer import *
import json

CLIENT_WIDTH = 1200
CLIENT_HEIGHT = 768
UI_SIZE = 64

CollisionBox = False

Player = None
background = None
timer = None
p_bullet = []
e_bullet = []
bomb = []
enemy = []
item = []
particle = []
GameClear = False

live = 0
curr_bomb = 0
Player_Power = 0.0
maintime = 0
total_time = 0
score = 0
DEBUG_MODE = False

def buildgame():
    global Player
    global p_bullet
    global e_bullet
    global bomb
    global enemy
    global item
    global live
    global curr_bomb
    global Player_Power
    global background
    global timer
    global particle
    global maintime
    global total_time
    global score
    global DEBUG_MODE
    global GameClear

    Player = Ruby(600, 600)
    background = BKStage1()
    timer = T_Stage1()
    p_bullet = []
    e_bullet = []
    bomb = []

    enemy = []
    item = []
    particle = []

    f = open('GameInit.txt', 'r')
    init_data = json.load(f)
    f.close()

    live = init_data['StartLive']
    curr_bomb = init_data['Bomb']
    if init_data['DebugMode'] == 1:
        DEBUG_MODE = True
    else:
        DEBUG_MODE = False
    Player_Power = 0
    maintime = 0
    total_time = 0
    score = 0

    GameClear = False