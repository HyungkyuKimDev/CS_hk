## Reference : [Nginx php-fpm 설정방법](https://phsun102.tistory.com/46)

<br>

# php-fem 과 nginx

0. php-fpm
CGI( Common Gateway Interface )는 웹서버와 외부 프로토콜을 연결시켜주는 표준 프로토콜이다.   
이 CGI는 각각의 요청별로 프로세스를 생성한다. 요청이 들어올 때 마다 프로세스의 생성과 삭제를 반복하다보면 자연스럽게 속도는 느려진게 된다. 이러한 CGI의 단점을 개선하고자 FastCGI가 등장하였다. 새로이 등장한 FastCGI는 요청이 들어올 때 마다 프로세스를 생성하는 것이 아닌, 이미 기존에 만들어진 프로세스를 바탕으로 새로운 요청들을 처리해 나간다. 프로세스의 생성과 삭제를 통해 발생하는 부하를 줄이기 위한 FastCGI를 활용하기 위해 사용되어지는 것이 php-fpm이다. php가 FastCGI 모드에서 동작하여 처리될 수 있도록 해준다.

1. php-fpm 설치
```
yum install php8-fpm
# php-fpm이 설치되면서 php8버전도 자동적으로 설치된다
```

2. php-fpm 설정 파일 변경

```
nano /etc/php-fpm.d/www.conf
vi /etc/php-fpm.d/www.conf
vim /etc/php-fpm.d/www.conf
```

 
```
# 에디터로 이동

user = apache

group = apache ~~ 부분을 변경해준다.

user = apache
group = apache
;listen.owner = nobody
;listen.group = nobody
;listen.mode = 0660
# php-fpm 설치 시, 기본적으로 설정된 값


user = nginx
group = nginx
listen.owner = nginx
listen.group = nginx
listen.mode = 0660
# nginx에서 php-fpm을 사용하기 위해 설정을 변경한다
```
 

 

3. listen 값 변경

```
listen = 127.0.0.1:9000 으로 되어져 있는 부분을 변경한다.

listen = 127.0.0.1:9000
# 기본으로 설정된 값

listen = /var/run/php-fpm/php-fpm.sock
# php-fpm 소켓으로 변경한 값
 ```

 

4. php-fpm.sock 생성 유무 확인

```
cd /var/run/php-fpm
# php-fpm 관련 디렉터리로 이동

ls
# 현재 디렉터리에 존재하는 파일 목록 확인
php-fpm.sock이 생성된 것을 확인할 수 있다. 생성된 php-fpm.sock 파일은 소켓을 의미한다. 이 소켓파일이 존재해야 php파일을 웹에서 확인할 수 있다.
```
 

 

5. nginx 설정 변경

```
nano /etc/nginx/conf.d/default.conf
vi /etc/nginx/conf.d/default.conf
vim /etc/nginx/conf.d/default.conf

# nginx의 server블록 내용을 변경하기 위해 에디터로 이동
 

location ~ \.php$ 부분 주석해제

# nginx server 블록 변경

location ~ \.php$ {
        root           /var/www/html;
        # php 파일이 존재하는 디렉터리 경로
        
        fastcgi_pass   unix:/var/run/php-fpm/php-fpm.sock;
        # fastcgi_pass : php-fpm.sock이 존재하는 경로
        
        fastcgi_index  index.php;
        # 초기 php 파일명 지정
        
        fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include        fastcgi_params;
}
```

 

6. index.php 파일 생성

```
nano /var/www/html/index.php
vi /var/www/html/index.php
vim /var/www/html/index.php

# index파일 생성하기 위해 에디터로 이동
 

<?php
	phpinfo();
	// index.php
?>
```

127.0.0.1로 이동하면 현재 OS에 설치된 php관련 정보 페이지가 나오게 된다.
