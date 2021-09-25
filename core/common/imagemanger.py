import os.path as osPath

from PIL import Image as PImage, ImageTk
from tkinter import Image


class ImageManger:
    INDICATOR = "bhhhh.png"
    BACKGROUND = "bg66.png"

    def __init__(self, base_path):
        self.base_path = base_path
        self.cache = {}
        self.cache2 = {}

    def get_image(self, path, width, height) -> Image:
        key = "{}_{}X{}".format(path, width, height)
        if key in self.cache:
            return self.cache[key]

        image = PImage.open(osPath.join(self.base_path, path))
        image = image.resize((width, height), PImage.ANTIALIAS)
        self.cache[key] = ImageTk.PhotoImage(image)
        return self.cache[key]

    def load_image(self, path):
        if path in self.cache2:
            return self.cache2[path]
        image = PImage.open(osPath.join(self.base_path, path))
        self.cache[path] = ImageTk.PhotoImage(image)
        return self.cache[path]
