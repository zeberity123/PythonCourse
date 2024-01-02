from tkinter import *

## 변수 ##
window = None
canvas = None
XSIZE, YSIZE=256,256

## 메인 코드 ##
window=Tk()
canvas = Canvas(window, height=XSIZE, width=YSIZE)

canvas.pack()
window.mainloop()
