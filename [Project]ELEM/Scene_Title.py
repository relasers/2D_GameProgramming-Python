from pico2d import *
import FrameWork
import Scene_MainGame

name = "TitleState"

def enter():
    pass

def exit():
    close_canvas()


def update():
    FrameWork.push_state(Scene_MainGame)


def draw():
    clear_canvas()
    update_canvas()


def handle_events():
    events = get_events()


def pause():
    pass


def resume():
    pass
