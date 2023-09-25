# Nginx

오픈 소스 고성능 HTTP 및 리버스 프록시 서버   
<br>

## 사용 커맨드

Nginx 실행

```
service nginx start
sudo service nginx start
sudo systemctl start nginx
```

Nginx 재실행

```
service nginx restart
sudo service nginx restart
sudo systemctl restart nginx
```

Nginx 중단

```
service nginx stop
sudo service nginx stop
sudo systemctl stop nginx
```

Nginx 상태보기

```
service nginx status
sudo service nginx status
ps -ef | grep nginx
```

Nginx 구성 테스트

```
sudo nginx -t
sudo systemctl status nginx
sudo nginx -v
```


### reference
1. https://computer-science-student.tistory.com/393
2. https://sm-code.tistory.com/entry/Nginx-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%A0%95%EB%A6%AC