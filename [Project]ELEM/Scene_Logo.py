from pico2d import *
import FrameWork
import Scene_Title
import RES
name = "LogoState"
image = None
logo_time = 0.0
opacify = 1.0

def enter():
    pass


def exit():
    pass

def update():
    global logo_time
    global opacify

    if logo_time > 1.0 :
        logo_time = 0
        FrameWork.push_state(Scene_Title)

    opacify -= 0.01
    logo_time += 0.01
    pass

def draw():
    global opacify

    clear_canvas()
    RES.res.spr_back_blackscreen.opacify(opacify)
    RES.res.spr_back_blackscreen.draw(600,384)
    #RES.res.spr_back_logo.opacify(opacify)
    #RES.res.spr_back_logo.clip_draw_to_origin(0,0,1200,800,0, 0)
    RES.res.spr_back_logo.draw(600,400)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass

def pause():
    pass

def resume():
    pass
