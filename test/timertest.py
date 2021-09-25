import time
import sys
from core.common import Timer, TimerEvent

if __name__ == '__main__':
    timer = Timer(3)
    timer. \
        on(TimerEvent.Tick, lambda s: print("tick--")). \
        on(TimerEvent.Exit, lambda s: print("exit--"))
    timer.start()
    time.sleep(2)
    print("stop")
    timer.stop()

