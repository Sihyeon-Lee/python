#code10-05.py

from tkinter import *

# 메인 코드
window = Tk()

button1 = Button(window, text = "파이썬 종료", fg = "red",
                 command = quit)

button1.pack()

window.mainloop()