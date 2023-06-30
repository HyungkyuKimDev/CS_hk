# readlines()
# 리스트 안의 항목으로 각 줄이 각각 추가됨
#
# replace()
# 특정 구문을 다른 구문으로 변경
#
# String strip()
# 단어 앞 뒤 공백을 제거해주는 메소드

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name =name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)