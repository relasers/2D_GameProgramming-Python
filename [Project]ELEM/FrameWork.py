import time

UPDATE_DELAY = 1.0 / 60.0

running = None
stack = None


class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw


def change_stage(state):
    global stack
    pop_state()
    stack.append(state)
    state.enter()


def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()


def pop_state():
    # 현재 스택을 날린다.
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit() # 현재 스택의 exit 를 실행
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
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
    # 리스트에서의 마지막 :: top
    # repeatedly delete the top of the stack
    while len(stack) > 0:
        stack[-1].exit()
        stack.pop()