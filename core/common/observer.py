from collections.abc import Callable


class Observer:
    def __init__(self):
        self.__events = {}

    def on(self, event: str, func: Callable):
        if event not in self.__events:
            self.__events[event] = []
        self.__events[event].append(func)
        return self

    def remove_listener(self, event: str, func: Callable):
        self.__events[event].remove(func)
        return self

    def emit(self, event: str, *arg, **kwargs):
        if event in self.__events:
            for func in self.__events[event]:
                func(self, *arg, **kwargs)
        return self