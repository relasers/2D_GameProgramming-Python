from pico2d import *
import FrameWork
import Scene_MainGame

name = "TitleState"

def enter():
    # open_canvas(FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT)
    pass

def exit():
    close_canvas()
    pass


def update():
    FrameWork.push_state(Scene_MainGame)
    pass


def draw():
    clear_canvas()
    update_canvas()
    pass


def handle_events():
    events = get_events()
    pass


def pause():
    pass


def resume():
    pass
