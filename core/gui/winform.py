from tkinter import *
from tkinter import messagebox
from ..common import Observer


class WinForm(Observer):
    def __init__(self, **kwargs):
        super().__init__()
        self.title = kwargs.get("title", "")
        self.win = Tk()
        self.win.title(self.title)
        # self.win.resizable(width=False, height=False)
        # self.win.iconbitmap('images/fklogo.ico')

        self.screen_width = self.win.winfo_screenwidth()
        self.screen_height = self.win.winfo_screenheight()
        self.width = kwargs.get("width", self.screen_width / 4)
        self.height = kwargs.get("height", self.screen_height / 4)
        self.canvas = Canvas(self.win, bg="black", width=self.width, height=self.height)
        self.canvas.pack()
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        # if messagebox.askokcancel("提示", "确认要退出程序么?"):
        self.emit("beforeclose")
        # self.win.destroy()

        # sys.exit(0)

    def exit(self):
        self.win.quit()

    def show(self):
        x = (self.screen_width - self.width) / 2
        y = (self.screen_height - self.height) / 2
        self.win.geometry("%dx%d+%d+%d" % (self.width, self.height, x, y))
        self.win.mainloop()
