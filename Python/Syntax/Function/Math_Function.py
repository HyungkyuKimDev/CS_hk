"""
Reference : 동연이의 지식 저장소 - PYTHON 기본 문법 정리
(https://www.dongyeon1201.kr/d265b6e8-dd92-4bef-83e7-1280eda02cad)
"""

import math
# 수학 내장 함수

""" sum 함수
Function : iterable 자료형(member를 차례대로 반환 가능한 object. Ex : str , list , tuple)의 원소들 값들을 모두 더하여 반환한다.
Usage : sum(iterable, start=num) => start는 총합에서 추가하는 값
Return : num (원소들의 합)
"""
# sum Example
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 55
print(sum(nums))

# 60
print(sum(nums, start=5))

""" divmod 함수
Function : 두 수의 몫과 나머지를 구함
Usage : divmod([int / float], [int / float])
Return : (tuple 자료형) => (몫, 나머지)
Tip : 작은 수의 경우, a//b , a%b 를 사용하는 경우가 더 빠르다.
"""

# divmode Example
num1 = 5
num2 = 3

# (1, 2)
print(divmod(num1, num2))

# <class 'tuple'>
print(type(divmod(num1, num2)))

# 1, 2
print(*divmod(num1, num2))

""" int 형 변환 함수
Function : 특정 진수의 수를 10진법으로 변환시킨다.
Usage : int(x,[base=10]) => base 값은 해당 수의 진법 수
Return : 변환된 숫자
"""

num = '1234'
base = 5

# 5진법으로 작성된 1234 숫자가 10진법으로 변환된다.
answer = int(num, base)

# 16진수로 작성된 0x123 값이 10진수로 변환된다. => 291
int('0x123', 16)

# 8진수로 작성된 0o1234 값이 10진수로 변환된다. => 668
int('0o1234', 8)

# 2진수로 작성된 0b1010101 값이 10진수로 변환된다. => 749
int('0b1011101101', 2)

""" max / min 함수
Function : iterable 자료형 또는 인자로 삽입된 숫자들 중 가장 크거나 작은 값을 구한다.
Usage : 
max(iterable) / min(iterable) 
max(num1, num2, num3, ...) / min(num1, num2, num3, ...)
Return : 
max() 함수일 경우 : 가장 큰 값 
min() 함수일 경우 : 가장 작은 값
"""
# max / min Example
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 10
print(max(nums))

# 17
print(max(1, 3, 4, 17, 16, 13))

"""round 함수
Function : 소수 값을 반올림할 때 사용하는 함수
Usage : round(float, n) => n은 반올림 소수 단위 정함
Return : 반올림 처리 된 값 반환
"""
# round Example
# 2
print(round(1.5))

# 1.77
print(round(1.7664, 2))

"""abs() 함수
Function : 입력한 숫자의 절대 값을 구하는 함수
Usage : abs(num)
Return : 입력한 숫자(num)의 절대 값이 반환
"""
# abs() Example
# 1.54
print(abs(-1.54))

# 3.54
print(abs(3.54))

""" math.gcd(), math.lcm() 함수
Function : 입력한 두 숫자의 최대 공약수와 최소 공배수를 구하는 함수
Usage :
최대 공약수 : math.gcd(num1, num2)
최소 공배수 : math.lcm(num1, num2)
Return :
gcd() 함수 일 경우 : 최대 공약수 반환
lcm() 함수 일 경우 : 최소 공배수 반환
Tip : 두 숫자까지 사용 가능하므로, 셋 이상은 직접 함수를 제작하여 구현해야한다. 
"""
# gcd() lcm() Example
# 7
print(math.gcd(14, 21))

# 42
print(math.lcm(14, 21))
