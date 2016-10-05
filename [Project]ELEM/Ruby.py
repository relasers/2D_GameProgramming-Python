from pico2d import *
from Player import *
import random

class Ruby(Player):
    image = None

    def __init__(self, point_x, point_y):
        self.point = Vec2D(point_x, point_y)
        self.frame = random.randint(0, 4)
        if Ruby.image == None:
            Ruby.image = load_image('Resources/images/Characters/Ally/Ruby_set.png')

    def draw(self):
        self.image.clip_draw(self.frame * 64, 0, 64, 64, self.point.x, self.point.y)

    def update(self):
        self.frame = (self.frame + 1) % 4
