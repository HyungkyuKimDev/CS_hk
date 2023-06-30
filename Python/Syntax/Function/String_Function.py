"""
Reference : 동연이의 지식 저장소 - PYTHON 기본 문법 정리
(https://www.dongyeon1201.kr/d265b6e8-dd92-4bef-83e7-1280eda02cad)
"""

"""좌, 중앙, 우측 정렬
Function : 특정문자열을 좌 or 중앙 or 우측 으로 정렬한 문자열을 만들 때 사용
Usage :
ljust(width, [fillchar=' ']) => 특정문자를 왼쪽으로 정렬, 길이보다 문자열이 짧을경우 fillchar 값으로 채운다.
center(width, [fillchar=' ']) => 특정문자를 중앙으로 정렬, 길이보다 문자열이 짧을경우 fillchar 값으로 채운다.
rjust(width, [fillchar=' ']) => 특정문자를 오른쪽으로 정렬, 길이보다 문자열이 짧을경우 fillchar 값으로 채운다.
Return : str(정렬된 문자)
"""
# 좌, 중앙, 우측 정렬 Example
test = "abc"

# abc!!!!
temp_str = test.ljust(7, '!')
print(temp_str)

# !!abc!!
temp_str = test.center(7, '!')
print(temp_str)

# !!!!abc
temp_str = test.rjust(7, '!')
print(temp_str)
