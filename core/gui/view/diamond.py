from .layer import Layer
import sys
import random
from ...common import Context, Config


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.id = -1


class DiamondView(Layer):
    GROUP_TAG = ("__diamond",)

    def __init__(self, x, y, parent):
        super().__init__(parent.x + x, parent.y + y)
        self.parent = parent
        self.border_color = "white"
        self.fill_color = "blue"
        self.type = None
        self.isCanRotate = False
        self.cells = []
        self.center_x = -1
        self.center_y = -1
        self.width = -1
        self.min_x = -1

    def _init(self, block_json):
        self.type = block_json["type"]
        self.isCanRotate = bool(block_json["rotate"])
        data = block_json["data"]
        for row in range(len(data)):
            for col in range(len(data[0])):
                if data[row][col] == 0:
                    continue
                self.cells.append(Cell(col, row))
                if data[row][col] == 8:
                    self.center_x = col
                    self.center_y = row

    def _create_diamond(self):
        size = self.parent.size
        for cell in self.cells:
            x = self.x + cell.x * size + 1
            y = self.y + cell.y * size + 1
            cell.id = self.canvas.create_rectangle(
                x, y, x + size - 2, y + size - 2,
                outline=self.border_color,
                fill=self.fill_color, tag=self.GROUP_TAG)
        self.update_width()

    @classmethod
    def create(cls, x, y, parent, block_json):
        view = DiamondView(x, y, parent)
        view._init(block_json)
        colors = Context.get_config().colors
        index = random.randint(0, len(colors) - 1)
        view.border_color = colors[index]["border"]
        view.fill_color = colors[index]["fill"]
        view._create_diamond()
        return view

    def rotate(self):
        size = self.parent.size
        for cell in self.cells:
            x = self.x + cell.x * size + 1
            y = self.y + cell.y * size + 1
            self.canvas.coords(cell.id, x, y, x + size - 2, y + size - 2)
        self.update_width()

    def move(self, dx, dy):
        size = self.parent.size
        # for index, id in enumerate(self.canvas.find_withtag('diamond')):
        self.canvas.move(self.GROUP_TAG, dx * size, dy * size)
        self.x += dx * size
        self.y += dy * size
        self.update_width()

    def update_width(self):
        rx, lx = -1, sys.maxsize
        size = self.parent.size
        for cell in self.cells:
            x = self.x + cell.x * size
            rx = max(rx, x)
            lx = min(lx, x)
        self.min_x = lx
        self.width = rx - lx + size
        self.emit("changed")

    def destroy(self):
        self.emit("beforeDestroy")
        self.canvas.delete(self.GROUP_TAG)
        self.emit("destroyed")
