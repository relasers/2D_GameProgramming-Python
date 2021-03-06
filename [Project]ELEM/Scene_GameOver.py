from pico2d import *
import RES
import FrameWork
import Scene_Title
import math
name = "TitleState"

startpos_y = 100
angle = 0

opacify = 0.5


def enter():
    RES.res.snd_gameover.set_volume(128)
    RES.res.snd_gameover.repeat_play()

    pass

def exit():
    pass


def update():
    global startpos_y, angle, opacify

    angle = (angle+1) % 360

    startpos_y = 100 + math.sin(angle * math.pi / 180.0)*20
    opacify = 0.5 + math.sin(angle * math.pi / 180.0)*0.5
    pass


def draw():
    global startpos_y,opacify
    clear_canvas()

    RES.res.spr_back_black.clip_draw_to_origin(0, 0, 64, 64, 0, 0, 1200, 800)

    RES.res.spr_back_gameover_gray.opacify(max(0.4,opacify))
    RES.res.spr_back_gameover_gray.draw(600, 384)
    RES.res.spr_back_gameover.opacify(opacify)
    RES.res.spr_back_gameover.draw(600, 384)

    RES.res.spr_press_backto.opacify(opacify)
    RES.res.spr_press_backto.draw(600, (int)(startpos_y) )

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
