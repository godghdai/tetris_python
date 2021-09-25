import os

from .common import Config, KeyMapper, Context, ImageManger
from .service import LogicService
from .gui import TetrisWin
from .control import GameControl
import signal


class App:
    singleton = None

    def __init__(self):
        self.context = Context.get_instance()

        self.config = Config()
        self.context.register(self.config)

        keymapper = KeyMapper()
        self.context.register(keymapper)

        imagemanger = ImageManger(os.path.join(os.getcwd(), "resource"))
        self.context.register(imagemanger)

        self.win = TetrisWin()
        self.context.register(self.win)

        self.context.register(LogicService())
        self.control = GameControl()
        keymapper.bind(self.config.keymapper, self.control)

        self.context.register(self.control)

        self.control.start()

    def run(self):
        bind_signal()
        self.win.show()


def bind_signal():
    # interrupt(Ctrl+C中断)
    signal.signal(signal.SIGINT, exit_gracefully)
    # Software termination signal from kill(Kill发出的软件终止)
    signal.signal(signal.SIGTERM, exit_gracefully)
    # signal.signal(signal.SIGKILL, exit_gracefully)
    # signal.signal(signal.SIGHUP, exit_gracefully)


def exit_gracefully(signum, frame):
    global is_exit
    is_exit = True
    print("receive a signal %d, is_exit = %d" % (signum, is_exit))
