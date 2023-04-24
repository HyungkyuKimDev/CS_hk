from turtle import Turtle, Screen
# keyword module name keyword Thing in module
# turtle 모듈에서 Turtle을 가져옴

# from turtle import *
# turtle 모듈에서 전부 가져옴 // 코드 이해가 어렵기 때문에 잘 안씀

# import turtle as t
# 모듈을 as ~ 값으로 데리고 올 수 있음

# turtle과 같이 내장된 모귤 패키지 이외 라이브러리는 외부 인터넷에서 설치해서 사용함
"""
gubbuk = Turtle()

gubbuk.shape("turtle")
"""
"""
def gubbuk_square(self):
    for _ in range(4):
        self.forward(100)
        self.right(90)
        
gubbuk_square(gubbuk)
"""
"""
for _ in range(10):
    gubbuk.pendown()
    gubbuk.forward(10)
    gubbuk.penup()
    gubbuk.forward(10)
"""

"""
python tuple
튜플은 리스트와 비슷하지만 변경할 수 없다. immutable
변경 불가능한 리스트를 만들고 싶다면 사용( Ex) 색상 )
만약 리스트로 만들고 싶으면 list(my_tuple)로 리스트로 만들어냄
 
my_tuple = (a, b, c)
my_tuple[0]
"""

"""
event listener
사용자의 동작을 인식해 이용하는 방법
"""
"""
screen = Screen()

def move_forward():
    gubbuk.forward(10)

screen.listen()
screen.onkey(move_forward, "w")
screen.exitonclick()
"""
"""
Higher order function 고차 함수
함수 와 다른 함수를 동시에 엮어서 사용되는 방식

def add(n1, n2):
    return n1 + n2
    
def calculator(n1, n2, func):
    return func(n1, n2)
    
result = calculator(2, 3, add)
print(result)
"""

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    gubbuk = Turtle(shape="turtle")
    gubbuk.color(colors[turtle_index])
    gubbuk.penup()
    gubbuk.goto(x=-230, y=y_positions[turtle_index])

screen.exitonclick()
