## Reference : [소켓이란? 종류, 통신 흐름, HTTP통신과의 차이](https://velog.io/@newdana01/%EC%86%8C%EC%BC%93%EC%9D%B4%EB%9E%80-%EC%A2%85%EB%A5%98-%ED%86%B5%EC%8B%A0-%ED%9D%90%EB%A6%84-HTTP%ED%86%B5%EC%8B%A0%EA%B3%BC%EC%9D%98-%EC%B0%A8%EC%9D%B4)

<br>

# Socket

## Socket이란?
네트워크를 경유하는 프로세스 간 통신의 종착점.    
OSI 7계층 중 응용 계층에 속하는 프로세스들은 데이터 송수신을 위해 반드시 소켓을 거쳐 전송 계층으로 데이터를 전달해야한다.    
즉, 소켓은 전송 계층과 응용 프로그램 사이의 인터페이스 역할을 하며 떨어져 있는 두 호스트를 연결해준다.

<img src="https://velog.velcdn.com/images/newdana01/post/9b90db1e-11f4-4d17-b8f6-331402801d46/image.png">

## 소켓은 아래의 3 요소로 정의된다.

1. 프로토콜
2. IP
3. Port

## 일반적인 소켓 통신의 흐름

<img src="https://velog.velcdn.com/images/newdana01/post/817b8ba8-4428-4e66-8128-7c01b554f8ff/image.png">


## 서버

1. 소켓 생성
2. 바인딩 (ip, port번호 설정)
3. listen()으로 클라이언트 요청에 대기열을 만들어 몇개의 클라이언트를 대기시킬지 결정
4. accept()로 클라이언트와 연결
5. 데이터 송수신
6. 소켓 닫기

## 클라이언트

소켓 생성
서버에 설정된 ip, port로 연결 시도
accept()로 클라이언트의 socket descriptor 반환
데이터 송수신
소켓 닫기

## 소켓 종류
(1) 스트림 소켓
TCP(Transmission Control Protocol)을 사용하는 연결 지향방식의 소켓
송수신자의 연결을 보장하여 신뢰성있는 데이터 송수신이 가능
데이터의 순서 보장
소량의 데이터보다 대량 데이터 전송에 적합
점대점 연결

<img src="https://velog.velcdn.com/images/newdana01/post/2999a10d-fe3a-4cd4-bf5f-90c2f777a2e9/image.png">

### 서버

소켓 생성
바인딩
listen (연결되지 않은 소켓을 대기모드로 전환)
클라이언트 요청 수락 후 통신을 위한 실질적인 소켓 생성 (처음에 생성한 소켓은 새로운 클라이언트 요청을 대기하기 위해 쓰임)
데이터 송수신
소켓 닫음

### 클라이언트

소켓 생성
서버가 설정한 ip, port로 연결
accept()로 클라이언트의 socket descriptor 반환
데이터 송수신
소켓 닫음

## (2) 데이터그램 소켓
UDP(User Diagram Protocol)을 사용하는 비연결형 소켓
데이터의 순서와 신뢰성을 보장하기 어려움
점대점 뿐만아니라 일대다 연결도 가능

<img src="https://velog.velcdn.com/images/newdana01/post/6d60e795-cd8d-4823-a6a0-bca9deb50cbf/image.png">

accept 과정없이 소켓 생성 후 바로 데이터 송수신


# HTTP 통신과 소켓 통신의 차이

## (1) HTTP 통신
클라이언트의 요청이 있을 때만 서버가 응답
JSON, HTML, Image 등 다양한 데이터를 주고 받을 수 있음
서버가 응답한 후 연결을 바로 종료하는 단방향 통신이지만 Keep Alive 옵션을 주어 일정 시간동안 커넥션을 유지할 수 있다.
실시간 연결이 아닌 데이터 전달이 필요한 경우에만 요청을 보내는 상황에 유리

## (2) 소켓 통신
클라이언트와 서버가 특정 포트를 통해 양방향 통신을 하는 방식
데이터 전달 후 연결이 끊어지는 것이 아니라 계속해서 연결을 유지 → HTTP에 비해 더 많은 리소스 소모
클라이언트와 서버가 실시간으로 계속하여 데이터를 주고받아야하는 경우에 유리
실시간 동영상 스트리밍이나 온라인 게임 등에 사용
