from tkinter import *

# 함수 정의 부분
def clickLeft(event) :
    messagebox.showinfo("마우스", "왼쪽 마우스가 클릭됨")

# 메인 코드 부분
window = Tk()

window.bind("<Button-1>", clickLeft)

window.mainloop()
