import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = 'C:\\Program Files\\Python35\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Program Files\\Python35\\tcl\\tk8.6'

executables = [cx_Freeze.Executable(script='main.py', icon='ELEM.ico')]

cx_Freeze.setup(
    name='Project ELEM',
    options={'build_exe': {'packages':['pico2d'],
                           'include_files':['./Resources/']}},
    executables = executables
)