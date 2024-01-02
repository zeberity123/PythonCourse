from tkinter import *

# 함수 정의 부분
def keyEvent(event) :
    messagebox.showinfo("키보드 이벤트",  "눌린 키 : " + chr(event.keycode) )
   
# 메인 코드 부분
window = Tk()

window.bind("<Key>",keyEvent)

window.mainloop()
