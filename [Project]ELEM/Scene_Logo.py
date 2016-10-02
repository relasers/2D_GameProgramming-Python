from pico2d import *
import FrameWork
import Scene_Title

name = "LogoState"
image = None
logo_time = 0.0

def enter():
    global image
    open_canvas(1200, 800)
    image = load_image('Resources/Images/BackGrounds/Main/Logo.png')


def exit():
    global image
    del(image)
    close_canvas()

def update():
    global logo_time

    if logo_time > 1.0 :
        logo_time = 0
        FrameWork.push_state(Scene_Title)

    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(600, 400)
    update_canvas()

def handle_events():
    events = get_events()
    pass

def pause():
    pass

def resume():
    pass
