#code10-16.py

from tkinter import *
from tkinter import messagebox

# 함수 선언 부분
def keyEvent(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키" +
                        chr(event.keycode))
                        #대소문자 다시 확인해보기

# 메인 코드 부분
window = Tk()

window.bind("<Key>", keyEvent)

window.mainloop()
