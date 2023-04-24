"""
OOP 객체 지향 프로그래밍
Object Oriented Programming

각각의 기능을 Object로 구현해 사용.
큰 것을 작은 것으로 나누는 프로그래밍 방식
Ex) 식당 Chef / Waiter / Cleaner
VS

Procedural Programming 절차 지향 프로그래밍 자바 등등
> 절차(순서)에 따라 진행. 코드가 복잡해지는 단점이 발생
"""

"""
How to OOP 
each Class 는 attributes(속성, 변수) 와 methods(기능, 함수) 를 가지고 있다.
each Class 는 여러 Objects 로 만들 수 있다.
"""
# car Object // CarBlueprint() Class
# car = CarBlueprint()

# blueprint
# import turtle
"""
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
# * import로 다른 파일의 변수를 사용할 수 있다.

my_screen = Screen()
print(my_screen.canvheight)
# Screen 클래스 my_screen 객체 .canvheight 속성(attribute)
# car.speed // car object speed attribute

my_screen.exitonclick()
"""

"""
# python packages
# python3 -m pip install ~~
# package 설치법

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Digimon", ["agumon", "ingmon"])
table.add_column("Type", ["fire", "electronic"])
print(table)
"""

# Class 만들기(blueprint)
"""
class User:
   pass

user_1 = User()
user_1.id = "001"
user_1.username = "james"

print(user_1.username)
"""
# Constructor 생성자
# init 은 속성 초기화를 시킴
# 따라서 init 안에 것들은 객체를 생성할 때 자동으로 작동한다.
# 여러 속성을 가진 클래스를 만들때 사용
"""
class Car:
    def __init__(Self, seats):
        self.seats = seats

my_car = Car(5) // my_car.seats = 5
"""

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # 항상 0으로 고정. 특정 값으로 고정인 경우 수를 지정해도 됨

user_1 = User("001", "kim")
user_2 = User("002", "jack")
print(user_1.id)

"""
def function():
    pass
# pass 는 클래스나 함수를 빈칸으로 넘길 수 있음
"""

"""
클래스 이름 PascalCase
파이썬에서 사용X camelCase
변수 이름 snake_case
"""


