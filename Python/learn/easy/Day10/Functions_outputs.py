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