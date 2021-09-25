from .layer import Layer
from ...common import Context, Config
from .wall import WallView
from .diamond import DiamondView
from .indicator import IndicatorView
from .label import LabelView
import random


class BoardView(Layer):
    def __init__(self):
        board = Context.get_config().board
        super().__init__(board["x"], board["y"])
        self.rows = board["rows"]
        self.cols = board["cols"]
        self.size = board["size"]
        self.diamond: DiamondView = None
        self.indicator: IndicatorView = None
        self.label: LabelView = None
        self.wall: WallView = None
        self.indicator_height = self.rows * self.size - 1
        self.total_remove_lines = 0

    def on_diamond_created(self, source):
        self.indicator = IndicatorView(source.min_x, self.y - 1, source.width, self.indicator_height)
        self.canvas.tag_lower(self.indicator.id, self.diamond.GROUP_TAG)
        self.canvas.tag_lower(self.indicator.id, self.wall.WALL_TAG)

    def on_diamond_changed(self, source):
        self.indicator.update(source.min_x, self.y - 1, source.width, self.indicator_height)
        # if len(self.canvas.find_withtag(self.wall.WALL_TAG)) > 0:
        #  self.canvas.tag_lower(self.indicator.id, self.wall.WALL_TAG)

    def on_diamond_destroyed(self, source):
        self.indicator.destroy()

    def on_wall_remove_rows(self, source, lines):
        self.total_remove_lines += lines
        self.label.text(str(self.total_remove_lines))

    def create_diamond(self):
        ctx = Context.get_instance()
        config: Config = ctx.get_config()
        index = random.randint(0, len(config.diamonds) - 1)
        self.diamond = DiamondView.create(config.size * (config.cols / 2 - 2), 0, self,
                                          config.diamonds[index])
        self.diamond.on("created", self.on_diamond_created). \
            on("changed", self.on_diamond_changed). \
            on("destroyed", self.on_diamond_destroyed). \
            emit("created")
        ctx.register(self.diamond)
        return self.diamond

    def create_wall(self):
        self.wall = WallView.create(0, 0, self)
        self.wall.on("removeRows", self.on_wall_remove_rows)
        Context.module_register(self.wall)

    def create_info(self):
        LabelView(250, 50, "消除行")
        self.label = LabelView(250, 75, "0")

    @classmethod
    def create(cls):
        boardview = BoardView()
        boardview.create_wall()
        boardview.create_diamond()
        boardview.create_info()
        Context.get_instance().register(boardview)
        return boardview

    def new_diamond(self) -> DiamondView:
        ctx = Context.get_instance()
        if self.diamond is not None:
            ctx.unregister(self.diamond)
            self.diamond.destroy()
        self.create_diamond()
        return self.diamond
