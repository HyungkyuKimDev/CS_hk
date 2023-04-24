# SMTP
# Simple Mail Transfer Protocol
#
# 메일을 주고받는 방법
# 각각의 메일 서버를 통과해 상대방의 컴퓨터에 이동함

# import smtplib # smtp 사용 위한 파이썬 모듈 smtplib
#
# my_email = "hkpythontest3@gmail.com" # 테스트 서버
# my_password = "yfesgetfclcmouhl"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection: # 이메일 제공자 설정, 서버 마다 다름
#     connection.starttls() # 이메일 송수신시 보호. 암호화
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs="hkpythontest2@gmail.com", msg="Subject:Hi!\n\nThis is My Second letter")

import datetime as dt

# now_time = dt.datetime.now()
# year = now_time.year
# day_of_week = now_time.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1998, month=1, day=16)
# print(date_of_birth)


