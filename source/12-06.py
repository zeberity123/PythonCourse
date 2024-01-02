from tkinter import *

# 함수 정의 부분
def myFunc() :
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")

# 메인 코드 부분
window = Tk()

photo = PhotoImage(file="gif/dog2.gif")
button1 = Button(window, image=photo, command=myFunc)

button1.pack()

window.mainloop()
