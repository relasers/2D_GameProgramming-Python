from pico2d import *


class Particle:
    opacify = 1
    MX_frame = 0
    img_frame = 0
    Fade_out = False
    def __init__(self,fadeout,size,zoommode,zoomsize):
        self.Fade_out = fadeout
        pass
    def isDestroy(self):
        if self.img_frame == self.MX_frame:
            return True
        if self.opacify < 0:
            return True


