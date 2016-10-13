from pico2d import *
import FrameWork
import Scene_Title
import RES
name = "LogoState"
image = None
logo_time = 0.0
opacify = 0

def enter():
    global image
    image = load_image('Resources/Images/BackGrounds/Main/Logo.png')
    pass


def exit():
    global image
    del(image)
    close_canvas()
    pass

def update():
    global logo_time
    global opacify

    if logo_time > 1.0 :
        logo_time = 0
        FrameWork.push_state(Scene_Title)

    opacify += 0.1
    logo_time += 0.01
    pass

def draw():
    global image
    global opacify

    clear_canvas()

    image.opacify(opacify)
    image.clip_draw_to_origin(0,0,1200,800,0, 0)

    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass

def pause():
    pass

def resume():
    pass
