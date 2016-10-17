from pico2d import *
import FrameWork
import GameManager
from BackGround import *
from obj_Bullet import *
from obj_Player import *
from obj_enemy import *
from Timer import *
import random

name = "MainState"
def enter():
    # open_canvas(FrameWork.CLIENT_WIDTH,FrameWork.CLIENT_HEIGHT)
    GameManager.buildgame()
    pass


def exit():
    close_canvas()
    pass


def update():
    GameManager.timer.update()
    GameManager.Player.update()

    for bullets in GameManager.p_bullet:
        bullets.update()
    for bullets in GameManager.e_bullet:
        bullets.update()
    for bomb in GameManager.bomb:
        bomb.update()

    for enemys in GameManager.enemy:
        enemys.update()

    for bullets in GameManager.p_bullet:
        for enemys in GameManager.enemy:
            if bullets.isHit(enemys) is True and bullets.iscollisioned is False:
                enemys.HP -= bullets.Damage
                bullets.iscollisioned = True

    for bomb in GameManager.bomb:
        for enemys in GameManager.enemy:
            if bomb.isHit(enemys) is True:
                enemys.HP -= bomb.Damage


    for bullets in GameManager.e_bullet:
        if bullets.isHit(GameManager.Player) is True and bullets.HP > 0:
            GameManager.live -= 1
            bullets.HP -= 10
        if len(GameManager.bomb) > 0:
            if bullets.isHit(GameManager.bomb[0]) is True:
                bullets.HP -= 10




    for bullets in GameManager.p_bullet:
        if bullets.isDestroy() is True:
            GameManager.p_bullet.remove(bullets)
    for bullets in GameManager.e_bullet:
        if bullets.isDestroy() is True:
            GameManager.e_bullet.remove(bullets)

    for bomb in GameManager.bomb:
        if bomb.isDestroy() is True:
            GameManager.bomb.remove(bomb)

    for enemys in GameManager.enemy:
        if enemys.isDestroy() is True:
            if enemys.HP < 0:
                RES.res.snd_destroy.play()
            GameManager.enemy.remove(enemys)

    GameManager.background.update()
    pass


def draw():
    clear_canvas()

    GameManager.background.draw()

    for bullets in GameManager.p_bullet:
        bullets.draw()

    for enemys in GameManager.enemy:
        enemys.draw()

    for bomb in GameManager.bomb:
        bomb.draw()

    GameManager.Player.draw()

    for bullets in GameManager.e_bullet:
        bullets.draw()

    RES.res.font_elem.draw(0, 780, " PROJECT ELEM ",(255,0,255))
    RES.res.font_elem.draw(0, 750, " Live :: %s " % GameManager.live, (255, 0, 255))

    update_canvas()
    pass


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
            GameManager.background.state = (GameManager.background.state + 1 ) % 4
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p): # Toggle Collision Box
            GameManager.CollisionBox = not GameManager.CollisionBox
        else:
            GameManager.Player.handle_chara(event)
        pass

def pause():
    pass


def resume():
    pass
