# FIleNotFound
# with open("a_file.txt") as file:
#     file.read()

# 해결
try:
    file = open("A_file.txt")
except FileNotFoundError:
    file = open("A_file.txt", mode="w")
    file.write("Something")
except KeyError as error_message:
    print(f"the key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    raise FileNotFoundError("This is Not Truth")
# keyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banna", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "Abc"
# print(Text +5)

# 예외가 발생할 코드를 포함하는 코드 블록
# try :
#
# 에러가 발생했을 때 작동하는 코드 블록 에러의 이름을 명명해서 적절한 에러가 발생했을 때 작동하도록 함.
# except:
#
# 에러가 발생하지 않았을 때 작동하는 코드 블록
# else:
#
# 어떤 경우에도 작동하는 코드 블록 (잘 사용하지 않음)
# finally:
# raise 는 어떠한 경우에도 에러 메세지를 줄 수 있다.
# raise 오류("오류 메세지")