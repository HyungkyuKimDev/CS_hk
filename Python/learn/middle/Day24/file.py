# 기본 파일 읽기 방법
# file = open("file_ex.txt")
# comment = file.read()
# print(comment)
# file.close()

# 파일 닫기 신경 없이 사용하는 방법
with open("file_ex.txt", mode="a") as file: # file로 저장
    file.write("\nI'm kyu!!")
# r write 모드에서 파일이 없으면 새로 만들어짐
# r 읽기 모드 w 쓰기 모드 a 덧붙여쓰기 모드