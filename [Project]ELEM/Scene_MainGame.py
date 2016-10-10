from pico2d import *
import FrameWork
from obj_Bullet import *
from obj_Player import *

name = "MainState"
ruby = None
p_bullet = []

def enter():
    global ruby
    open_canvas(FrameWork.CLIENT_WIDTH, FrameWork.CLIENT_HEIGHT)
    ruby = Ruby(600, 600)


def exit():
    close_canvas()


def update():
    global p_bullet
    if ruby.update() is True:
        p_bullet += [ruby.shoot()]
    for bullets in p_bullet:
        bullets.update()

def draw():
    global p_bullet
    clear_canvas()
    ruby.draw()

    for bullets in p_bullet:
        bullets.draw()

    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            FrameWork.quit()
        else:
            ruby.handle_chara(event)

def pause():
    pass


def resume():
    pass
