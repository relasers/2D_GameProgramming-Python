
import platform
import os



if platform.architecture()[0] == '32bit' :
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"




from pico2d import *
from GameManager import *
import RES
import FrameWork

import Scene_Logo

open_canvas(CLIENT_WIDTH, CLIENT_HEIGHT)
RES.loading_data()
FrameWork.run(Scene_Logo)
