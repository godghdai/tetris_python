from .layer import Layer
from ...common import ImageManger


class IndicatorView(Layer):
    TAG = ("__indicator",)

    def bak(self):
        self.id = self.canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height,
            outline="blue",
            tag=self.TAG
        )

    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = int(width)
        self.height = int(height)
        self.photo = None
        self.id = self.canvas.create_image(x, y, image=self.photo, anchor="nw")
        self.image_manger: ImageManger = self.ctx.get_module("core.common.imagemanger.ImageManger")
        self.update_image()

    def update_image(self):
        self.photo = self.image_manger.get_image(
            ImageManger.INDICATOR,
            self.width, self.height + 4
        )

    def update(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = int(width)
        self.height = int(height)
        self.update_image()
        self.canvas.itemconfig(self.id, image=self.photo)
        self.canvas.coords(self.id, x, y)

    def destroy(self):
        self.canvas.delete(self.id)
