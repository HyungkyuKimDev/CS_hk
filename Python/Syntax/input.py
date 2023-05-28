# 입력문 input(prompt)

input("What is your name?")
#  > 대신에 커서가 깜빡이게 된다.

print("Hello "+ input("What's your name : "))
# 이름을 input 입력 받은 뒤 print 출력

user_name = input("What is your name?")
print(len(user_name))
# 문자열 구하는 함수 len(S)
# == print(len(input("What is your name?")))