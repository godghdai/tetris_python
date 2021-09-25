from tkinter import *
from PIL import Image
from PIL import ImageTk

window = Tk()
window.title('My Window')
window.geometry('600x800')

canvas = Canvas(window, bg='green', height=500, width=500)
canvas.pack()

# 说明图片位置，并导入图片到画布上
im1 = None
im2 = None
im1 = Image.open("D:/Users/yzd/PycharmProjects/my/tetris/resource/9.jpg")

im2 = ImageTk.PhotoImage(im1)

canvas.create_image(0, 0, anchor=NW, image=im2)
canvas.create_rectangle(0,0,20,20,fill="white")
window.mainloop()
