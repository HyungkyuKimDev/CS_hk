# 모던 PHP

---

## 내장 웹서버 실행하기

1. 내장된 웹서버 실행

PHP 파일에 있는 디렉터리에 가서, 터미널에 아래와 같이 입력

```
php -S 127.0.0.1:8000
```

-S 옵션이 서버 실행 옵션

이후 브라우져에서 아래와 같이 입력해 접속

```
127.0.0.1:8000/[php file name]
```

---

2. 내장 Apache 서버 이용

PHP에는 Mac에 내장된 Apache 웹 서버가 제공되어. 실행 가능하다.

터미널에 가서 아래와 같이 입력해 Apache 실행

```
sudo apachectl start
```

이후 브라우져에 가서 아래와 같이 입력해 접송

```
http://localhost/[php file name]
```

이때, php 파일은 Root 폴더에 있어야 한다.

서버 상황 확인은 아래 코드

```
apachectl status
```

종료 코드

```
apachectl stop
```

3. MAMP 사용 방법

1번 방법과 거의 동일

### Refernce : https://wikidocs.net/116963