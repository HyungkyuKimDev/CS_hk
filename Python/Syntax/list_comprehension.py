# list comprehension
# 리스트 이용 새 리스트에  새로운 값을 주기 위한 방법
# new_list = [new_item for item in list]

# list comprehension 안 쓴 경우
# numbers = [1, 2, 3]
# new_list = []
# for n in list:
#     add_1 = n + 1
#
# new_list.append(add_1)

# list comprehension 이용 경우
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

# 문자열의 경우
# name = "KImHyungkyu"
# new_name = [letter for letter in name]
# print(new_name)

# 조건식을 추가한 경우
# names = ["alex", "Beth", "Elanor"]
# short_names = [n for n in names if len(n) < 5]
# short_names = [n.upper() for n in names if len(n) < 5]

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex", "Bath", "Dave"]

import random
students_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
