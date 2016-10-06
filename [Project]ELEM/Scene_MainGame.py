from pico2d import *
import FrameWork
from Ruby import *

name = "MainState"
ruby = None

def enter():
    global ruby
    open_canvas(1200, 800)
    ruby = Ruby(600, 600)

def exit():
    close_canvas()


def update():
    ruby.update()
    pass


def draw():
    clear_canvas()
    ruby.draw()
    update_canvas()


def handle_events():
    events = get_events()


def pause():
    pass


def resume():
    pass
