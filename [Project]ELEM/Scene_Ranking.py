from pico2d import *
import RES
import FrameWork
import Scene_Title
import GameManager
import math
import json
def bubble_sort(data):
    for i in range(0,len(data)):
        for j in range(i+1,len(data)):
            if data[i]['Score'] < data[j]['Score']:
                data[i], data[j] = data[j], data[i]


name = "RankingState"

startpos_y = 100
angle = 0

opacify = 0.5


def enter():
    pass

def exit():
    close_canvas()
    pass


def update():
    global startpos_y, angle, opacify

    angle = (angle+1) % 360

    startpos_y = 100 + math.sin(angle * math.pi / 180.0)*20
    opacify = 0.5 + math.sin(angle * math.pi / 180.0)*0.5
    pass


def draw():
    global startpos_y,opacify,angle
    clear_canvas()

    RES.res.spr_back_black.clip_draw_to_origin(0, 0, 64, 64, 0, 0, 1200, 800)

    RES.res.spr_back_rankpage.opacify(max(0.4,opacify))
    RES.res.spr_back_rankpage.draw(600- math.sin(angle * math.pi / 180.0)*50, 384)
    RES.res.spr_back_rankpage.opacify(opacify)
    RES.res.spr_back_rankpage.draw(600+ math.sin(angle * math.pi / 180.0)*50, 384)

    RES.res.spr_ranklens.draw(GameManager.CLIENT_WIDTH*0.5,GameManager.CLIENT_HEIGHT*0.5 )
    RES.res.spr_back_black.clip_draw_to_origin(0, 0, 64, 64, 0, 0, 200, 800)
    RES.res.spr_back_black.clip_draw_to_origin(0, 0, 64, 64, 1000, 0, 200, 800)

    RES.res.font_elem.draw(0, GameManager.CLIENT_HEIGHT - 25, " Press space to back ", (0, 255, 255))

    RES.res.font_elem.draw(600, 700, '[Play Record]', (255, 100, 100))

    f = open('Record.txt', 'r')
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)
    score_data = score_data[:10]

    y = 0
    for score in score_data:
        RES.res.font_elem.draw(400, 600 - y * 40, ' ::: Score : %3d ::: Remain Live : %3d ::: PlayTime : %4.1f' %
                  (score['Score'], score['Live'], score['PlayTime']),
                  (255, 255, 255))
        y += 1

    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            FrameWork.push_state(Scene_Title)
    pass


def pause():
    pass


def resume():
    pass
