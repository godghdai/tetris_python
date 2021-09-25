class KeyMapper:
    def __init__(self):
        self.keymap = None
        self.key_callable = None

    def bind(self, keymap, obj):
        if keymap is None or obj is None:
            return
        self.keymap = keymap
        self.key_callable = {}
        for key, value in self.keymap.items():
            if not hasattr(obj, value):
                raise Exception("The {}  has no attribute [ {} ]!!".format(type(obj), value))
            attr = getattr(obj, value)
            if not callable(attr):
                raise Exception("The {} has a [ {} ] attribute is not callable!!".format(type(obj), value))
            self.key_callable[key] = attr

    def __call__(self, event):
        if event.keysym not in self.keymap:
            return
        self.key_callable[event.keysym]()
