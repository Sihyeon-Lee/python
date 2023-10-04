#code10-12.py
from tkinter import *
from time import *

# 전역 변수 선언 부분
# 리스트 변수에 사진 9장의 파일명을 저장
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif",
             "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
# PhotoImage() 함수로 생성할 변수 9개 준비
photoList = [None] * 9
# 현재 사진 번호에 사용할 num 선언, 0~8까지 사용
num = 0

# 함수 선언 부분
# 다음 버튼 실행 함수
def clickNext() :
    global num
    # 다음 사진을 표시해야 하므로 사진 번호 하나 증가
    num += 1
    # 사진 번호는 최대 8이므로 8이 넘으면 다시 0번 사진을 표시하게 함
    if num > 8 :
        num = 0
    photo =  PhotoImage(file = "gif/" + fnameList[num])
    # 변경된 사진 번호에 해당하는 이미지 파일로 PLabel을 변경
    pLabel.configure(image = photo)
    pLabel.image = photo

# 이전 버튼 실행 함수
def clickPrev() :
    global num
    # 이전 사진을 표시해야 하므로 사진 번호 하나 감소
    num -= 1
    # 사진 번호는 최소 0이므로 0보다 작으면 다시 8번 사진을 표시하게 함
    if num < 0 :
        num = 8
    photo = PhotoImage(file = "gif/" + fnameList[num])
    # 변경된 사진 번호에 해당하는 이미지 파일로 PLabel을 변경
    pLabel.configure(image = photo)
    pLabel.image = photo

# 메인 코드 부분
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

# 프로그램 실행 직후 보이는 이미지는 첫 번째 사진이 보이게 설정
photo = PhotoImage(file = "gif/" + fnameList[0])
pLabel = Label(window, image = photo)

# 버튼 및 이미지 위치를 place로 지정
btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()