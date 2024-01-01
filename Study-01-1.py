#code02-06.py
# 거북이 반복문 이용
import turtle

myT = None

myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0, 4) :
    myT.forward(200)
    myT.right(90)

turtle.done()