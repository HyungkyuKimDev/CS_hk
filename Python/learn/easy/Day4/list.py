# 리스트는 데이터 구조를 의미한다.

state_of_america = ["LA", "New York"]

print(state_of_america[0]) # LA
print(state_of_america[-1]) # New York

# 배열 끝 요소 추가 ~.append("#")

state_of_america.extend(["Angela", "seoul"])

# index err == 리스트 관련 문제

# 중첩 리스트
state_of_japan = ["nagoya", "tokyo"]

state_of_global = [state_of_america, state_of_japan]
print(state_of_global)
print(state_of_global[1][1]) # 중첩 리스트 중 두번째 리스트의 두번째 항목

# 문자열 팁 ''' 을 사용한다.
star = '''
    *
   ***  
  *****
'''

print(star)