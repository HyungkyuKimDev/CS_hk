# key value
# 사전 key 단어 value 그 단어의 뜻
# {key: value}

"""
programming_dictionary = {
"~" : " ",
"~": " ",
...etc
"""

programming_dictionary = {
    "bug": "An error",
    "Function": "call over",
    123: "number"
}

print(programming_dictionary["bug"]) # key를 이용하고 출력은 value가 나온다.
print(programming_dictionary[123])

#Adding new items to dictionary 딕셔너리에 새 값 넣기
programming_dictionary["Loop"] = "Action"

# Create an empty dictionary
empty_dictionary = {}

# Wipe an exisiting dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A month"
print(programming_dictionary["Bug"])

# Loop through a dictionary
for key in programming_dictionary:
    print(key) # key가 출력
    print(programming_dictionary[key]) # value 값 출력