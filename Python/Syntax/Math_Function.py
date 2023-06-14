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
# SUM Example
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 55
print(sum(nums))

# 60
print(sum(nums, start=5))

""" divmod 함수
Function : 두 수의 몫과 나머지를 구함
Usage : divmod([int / float], [int / float])
Return : (tuple 자료형) => (몫, 나머지)
"""
num1 = 5
num2 = 3

# (1, 2)
print(divmod(num1, num2))

# <class 'tuple'>
print(type(divmod(num1, num2)))

# 1, 2
print(*divmod(num1, num2))
