from pico2d import *
import FrameWork
import GameManager
from BackGround import *
from obj_Bullet import *
from obj_Player import *
from obj_enemy import *
import random

name = "MainState"
time = 0
def enter():
    # open_canvas(FrameWork.CLIENT_WIDTH,FrameWork.CLIENT_HEIGHT)
    GameManager.buildgame()
    pass


def exit():
    close_canvas()
    pass


def update():
    global time
    time += 1
    if time > 100:
        GameManager.enemy += [
            Enemy64(2, GameManager.CLIENT_WIDTH,random.randint(0,GameManager.CLIENT_HEIGHT-GameManager.UI_SIZE),180,0,20,-0.25),
            Enemy_spiral(3, GameManager.CLIENT_WIDTH,
                    random.randint(0, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE), 180, 0, 10, -0.1)
        ]
        time = 0
    GameManager.Player.update()

    for bullets in GameManager.p_bullet:
        bullets.update()
    for bullets in GameManager.e_bullet:
        bullets.update()
    for enemys in GameManager.enemy:
        enemys.update()


    for bullets in GameManager.p_bullet:
        for enemys in GameManager.enemy:
            if bullets.isHit(enemys) is True and bullets.iscollisioned is False:
                enemys.HP -= bullets.Damage
                GameManager.p_bullet.remove(bullets)


    for bullets in GameManager.e_bullet:
        if bullets.isHit(GameManager.Player) is True:
            GameManager.e_bullet.remove(bullets)

    for enemys in GameManager.enemy:
        if enemys.isDestroy() is True:
            GameManager.enemy.remove(enemys)
    for bullets in GameManager.p_bullet:
        if bullets.isDestroy() is True:
            GameManager.p_bullet.remove(bullets)
    for bullets in GameManager.e_bullet:
        if bullets.isDestroy() is True:
            GameManager.e_bullet.remove(bullets)

    GameManager.background.update()
    pass


def draw():
    clear_canvas()



    GameManager.background.draw()

    for bullets in GameManager.p_bullet:
        bullets.draw()

    for enemys in GameManager.enemy:
        enemys.draw()

    GameManager.Player.draw()

    for bullets in GameManager.e_bullet:
        bullets.draw()

    RES.res.font_elem.draw(0, 780, " PROJECT ELEM ",(255,0,255))

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
