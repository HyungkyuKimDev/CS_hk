# gui
# Graphic User Interface

# Tkinter
from tkinter import *

window = Tk()
# 이름 붙이기
window.title("HK's GUI Program")
# 최소 크기 적용
window.minsize(width=500, height=300)

input = Entry(width=100)
input.grid(column=1, row=0)
miles = Label(text="Miles", font=("Arial", 23))
miles.grid(column=2, row=0)
is_equal = Label(text="is equal to", font=("Arial", 23))
is_equal.grid(column=0, row=1)
result = Label(text="0", font=("Arial", 23))
result.grid(column=1, row=1)
km = Label(text="Km", font=("Arial", 23))
km.grid(column=2, row=1)
def button_Clicked():
    result.config(text=f"{int(input.get())/1.6}")

button1 = Button(text="Calculate", command=button_Clicked)
button1.grid(column=1, row=2)

#Label
# my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# # 라벨 레이아웃
# my_label.pack()
# my_label["text"] = "New Text"
# my_label.config(text="new Text")

# 버튼
# def button_clicked():
#     print("I got clicked")
#     my_label.config(text=f"{input.get()}")
#
# button = Button(text="click me", command=button_clicked)
# button.pack()
#
# # 입력창
# input = Entry(width=10)
# input.pack()

# 라벨을 표시하는 방법
# pack은 라벨의 위치를 지정, 정확한 위치를 지정하기에는 어려움이 있음
# place는 라벨의 위치를 x y 값으로 지정
# grid는 열과 행으로 나눠서 사용 column=# row=#



# 윈도우가 계속 작동하게 함
window.mainloop()

# Arguments with Default Values
# def my_function(A=1, b=2, c=3)
# 입력하지 않은 인수 값의 경우 default values를 가지고 있어 입력하지 않은 인수 값이 있더라도(누락 인수) 사용이 가능하다.

# 만약에 위와 같은 경우에 3개가 아닌 4개의 인수를 쓰고 싶은 경우는 어떻게 해야할까?
# Unlimited Arguments
# *args
#
# def add(*args):
#     for n in args:
#         print(n)

# 각 인수는 튜플 형태로 저장된다.

# def caculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)

# **kwargs는 인수들이 딕셔너리 형태로 저장된다.

# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw.get("model")
#         self.colour = kw.get("colour")
#
#
# my_car = Car(make ="Nissan", model="GT-R")
# print(my_car.model)