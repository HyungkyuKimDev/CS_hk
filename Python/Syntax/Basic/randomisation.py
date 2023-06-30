# Randomisation
# 무작위성

# 모듈은 각각 프로그램의 일정 기능을 담당한다.
# 모듈은 동일한 파이썬 파일로, import module_name 을 통해서 사용할 수 있다.

# 사용하기 위해서 random 모듈을 가져와야 한다.
import random

random_num = random.randint(1, 10)
print(f"{random_num}")

# 부등 소수섬 난수 random() 0 ~ 1 사이의 부등 소수점을 나타낸다.
