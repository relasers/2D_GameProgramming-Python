from pico2d import *

import Scene_Logo
import Scene_Stage_1
import Scene_Stage_2
import Scene_GameOver

open_canvas()


class FrameWork:
    UPDATE_DELAY = 0.016

    def change_stage(self, state):
        global stack
        self.pop_state()
        state.append(state)
        state.enter()

    def push_state(self, state):
        global stack
        if len(stack) > 0 :
            stack[-1].pause()
        stack.append(state)
        state.enter()

    def pop_state(self):
        global stack
        if len(stack) > 0 :
            stack[-1].exit()
            stack.pop()
        if len(stack) > 0 :
            stack[-1].resume()

    def quit(self):
        global running
        running False

    def run(self,start_state):
        global running, stack
        running = True
        stack = [start_state]
        start_state.enter()
        while running :
            stack[-1].handle_events()
            stack[-1].update()
            stack[-1].draw()
        # repeatedly delete the top of the stack
        while len(stack) > 0 :
            stack[-1].exit()
            stack.pop()