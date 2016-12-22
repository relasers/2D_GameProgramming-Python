from pico2d import *
import FrameWork
import Scene_Title
import RES
name = "LogoState"
image = None
logo_time = 0.0

blackopacify = 1.0
warpopacify = 1.0
profileopacify = 1.0


def enter():
    pass


def exit():
    pass

def update():
    global logo_time
    global blackopacify, warpopacify, profileopacify

    if 1.5 > logo_time > 0.0:
        blackopacify = max(0, blackopacify - 0.01)
    if logo_time > 1.5:
        warpopacify = max(0, warpopacify - 0.01)
    if logo_time > 3.0:
        blackopacify = min(1, blackopacify + 0.01)
    if logo_time > 4.0:
        logo_time = 0
        FrameWork.push_state(Scene_Title)
    logo_time += 0.01
    pass

def draw():
    global blackopacify, warpopacify, profileopacify

    clear_canvas()

    RES.res.spr_back_blackscreen.opacify(blackopacify)
    RES.res.spr_back_logo.opacify(warpopacify)
    RES.res.spr_back_profile.opacify(profileopacify)

    RES.res.spr_back_profile.draw(600, 384)
    RES.res.spr_back_logo.draw(600, 384)
    RES.res.spr_back_blackscreen.draw(600, 384)

    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass

def pause():
    pass

def resume():
    pass
