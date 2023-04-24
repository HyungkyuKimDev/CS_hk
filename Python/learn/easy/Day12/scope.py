"""
다른 언어와 달린 파이썬은 if else while 등등의 경우 scope를 생성하지 않는다.
def의 경우에만 scope가 형성되고 지역변수가 생긴다.
def 안에 전역 변수를 수정하는 방법
global 변수 하면 그 변수 쓸 수 있다.
그냥 return 값으로 그 전역 변수를 사용해도 됨.
"""

# Global Constants 상수는 대문자로

PI = 3.1459

# range(start, stop, step)
