from .layer import Layer
from ...common import ImageManger


class CellData:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.id = None
        self.mark = False
        self.border_color = None
        self.fill_color = None


class WallView(Layer):
    WALL_TAG = ("__wall",)

    def __init__(self, x, y, parent):
        super().__init__(parent.x + x, parent.y + y)
        self.border_id = None
        self.border_padding = 4
        self.cells = None
        self.parent = parent
        self.max_dy = parent.rows
        self.max_dx = parent.cols
        self.photo = None
        self.image_manger: ImageManger = self.ctx.get_module("core.common.imagemanger.ImageManger")

    @classmethod
    def create(cls, x, y, parent):
        view = cls(x, y, parent)
        # CellData二维数组初始化
        view.cells = [
            ([CellData(row, col) for col in range(parent.cols)])
            for row in range(parent.rows)
        ]

        view.photo = view.image_manger.load_image(ImageManger.BACKGROUND)
        view.canvas.create_image(x, y, image=view.photo, anchor="nw")
        view.create_wall()
        view.create_border()
        return view

    def create_border(self):
        padding = self.border_padding
        self.border_id = \
            self.canvas.create_rectangle(
                self.x - padding,
                self.y - padding,
                self.x + self.parent.size * self.parent.cols + padding,
                self.y + self.parent.size * self.parent.rows + padding,
                outline="yellow", width=1)

    def border_color(self, color):
        self.canvas.itemconfig(self.border_id, outline=color)

    def create_wall(self):
        size = self.parent.size
        for row in range(self.parent.rows):
            for col in range(self.parent.cols):
                x = self.x + col * size + 1
                y = self.y + row * size + 1
                # DarkSlateGray
                self.cells[row][col].id = \
                    self.canvas.create_rectangle(
                        x, y, x + size - 2, y + size - 2,
                        outline="",
                        fill="",
                        tag=self.WALL_TAG
                    )
                self.cells[row][col].border_color = ""
                self.cells[row][col].fill_color = ""

    def update(self):
        lines = 0
        while True:
            row = self.find_remove_row()
            if row == -1:
                break
            self.remove_row(row)
            lines += 1
        if lines > 0:
            self.emit("removeRows", lines)

    def find_remove_row(self):
        for row in range(self.max_dy - 1, -1, -1):
            for col in range(self.max_dx):
                if not self.is_mark(row, col):
                    break
            else:
                return row
        return -1

    def remove_row(self, r_row):
        cells = self.cells
        for col in range(self.max_dx):
            for row in range(r_row - 1, -1, -1):
                cur = cells[row][col]
                border_color, fill_color, mark = cur.border_color, cur.fill_color, cur.mark
                self.update_cell(self.cells[row + 1][col], border_color, fill_color, mark)

    def update_cell(self, cell: CellData, border_color, fill_color, mark):
        self.canvas.itemconfig(cell.id, outline=border_color, fill=fill_color)
        cell.mark = mark
        cell.border_color = border_color
        cell.fill_color = fill_color
        # if mark:
        #     self.canvas.dtag(cell.id, self.WALL_BG_TAG)
        #     self.canvas.addtag_withtag(self.WALL_TAG, cell.id)
        # else:
        #     self.canvas.dtag(cell.id, self.WALL_TAG)
        #     self.canvas.addtag_withtag(self.WALL_BG_TAG, cell.id)

    def mark(self, row, col, border_color, fill_color):
        self.update_cell(self.cells[row][col], border_color, fill_color, True)

    def is_mark(self, row, col):
        return self.cells[row][col].mark

    def is_overload(self):
        for col in range(self.max_dx):
            pass
