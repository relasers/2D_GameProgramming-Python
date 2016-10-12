from pico2d import *
import FrameWork
import Scene_Title
import RES
name = "LogoState"
image = None
logo_time = 0.0

def enter():
    global image
    FrameWork.sprite = RES.Res()
    image = load_image('Resources/Images/BackGrounds/Main/Logo.png')
    pass


def exit():
    global image
    del(image)
    close_canvas()
    pass

def update():
    global logo_time

    if logo_time > 1.0 :
        logo_time = 0
        FrameWork.push_state(Scene_Title)

    logo_time += 0.01
    pass

def draw():
    global image
    clear_canvas()
    image.draw(600, 400)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass

def pause():
    pass

def resume():
    pass
