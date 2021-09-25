import threading
import time
from .observer import Observer


class TimerEvent:
    Start = "start"
    Tick = "tick"
    Exit = "exit"


class Timer(Observer):
    """
    given number of seconds.  The argument may be
    a floating point number for subsecond precision
    """

    def __init__(self, frame: float):
        super().__init__()
        self.running = False
        self.seconds = 1 / frame
        self.thread = threading.Thread(target=self, args=())

    def __call__(self, *args, **kwargs):
        while self.running:
            self.emit(TimerEvent.Tick)
            time.sleep(self.seconds)
        self.emit(TimerEvent.Exit)

    def is_alive(self):
        return self.thread.isAlive()

    def start(self):
        if self.running:
            return
        self.running = True
        self.emit(TimerEvent.Start)
        self.thread.start()

    def stop(self):
        self.running = False
