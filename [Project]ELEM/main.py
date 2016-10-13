from pico2d import *
from GameManager import *
import RES
import FrameWork

import Scene_Logo

open_canvas(CLIENT_WIDTH, CLIENT_HEIGHT)
RES.loading_data()
FrameWork.run(Scene_Logo)
