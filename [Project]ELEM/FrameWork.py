from pico2d import *

open_canvas()

UPDATE_DELAY = 0.016

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
    while running:
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
    # repeatedly delete the top of the stack
    while len(stack) > 0:
        stack[-1].exit()
        stack.pop()