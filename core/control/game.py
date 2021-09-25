from ..gui.view import DiamondView
from ..service import LogicService
from ..common import KeyMapper, Context
from ..common import Timer, TimerEvent
import threading
import time


class GameControl:
    def __init__(self):
        self.win = Context.get_module("core.gui.tetriswin.TetrisWin")
        self.logic: LogicService = Context.get_module("core.service.logic.LogicService")
        self.keymapper = Context.get_module("core.common.keymapper.KeyMapper")
        self.diamond: DiamondView = Context.get_module("core.gui.view.diamond.DiamondView")
        self.win.canvas.bind_all('<KeyPress>', self.keypress)
        self.win.on("beforeclose", self.beforeclose)
        self.timer = Timer(4)
        self.lock = threading.Lock()

    def start(self):
        self.timer.on(TimerEvent.Tick, self.tick)
        self.timer.on(TimerEvent.Exit, self.close)
        self.timer.start()

    def close(self, source):
        self.win.exit()

    def beforeclose(self, source):
        self.timer.stop()

    def tick(self, source):
        self.lock.acquire()
        self.move_down()
        # time.sleep(0.4)
        self.lock.release()

    def create_block(self):
        # self.logic.create_block()
        # self.win.create_block()
        pass

    def keypress(self, event):
        self.keymapper(event)

    def rotate(self):
        if self.logic.can_rotate():
            self.logic.rotate()
            self.diamond.rotate()

    def move_up(self):
        if self.logic.can_move(0, -1):
            self.diamond.move(0, -1)

    def move_down(self):
        if self.logic.can_move(0, 1):
            self.diamond.move(0, 1)

    def move_down_fast(self):
        while self.logic.can_move(0, 1):
            self.diamond.move(0, 1)

    def move_left(self):
        if self.logic.can_move(-1, 0):
            self.diamond.move(-1, 0)

    def move_right(self):
        if self.logic.can_move(1, 0):
            self.diamond.move(1, 0)
