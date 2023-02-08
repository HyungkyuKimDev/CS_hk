UNIX

기본
:
UNIX는 OS의 일종으로, Windows나 macOS와 달리 서버용으로 자주 사용된다.
UNIX에는 여러 OS가 있는 데, 그 중에서 가장 널리 사용되는 것이 LINUX이다.
리눅스에는 여러 배포 형식(Distribution)이 있다.
Ex) Red Hat Enterprise Linux, CentOS, Debian, Ubuntu, Alpine 등등이 있다.
기본적으로 커멘드는 POSIX라는 규격으로 통일되어 있다.

Windows 나 macOS에서 사용되는 인터페이스. 마우스를 통해 조작하는 인터페이스를
GUI (Graphical User Interface)

명령만으로 조작하는 인터페이스를
CUI (Character-based User Interface)
=> CUI로 작업하는 편이 ㅇ훨씬 효율적이므로 자동화가 싶기 때문에 사용한다.

LINUX 실행 환경
:
쉘 프로그램이 가동됨. 표현되어 있는 부분은 쉘의 프롬프트로서 로그인 유저명 콜론 지금의 위치가 표현되었다. Ex) unixUser:~ $
달러 표시는 관리자 사용자가 아니라 일반 사용자임을 나타낸다.

커맨드
:
date => 날짜를 알려줌
cal => 달력 표시
화살표 위 아래 => 이전 이후 사용한 명령 기록 표시
ctrl + c => 명령 실행 안 하고 새 프롬프트로 이동
control + u => 치던 명령 지우기
clear : 화면 초기화
contrl + l : 화면 초기화

CUI디렉터리(=GUI의폴더) 구성
:
디렉터리 하위 디렉터리는 서브 디렉터리라고 한다.
가장 상위의 디렉터리는 /로 표현하고 root 디렉터리라고 한다.
서브 디렉터리로 자주 사용되는 것은 etc home var 등등이 있다.
etc는 설정 파일 저장 디렉터리 , home은 유저가 잘 사용하는 디렉터리, var은 어플케이션이 관리하는 데이터 저장하는 디렉터리로 웹 사이트 데이터베이스의 데이터 log 파일을 저장하는데 사용한다.
한 하위 서브디렉터리(Ex dotinstall)로 유저가 로그인했을 때, dotinstall 디렉터리는 dotinstall 유저의 hoem 디렉터리라고 한다.
또한 bin , sbin에는 커맨드용 실행 파일이 들어가는 디렉터리, tmp는 임시 파일 저장 디렉터리

디렉터리 명령 표현 방법
:
절대 경로(PATH)

> 루트 디렉터리 / 부터 시작. Ex) /home/dotinstall (루트 디렉터리 > home > dotinstall)
> *현재 로그인 되어 있는 유저의 home 디렉터는 자주 사용되므로 ~라는 기호로 경로로 표시한다
> *루트 디렉터로 이동할 떄는 cd / 로 한다.

상대 경로(PATH)

> 현재 dotinstall 디렉터리에 있는 경우 현재 디렉터리는 . 로 표현
> 그 위 하나 상위 디렉터리는 .. 로 표
> /home/dotinstall가 /etc에 가는 경우에는 ../../etc로 표현한다.

pwd

> 입력 시, 현 위치를 표시해 준다.

그냥 cd

> 입력 시, 홈디렉터리로 이동한다.

cd + tab

> cd 입력 후 탭 누르면 ls 처럼 이동 가능 디렉터리를 표시해준다.

cd ..

> 상위 디렉터리로 이동한다. \*상대 패스의 경우
> cd ../ 인 경우 여기 상위 폴더를 의미한다. cd ../ tab 하면 상위 폴더에서 갈 수 있는 디렉터리를 표시해준다.

ls

> 현재 디렉터리 들을 볼 수 있다.

- -a 하면 옵션을 통해 숨겨진 파일을 볼 수 있다. .으로 시작하는 파일은 숨겨진 파일이다.
  옵션은 여러 옵션을 복수 적용할 수도 있다. 순서와 중요하지 않다. (EX) ls -al == ls -la\_

* 옵션을 알고싶으면 ls --help 하면 된다.
* ls에 대해서 알고싶으면 man ls 하면 설명이 나온다.
* ls -l을 통해서 여러 파일 정보를 볼 수 있는데, 필요 정보를 추출하는 것을 와일드 카드 라고 한다.
  ls -l _.~ 구조로 . 뒤에 파일 형식을 입력하면 추출할 수 있다.
  또 특정 알파벳으로 시작하는 파일을 추출할 수 있는데. 이때 글자수에 해당하는 캐릭터는 ?로 표시한다.
  Ex) s로 시작하는 6글자 항목을 표시하고 싶음 => ls -l s?????
  문자 범위 예컨대 a부터 g까지 시작하는 항목을 6글자 항목을 표시하고 싶으면 []안에 넣으면 된다. Ex) ls -l [a-g]?????
  글자 수 범위 안하면 ls -l [a-g]_ // p 또는 s 의 경우 ls -l [ps]?????
  특정 문자열을 가지고 있는 것은 {}로 추출한다. ls -l {sh,ho}\*

touch

> 파일 생성을 위한 입력어 Ex) touch index.html

cp

> 파일을 복사하는 경우 Ex) cp index.html profile.html

mv

> 이름을 바꾸는 경우 Ex) mv profile.html about.html => profile > about

rm

> 파일을 삭제하는 입력어 Ex) rm about.html
