from pico2d import *
import FrameWork
import GameManager
from BackGround import *
from obj_Bullet import *
from obj_Player import *

name = "MainState"

def enter():
    GameManager.buildgame()


def exit():
    close_canvas()


def update():
    GameManager.Player.update()

    for bullets in GameManager.p_bullet:
        bullets.update()

    for bullets in GameManager.p_bullet:
        if bullets.isout() is True:
            GameManager.p_bullet.remove(bullets)
    GameManager.background.update()
def draw():
    clear_canvas()

    GameManager.background.draw()

    GameManager.Player.draw()

    for bullets in GameManager.p_bullet:
        bullets.draw()

    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            GameManager.Player_Power += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
            GameManager.background.switch_uptosky = True
        else:
            GameManager.Player.handle_chara(event)

def pause():
    pass


def resume():
    pass
