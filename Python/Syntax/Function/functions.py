# function

"""
def funciton_name():
    ~~
    ~~

funciton_name()
"""

# Indentation 들여쓰기

# code block


def my_function(jane):
    print(f"Hello {jane}")
# 들여쓰기 안은 하나의 코드 블락이다.


my_function("kyu")

"""
def my_function(someting):
    #
"""
# sometihng == parameter 파라미터 함수에서 아규먼트가 사용될 때 이용 되는 데이터 이름
# something = 123 // 123 argument 함수에 전해져 호출되는 데이터

"""
여러 파라미터 사용
def greet_with(name, location):
    #
    
Positional Arguments 순서에 따라 위치 인자가 작동함 
Keyword Arguments 그래서 그런 순서 문제에서는 키워드 아규먼트를 쓴다.

greet_with(name="kyu", location="seoul")
"""

# module math
# math.ceil() 올림

# Functions with Outputs


def my_function():
    return 3 * 2


print(my_function())

# 출력이 있는 함수를 만들기 위해서는 return이 있는게 중요하다. return는 함수의 마지막을 의미한다.
# 그래서 함수 안에서 또 다른 코드 블락에서 return이 있으면 그대로 종료된다.

# title은 문자열의 앞글자만 대문자로 만들어준다.


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


print(format_name("AngGELa", "Yu"))
