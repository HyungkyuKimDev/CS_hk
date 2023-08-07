# nc command (netcat)

Reference : [쵸코쿠키의 연습장, Linux : Netcat (nc) 명령어, 사용 방법, 예제](https://jjeongil.tistory.com/1600)

## Netcat Index

Netcat(ornc)은 TCP 또는 UDP 프로토콜을 사용하여 네트워크 연결을 통해 데이터를 읽고 쓰는 명령줄 유틸리티이다.  

Netcat은 교차 플랫폼이며 리눅스, MacOS, 윈도우즈 및 BSD에서 사용할 수 있다.
또한, 네트워크 연결을 디버그 및 모니터링하고, 열린 포트를 검사하고, 데이터를 전송하고, 프록시로 사용하는 등의 작업을 수행할 수 있다.

Netcat 패키지는 MacOS 및 Ubuntu, Debian 또는 CentOS와 같은 널리 사용되는 Linux 배포에 설치되어 있다.


## Netcat Syntax

```
nc [options] host port
```

Ubuntu에서는 netcat 또는 nc를 사용할 수 있다. 둘 다 openBSD 버전에 대한 symilinks이다.

기본적으로 Netcat은 지정된 호스트 및 포트에 대한 TCP 연결을 시작한다. UDP 연결을 설정하려면 -u 옵션을 사용한다.

```
nc -u host port
```

### 포트 검색

포트 검색은 Netcat의 가장 일반적인 용도 중 하나이다. 단일 포트 또는 포트 범위를 검색할 수 있다.

예를 들어 20-80 범위의 열린 포트를 검색하려면 다음 명령을 사용한다.

```
nc -z -v 10.10.8.8 20-80

# nc: connect to 10.10.8.8 port 20 (tcp) failed: Connection refused
# nc: connect to 10.10.8.8 port 21 (tcp) failed: Connection refused
# Connection to 10.10.8.8 22 port [tcp/ssh] succeeded!
# nc: connect to 10.10.8.8 port 23 (tcp) failed: Connection refused
# ...
# nc: connect to 10.10.8.8 port 79 (tcp) failed: Connection refused
# Connection to 10.10.8.8 80 port [tcp/http] succeeded!
```

-z 옵션은 nc에 데이터를 보내지 않고 열린 포트만 검색하도록 지시하고 -v 옵션은 보다 자세한 정보를 제공한다.

열린 포트가 있는 라인만 인쇄하려는 경우 grep 명령을 사용하여 결과를 필터링할 수 있다.

```
nc -z -v 10.10.8.8 20-80 2>&1 | grep succeeded

# Connection to 10.10.8.8 22 port [tcp/ssh] succeeded!
# Connection to 10.10.8.8 80 port [tcp/http] succeeded!
```

Netcat을 사용하여 서버 소프트웨어 및 해당 버전을 찾을 수도 있다. 예를 들어 "EXIT"를 보내는 경우이다. 명령은 기본 SSH 포트 22에서 서버에 전달된다.

```
echo "EXIT" | nc 10.10.8.8 22

# SSH-2.0-OpenSSH_7.6p1 Ubuntu-4
# Protocol mismatch.
```

UDP 포트를 검색하려면 아래 나온 것처럼 명령에 -u 옵션을 추가하면 된다.

```
nc -z -v -u 10.10.8.8 20-80
```

일반적으로 Nmap은 Netcat보다 복잡한 포트 검색에 더 적합한 도구이다.

### Netcat을 통해 파일을 전송

Netcat은 기본 클라이언트/서버 모델을 생성하여 호스트 간에 데이터를 전송하는 데 사용할 수 있다.

이는 수신 호스트의 특정 포트(-l 옵션 사용)를 수신하도록 Netcat을 설정한 다음 다른 호스트로부터 정기적인 TCP 연결을 설정하고 이 포트를 통해 파일을 전송함으로써 작동한다.

수신 시 다음 명령을 실행하여 수신 연결을 위해 포트 5555를 열고 출력을 파일로 리디렉션한다.

```
nc -l 5555 > file_name
```

송신 호스트에서 수신 호스트에 연결하고 다음 파일을 보낸다.

```
nc receiving.host.com 5555 < file_name
```

디렉토리를 전송하려면 tar를 사용하여 소스 호스트의 디렉토리를 아카이브하고 대상 호스트에서 아카이브를 추출할 수 있다.

수신 호스트에서 포트 5555의 들어오는 연결을 수신하도록 Netcat 도구를 설정한다. 들어오는 데이터는 tar 명령에 파이프로 연결되어 아카이브를 추출한다.

```
nc -l 5555 | tar xzvf -
```

송신 호스트에서 디렉토리를 패킹하고 수신 호스트의 수신 nc 프로세스에 연결하여 데이터를 전송한다.

tar czvf - /path/to/dir | nc receiving.host.com 5555

### 단순 채팅 서버를 생성

두 개 이상의 호스트 간에 온라인 채팅을 생성하는 절차는 파일을 전송할 때와 동일하다.

첫 번째 호스트에서 Netcat 프로세스를 시작하여 포트 5555에서 수신 대기한다.

```
nc -l 5555
```

두 번째 호스트에서 다음 명령을 실행하여 수신 포트에 연결한다.

```
nc first.host.com 5555
```

이제 메시지를 입력하고 ENTER를 누르면 두 호스트에 모두 표시된다.

연결을 닫으려면 CTRL+C를 입력한다.

### HTTP 요청을 수행

curl과 같이 HTTP 요청에 훨씬 더 나은 도구가 있지만 Netcat을 사용하여 다양한 요청을 원격 서버로 전송할 수도 있다.

예를 들어 OpenBSD 웹 사이트에서 Netcat man 페이지를 검색하려면 다음과 같이 입력한다.

```
printf "GET /nc.1 HTTP/1.1\r\nHost: man.openbsd.org\r\n\r\n" | nc man.openbsd.org 80
```

HTTP 헤더와 HTML 코드를 포함한 전체 응답이 터미널에 출력한다.

