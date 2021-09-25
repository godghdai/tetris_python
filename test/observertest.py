from core.common import Observer

if __name__ == '__main__':
    obs = Observer()
    pp = lambda source, x, y: print(x + "---", y)
    obs.on("model", lambda source, x, y: print(x, y))
    obs.on("model", pp)
    obs.emit("model", "hello", "world")
    obs.remove_listener("model", pp)
    obs.emit("model", "hello", "world")
