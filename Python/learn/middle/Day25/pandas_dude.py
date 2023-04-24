# CSV Comma Separated Values
# 콤마로 구분된 값들

# with open("weather.csv") as weather:
#     weather_data = str(weather.readlines())
#
# with open("pandas_dude.py", mode="a") as pandas:
#     pandas.write(weather_data)

# import csv
#
# with open("weather.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

# pandas 라이브러리
# 데이터를 분석하기 위한 라이브러리

# 판다 이용 간단히 데이터 가져오기
import pandas
# data = pandas.read_csv('weather.csv')
#print(data["temp"]) # temp 열 가져오기

# print(type(data)) # 데이터 타입 확인

# 데이터프레임
# 전체적으로는 데이터 프레임이라고 한다.
# 시리즈는 데이터 프레임의 각각의 열을 의미한다. 싱글 coluumn

# 데이터를 딕셔너리로 변환
# data_dict = data.to_dict()
# print(data_dict)

# 온도를 리스트로 변환 후 평균 온도 구하기
# temp_list = data["temp"].to_list()
# # avr_temp = 0
# # for temp in temp_list:
# #     avr_temp += int(temp)
# # avr_temp /= len(temp_list)
# # print(round(avr_temp))
#
# print(data["temp"].mean())

# Column
# print(data["condition"])
# print(data.condition)

# # Row
# monday = data[data.day == "Monday"]
# print(monday.temp)

# Creating dataframe from scratch
# data_dict = {
#     "students": ["amy", "james", "angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# sat 수학 점수가 500점 넘는 학교 출력
data = pandas.read_csv("SAT__College_Board__2010_School_Level_Results.csv")
math = data[data.Mathematics > 500]
print(math.School_Name)
# 위 해당 학교 수 출력
print(len(math.School_Name))
