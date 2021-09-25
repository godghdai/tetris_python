import threading
import time

stop = False


def dowork(*args, **kwargs):
    i = 1
    while not stop:
        print(i)
        time.sleep(0.5)
        i += 1


thread = threading.Thread(target=dowork, args=(1, 2))
thread.start()
time.sleep(2)
stop = True
while thread.isAlive():
    time.sleep(1)
print(thread.isAlive())
print("exit")
