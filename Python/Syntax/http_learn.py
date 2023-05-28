# HTTP Requests 종류

# # 1. GET => requests.get()
# > api에 데이터를 요청하고, 데이터를 받는데 사용
#
# # 2. POST => request.post()
# > api에 데이터를 전송, 전송의 성공 여부를 응답 받음
#
# # 3. PUT => requests.put()
# > api에 데이터를 업데이트

# 4. DELETE => request.delete()
# > 기존 데이터 삭제됨


# HTTP
# import requests
# API 통신은 우선 site_name_endpoint + parameters 로 구성
# 기본 endpint 하나
# 해당 parameters 를 딕셔너리로 정리

# Ex)
# response = requests.post(url=pixela_endpoint, json=user_params)

# API 보안 // 암호화하는 방법
# HEADER 방식

# 사용 방법은 headers 딕셔너리에 토큰 값을 넣어 requests 안에 넣어 암호화 한다.
# headers = {
#     "TOKEN": "~~"
# }
#
# requests.post(url=, json=, headers=headers)