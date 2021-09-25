from .winform import WinForm
from .view import BoardView
from ..common import Context


class TetrisWin(WinForm):
    def __init__(self):
        ctx = Context.get_instance()
        config = Context.get_module("core.common.config.Config")
        super().__init__(title=config.title, width=config.width, height=config.height)
        ctx.register(self.canvas)
        self.board_view = BoardView.create()
