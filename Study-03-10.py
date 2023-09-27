#code10-11.py

from tkinter import *

# 전역 변수 선언 부분
# 버튼을 저장할 9개짜리 리스트 준비
btnList = [None] * 9
# 이미지 파일명 9개를 리스트 형식으로 저장
fnameList = ["froyo.gif", "gingerbread.gif", "honeycomb.gif", "icecream.gif",
             "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif"]
# PhotoImage()로 생성할 9개짜리 리스트 준비
photoList = [None] * 9
i, k = 0, 0
# 그림을 출력할 X, Y 좌표
xPos, yPos = 0, 0
# 그림의 순차번호 num 선언, 0~8까지 사용
num = 0

# 메인 코드 부분
window = Tk()
window.geometry("210x210")

#  9번 반복하며 버튼 생성
for i in range(0, 9) :
    photoList[i] = PhotoImage(file = "gif/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

#  3X3 9번 반복하여 2차원 형태로 이미지 출력
for i in range(0, 3) :
    for k in range(0, 3) :
        # 위젯을 고정 위치에 배치하기 위해 pack() 대신 place() 함수 사용
        # width와 height를 생략하면 위젯의 원래 크기로 표현됨
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()