from ...common import Observer, Context, Config
from tkinter import Canvas


class Layer(Observer):

    def __init__(self, x, y, **kwargs):
        super().__init__()
        self.x = x
        self.y = y
        self.ctx: Context = Context.get_instance()
        self.canvas: Canvas
        if "canvas" in kwargs:
            self.canvas: Canvas = kwargs.get("canvas")
        else:
            self.canvas: Canvas = self.ctx.get_module("tkinter.Canvas")
