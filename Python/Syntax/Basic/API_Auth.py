# API
# Aplication Programming Interface

# Program > API  > Extenal System
# 프로그램은 API를 토왜 외부 시스템에서 필요한 부분을 가지고 온다.
# 레스토랑이라고 치면 API는 메뉴이고. 외부 시스템은 그 레스토랑 주방을 의미한다.

# URL
# URL 은 API EndPoint
# API Request로 URL을 치면 필요한 정보를 가져와준다.

# API 요청하는 방법
import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status() # HTTP 오류 메세지 출력

# HTTP
# 1XX 진행 중
# 2XX 요청한 데이터를 받을 수 있음
# 3XX 요청한 데이터 받을 권한 없음
# 4XX 사용자에게 문제 발생
# 5XX 서버에 문제 발생

# data = response.json()["iss_position"]["longitude"]

Tokyo_lat = 35.6762
Tokyo_long = 139.6503

parameters = {
    "lat": Tokyo_lat,
    "lng": Tokyo_long,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

# URL 상에서 요청하는 방법
# Endpoint ? Params Name = Value & another Value & ...

# API Authenthic
# API 사용을 안전하게 사용하는 방법
#
# 유료 API
# Selling Data
#
# API Key
# API 사용 남용을 막기 위한 방법

# Environment Variables
# 편의성을 위해서 특정 변수를 환경 변수로 설정하여.설정 변화가 쉽게 한다. 또 보안을 위해서 암호 토큰 등등을 안전하게 저장할 수 있다.
# export ~="" 특정 변수 환경 변수로 설정
# ~.environ.get() => 저장한 환경 변수 받아오기

# 항상 API 키를 쓸때는 공개적인 곳에 업로드 하지 말고, 환경 변수를 사용해야 한다.

# 환경 변수 설정 방법
# export 변수 이름=값
# EX) export OWM_API_KEY=ldafjlksdajfk
#
# 이러면 env 에서 값이 저장되어 있음을 알 수 있음
#
# 환경 변수 이용 방법
# os 모듈 사용
# import os
# 변수명 = os.environ.get(찾는 환경 변수 이름)
#
# EX)
# import os
# api_key = os.environ.get("OWM_API_KEY")