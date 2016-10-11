from pico2d import *
import time

UPDATE_DELAY = 1.0 / 60.0

CLIENT_WIDTH = 1200
CLIENT_HEIGHT = 800
UI_SIZE = 64

running = None
stack = None


def change_stage(state):
    global stack
    pop_state()
    stack.append(state)
    state.enter()


def push_state(state):
    global stack
    if len(stack) > 0:
        stack[-1].pause()
    stack.append(state)
    state.enter()


def pop_state():
    global stack
    if len(stack) > 0:
        stack[-1].exit()
        stack.pop()

    if len(stack) > 0:
        stack[-1].resume()


def quit():
    global running
    running = False


def run(start_state):
    global running, stack
    running = True
    stack = [start_state]
    start_state.enter()
    current_time = time.clock()
    while running:
        if time.clock() - current_time > UPDATE_DELAY:
            current_time = time.clock()
            stack[-1].handle_events()
            stack[-1].update()
            stack[-1].draw()
    # repeatedly delete the top of the stack
    while len(stack) > 0:
        stack[-1].exit()
        stack.pop()