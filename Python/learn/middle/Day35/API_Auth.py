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