from tkinter.font import Font
from .layer import Layer


class LabelView(Layer):
    def __init__(self, x, y, text):
        super().__init__(x, y)
        font = Font(family='微软雅黑', size=10, weight='bold')
        self.id = self.canvas.create_text(x, y, font=font, fill="white", text=text)

    def text(self, text):
        self.canvas.itemconfig(self.id, text=text)

    def destroy(self):
        self.canvas.delete(self.id)
