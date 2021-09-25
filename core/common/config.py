import json
from .util import Util


class Config:
    def __init__(self):
        self._dic = {}
        self.load("keymapper")
        self.load("diamonds")
        self.load("ui")
        self.load("colors")

    def load(self, filename):
        path = Util.get_config_path(filename + ".json")
        fp = open(path, 'r', encoding='utf8')
        self._dic[filename] = json.load(fp)
        fp.close()

    @property
    def keymapper(self):
        return self._dic["keymapper"]

    @property
    def diamonds(self):
        return self._dic["diamonds"]

    @property
    def colors(self):
        return self._dic["colors"]

    @property
    def board(self):
        return self._dic["ui"]["board"]

    @property
    def size(self):
        return self._dic["ui"]["board"]["size"]

    @property
    def rows(self):
        return self._dic["ui"]["board"]["rows"]

    @property
    def cols(self):
        return self._dic["ui"]["board"]["cols"]

    @property
    def width(self):
        return self.cols * self.size + 100

    @property
    def height(self):
        return self.rows * self.size + 2 * self.size

    @property
    def title(self):
        return self._dic["ui"]["title"]
