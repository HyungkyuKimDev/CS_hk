# 변수 바꾸기
a = input("A: ")
b = input("B: ")

temp = a
a = b
b = temp

print("a became : " + a)
print("b became : " + b)

# 변수 규칙
# 변수의 이름이 의미가 있어야 한다.
# 숫자는 변수의 시작이 될 수 없다.
# 특정 기능을 가진 단어는 사용할 수 없다.

# 밴드 만들기
#1. Create a greeting for your program.
print("\n")
print("Hello My friends!!\n")

#2. Ask the user for the city that they grew up in.
user_city = input("Where are you from??\n")

#3. Ask the user for the name of a pet.
user_pet = input("Then What is your pet's name?\n")

#4. Combine the name of their city and pet and show them their band name.
print("Then your band name is : " + user_city + user_pet + "\n")

# Solution: https://replit.com/@appbrewery/band-name-generator-end
