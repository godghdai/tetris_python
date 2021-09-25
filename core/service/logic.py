from ..common import Context, Config


class LogicService:

    def __init__(self):
        ctx = Context.get_instance()
        config: Config = ctx.get_module("core.common.config.Config")
        self.config = config
        self.diamond = ctx.get_module("core.gui.view.diamond.DiamondView")
        self.wall = ctx.get_module("core.gui.view.wall.WallView")
        self.board = ctx.get_module("core.gui.view.board.BoardView")
        self.max_dx = config.cols
        self.max_dy = config.rows
        self.bak_dx = int(config.cols / 2 - 2)
        self.bak_dy = 0
        self.cur_dx = self.bak_dx
        self.cur_dy = self.bak_dy

    def in_area(self, new_dx, new_dy):
        if (new_dx < 0 or new_dx > self.max_dx - 1 or
                new_dy < 0 or new_dy > self.max_dy - 1):
            return False
        return True

    def can_move(self, dx, dy):
        cells = self.diamond.cells
        for cell in cells:
            new_dx = self.cur_dx + cell.x + dx
            new_dy = self.cur_dy + cell.y + dy

            if new_dy == self.max_dy:
                self.mark_to_wall(self.cur_dx, self.cur_dy)
                return False

            if not self.in_area(new_dx, new_dy):
                return False

            if self.wall.is_mark(new_dy, new_dx):
                if dy == 1:
                    self.mark_to_wall(self.cur_dx, self.cur_dy)
                return False

        self.cur_dx += dx
        self.cur_dy += dy

        return True

    def mark_to_wall(self, dx, dy):
        cells = self.diamond.cells
        for cell in cells:
            col = int(dx + cell.x)
            row = int(dy + cell.y)
            if self.wall.is_mark(row, col):
                print("game over!!")
                return
            self.wall.mark(row, col, self.diamond.border_color, self.diamond.fill_color)

        self.wall.update()

        self.cur_dx = self.bak_dx
        self.cur_dy = self.bak_dy
        # print(id(self.diamond))
        self.diamond = self.board.new_diamond()

        gamecontrol = Context.get_instance().get_module("core.control.game.GameControl")
        gamecontrol.diamond = self.diamond
        # print(id(self.diamond))

    def can_rotate(self):
        diamond = self.diamond
        if not diamond.isCanRotate:
            return False
        cells = diamond.cells
        for cell in cells:
            newX, newY = self.getNewXY(cell.x, cell.y, diamond.center_x, diamond.center_y)
            new_dx = self.cur_dx + newX
            new_dy = self.cur_dy + newY
            if not self.in_area(new_dx, new_dy):
                return False
        return True

    def rotate(self):
        diamond = self.diamond
        cells = diamond.cells
        for cell in cells:
            newX, newY = self.getNewXY(cell.x, cell.y, diamond.center_x, diamond.center_y)
            cell.x = newX
            cell.y = newY

    def getNewXY(self, x, y, center_x, center_y):
        # radians = math.radians(angle)
        # cosv, sinv = math.cos(radians), math.sin(radians)
        # 90 0 1
        # x0 = (x - center_x) * cosv - (y - center_y) * sinv + center_x
        # y0 = (x - center_x) * sinv + (y - center_y) * cosv + center_y
        x0 = center_y + center_x - y
        y0 = x - center_x + center_y
        # print(f"x:{x0},y:{y0}")
        return x0, y0
