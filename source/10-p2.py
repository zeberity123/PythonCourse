from tkinter import *

## 변수 ##
window = None
canvas = None
XSIZE, YSIZE=256,256

## 메인 코드 ##

window=Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height=XSIZE, width=YSIZE)

paper=PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image( (XSIZE/2, YSIZE/2), image=paper, state="normal")

# 이 부분에서 읽어온 파일을 찍기
fp = open('c:/temp/flower.raw', 'rb')

for i in range(0, XSIZE) :
    for k in range(0, YSIZE) :
        data = int(ord(fp.read(1)))
        paper.put("#%02x%02x%02x" % (data,data,data) , (k, i))
        
fp.close()

canvas.pack()
window.mainloop()

