Mysql

brew install mysql
>
설치

기본 사용

brew services start mysql
>
mysql 서버 시작(homevrew)로 설치되었으므로 이거 사용

brew services stop mysql
>
mysql 서버 종료(homebrew)로 설치된 경우라 마찬가지

시작 흐름

brew services start mysql // server 시작

mysql -u root -p // root 계정에 password 사용 접속

상태 확인
status

종료 흐름

exit // mysql 종료

brew services stop mysql // 서버 종료
