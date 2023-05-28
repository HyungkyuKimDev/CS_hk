# typeError 데이터 형식 에러

# Data Tyoes

# String

print("Hello"[0])
# subscript 문자열에서 인덱스로 원하는 글자를 뽑아내는 방법

# Integer

print(123 + 345)

# Large Integer
# 큰 숫자의 경의 _를 붙여서 쓰면 된다. 파이썬에서 _를 무시한다.

123_456_345

# Float
# float이 계산에 들어가면 정수가 float로 바뀐다.

3.1459

# Boolean

True
False

num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characater.")

# type() 는 안에 값의 데이터 형식을 알 수 있다.
print(type(num_char))

new_num_char = str(num_char)
# str()는 문자열로 바꿀 수 있다.

# float()는 부등 소수점으로 바꿀 수 있다.

# 부등 소수점 관련
# 반올림 round(n1 / n2 , n3) // n3는 몇번째 소수에서 반올림할지를 정함
# 버림 나누기를 // 사용 하면 자동 버림으로 바뀜
# number /= 2  # number = number / 2

# 십의 자리 일의 자리 문제
full_number = str(input("What is your number\n"))
ten_num = int(full_number[0])
one_num = int(full_number[1])
total_num = str(ten_num + one_num)

print("Then the number is : " + total_num)

# f-string 모든 타입을 문자열로 바꿔준다.
# 이걸 쓰면 print에서 문자열 이외 타입을 사용할 수 있다.
score = 0
height = 2.0
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
