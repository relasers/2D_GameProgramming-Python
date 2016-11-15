from pico2d import *
import FrameWork
import GameManager
from BackGround import *
from obj_Bullet import *
from obj_Player import *
from obj_enemy import *
from obj_boss import *
from obj_Item import *

from Timer import *
import random

name = "MainState"
isPause = False
def enter():
    # open_canvas(FrameWork.CLIENT_WIDTH,FrameWork.CLIENT_HEIGHT)
    GameManager.buildgame()
    pass


def exit():
    close_canvas()
    pass


def update():
    if isPause is False:
        update_running()
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

    for item in GameManager.item:
        item.draw()

    for particles in GameManager.particle:
        particles.draw()

    GameManager.Player.draw()

    for bullets in GameManager.e_bullet:
        bullets.draw()

    RES.res.spr_UIbar.draw(GameManager.CLIENT_WIDTH / 2, GameManager.CLIENT_HEIGHT - GameManager.UI_SIZE/2)
    RES.res.spr_powerbar.clip_draw_to_origin(0, 128, 528, 64,
                                             GameManager.CLIENT_WIDTH / 2 - 250, GameManager.CLIENT_HEIGHT - 64)
    RES.res.spr_powerbar.clip_draw_to_origin(0, 64, min(528, (int)(GameManager.Player_Power*1.056) ), 64,
                                             GameManager.CLIENT_WIDTH / 2 - 250, GameManager.CLIENT_HEIGHT - 64)
    RES.res.spr_powerbar.clip_draw_to_origin(0, 0, 528, 64,
                                             GameManager.CLIENT_WIDTH / 2 - 250, GameManager.CLIENT_HEIGHT - 64)

    RES.res.font_elem.draw(0, GameManager.CLIENT_HEIGHT - 20, " Live :: %s " % GameManager.live, (255, 0, 0))
    RES.res.font_elem.draw(0, GameManager.CLIENT_HEIGHT - 50, " Bomb :: %s " % GameManager.curr_bomb, (0, 255, 255))

    RES.res.font_elem.draw(270, GameManager.CLIENT_HEIGHT - 32, " Power :: " , (255, 255-(int)(0.51*GameManager.Player_Power), 255-(int)(0.51*GameManager.Player_Power)))
    RES.res.font_elem.draw(GameManager.CLIENT_WIDTH / 2-16, GameManager.CLIENT_HEIGHT - 32, "  %0.2f " % GameManager.Player_Power,
                           (255, (int)(0.51*GameManager.Player_Power), (int)(0.51*GameManager.Player_Power)))
    RES.res.font_elem.draw(300, GameManager.CLIENT_HEIGHT - 80, " Timer :: %s " % GameManager.maintime, (155, 155, 155))
    RES.res.font_elem.draw(GameManager.CLIENT_WIDTH/2 + 300, GameManager.CLIENT_HEIGHT - 32, " Score :: %s " % GameManager.score, (155, 155, 155))
    if isPause is True:
        RES.res.spr_pause.draw(GameManager.CLIENT_WIDTH/2, GameManager.CLIENT_HEIGHT/2)

    update_canvas()
    pass


def handle_events():
    global isPause
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            GameManager.Player_Power = min(500,GameManager.Player_Power+100)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
            GameManager.background.state = (GameManager.background.state + 1 ) % 4
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_o): # Toggle Collision Box
            GameManager.CollisionBox = not GameManager.CollisionBox
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p): # Toggle Collision Box
            if isPause is False:
                pause()
            elif isPause is True:
                resume()
        else:
            if isPause is False:
                GameManager.Player.handle_chara(event)
        pass

def pause():
    global isPause
    GameManager.background.pauseMusic()
    isPause = True
    pass


def resume():
    global isPause
    GameManager.background.resumeMusic()
    isPause = False
    pass

def update_running():

    GameManager.timer.update()
    GameManager.Player.update()

    for bullets in GameManager.p_bullet:
        bullets.update()
    for bullets in GameManager.e_bullet:
        bullets.update()
    for bomb in GameManager.bomb:
        bomb.update()

    for item in GameManager.item:
        item.update()

    for enemys in GameManager.enemy:
        enemys.update()

    for particles in GameManager.particle:
        particles.update()

###################<Power_Limited_Time>#######################

    if 399 < GameManager.Player_Power:
        GameManager.Player_Power = max (399,GameManager.Player_Power - 0.2 )

####################<Collision Check>################################################################################

    for item in GameManager.item:
        if item.isHit(GameManager.Player) is True and item.HP > 0:
            item.KIA()
            item.HP -= 10

    for bullets in GameManager.p_bullet:
        for enemys in GameManager.enemy:
            if bullets.isHit(enemys) is True and bullets.iscollisioned is False:
                enemys.HP -= bullets.Damage
                Player_Power_Upgrade()
                GameManager.score += 1
                bullets.iscollisioned = True

    for bomb in GameManager.bomb:
        for enemys in GameManager.enemy:
            if bomb.isHit(enemys) is True:
                Player_Power_Upgrade()
                GameManager.score += 1
                enemys.HP -= bomb.Damage

    for bullets in GameManager.e_bullet:
        if bullets.isHit(GameManager.Player) is True and bullets.HP > 0:
            GameManager.live -= 1
            GameManager.Player_Power *= 0.75
            bullets.HP -= 10
        if len(GameManager.bomb) > 0:
            if bullets.isHit(GameManager.bomb[0]) is True:
                bullets.HP -= 10


#####################<Destroy Check>##########################################################################


    for bullets in GameManager.p_bullet:
        if bullets.isDestroy() is True:
            GameManager.p_bullet.remove(bullets)
    for bullets in GameManager.e_bullet:
        if bullets.isDestroy() is True:
            GameManager.e_bullet.remove(bullets)

    for item in GameManager.item:
        if item.isDestroy() is True:
            GameManager.item.remove(item)

    for bomb in GameManager.bomb:
        if bomb.isDestroy() is True:
            GameManager.bomb.remove(bomb)

    for enemys in GameManager.enemy:
        if enemys.isDestroy() is True:
            if enemys.HP < 0:
                RES.res.snd_destroy.play()
                GameManager.particle += [
                    ExplodeEnemy(0, enemys.SpriteID, enemys.point.x, enemys.point.y, True, enemys.Size, True, 0, 12, 1)]
                enemys.KIA()
            GameManager.enemy.remove(enemys)
            GameManager.score += 10

    for particles in GameManager.particle:
        if particles.isDestroy() is True:
            GameManager.particle.remove(particles)

###################<BackGround Update>##################################################################

    GameManager.background.update()

#################<timer Update>##############################################################################
    GameManager.maintime += 1

def Player_Power_Upgrade():
    if GameManager.Player_Power < 100:
        GameManager.Player_Power = min(500, GameManager.Player_Power + 2)
    elif 100 <= GameManager.Player_Power < 200:
        GameManager.Player_Power = min(500, GameManager.Player_Power + 0.5)
    elif 200 <= GameManager.Player_Power < 300:
        GameManager.Player_Power = min(500, GameManager.Player_Power + 0.25)
    else:
        GameManager.Player_Power = min(500, GameManager.Player_Power + 0.1)