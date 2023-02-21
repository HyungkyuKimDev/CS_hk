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
\*root 루트는 관리자를 의미한다.

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
* -rw-r--r-- 1 khk36 staff 과 같이 처음 나온 부분은 접근 권한 관련 내용이다. 10글자 중 첫글자는 파일의 종률를 의미한다.
  // -면 일반 파일 , d면 디렉터리, 1 이면 심볼릭이 된다.
  이후 3문자씩 각각 소유 유저의 접근 권한, 소유 그룹의 접근 권한, 다른 사용자의 액세스 권한이 된다.
  r은 읽기 권한 w는 쓰기 권한 x는 실행 가능을 의미한다. 즉 위의 파일은 소유 유저(khk36)는 읽고 쓰고 가능 그룹(staff)과 다른 사용자는 읽기만 가능을 의미한다.
* chmod 커맨드로 접근 권한을 변경할 수 있다. 유저 부분(u) 그룹 부분(g) 다른 사용자 부분(o)로 표시하고 전부를 a로 표시한다 => chmod a=rwxrwxrwx index.html or chmod g=rw, o=rw index.html 로 쓴다.
  => 숫자로도 표시 가능하다. r 2^2 w 2^1 x 2^0이 된다. chmod 777 index.html == chmod rwxrwxrwx index.html => +-를 이용해서도 가능 chomd g+x,o-r index.html

touch

> 파일 생성을 위한 입력어 Ex) touch index.html
> 하위 디렉터리에 파일 생성도 가능 Ex) touch mysite/css/style.css
> 내부 파일까지 복사 된다.

cp

> 파일을 복사하는 경우 Ex) cp index.html profile.html \*디렉터리를 복사하고 싶은 경우 옵션 -r을 이용한다. Ex) cp -r mysite/ myprofile
> Ex) cp /etc/services . => 현 위치에 복사해줙

mv

> 이름을 바꾸는 경우 Ex) mv profile.html about.html => profile > about \*폴더 이름도 바뀌는 거 가능

rm

> 파일을 삭제하는 입력어 Ex) rm about.html
> 폴더 내부까지 전부 삭제하는 경우 옵션 -r을 사용 Ex) rm -r myprofile/

mkdir

> 디렉터리를 만드는 입력어 EX) mkdir mysite \*같은 디렉터리 안에 있는 파일과 폴더에서, 그 파일을 폴더에 넣는 입력 Ex) mv index.html mysite/ \*옵션 ls -p 하고 디렉터리를 만들면 계층으로 만들 수 있다. Ex) mkdir -p mysite/css

rmdir

> 디렉터리를 삭제하는 명령어 Ex) rmdir myprofile/ \*단, 디렉터리 안이 비어있어야 사용이 가능하다.

ln

> (심볼릭)폴더의 별명을 만들어서 상위 디렉터리를 이용하지 않고 바로 이동할 수 있도록 한다. 파일에도 사용가능
> Ex) ln -s myapp/css/common/ mycommon

- rm 별명 > 심볼릭 제거 가능

cat

> 파일의 내용을 읽기 위해 사용 Ex) cat (파일명)

more

> 파일 정보 읽는 걸 페이지 별로 하고 싶은 경우 사용 Ex) more (파일명) // 페이지를 이동하는 경우 스페이스바를 누른다.
> q를 누르면 종료 가능하다.

less

> more과 같이 파일 정보를 페이지 별로 읽을 수 있도록 한다. /(파일명)을 치면 그 파일 위치를 찾아주고. n을 입력하면 다음 그 파일 이름 위치를 찾아준다.

wc

> 파일 내 행의 수 / 단어의 수/ 바이트의 수 / 파일 명을 출력해줌
> wc -l 의 경우 행의 수만 표시 됨

head

> 파일 앞 부분만 보고 싶은 경우 head -(보고싶은 행의 수) 파일명 입력
> Ex) head -3 services

tail

> head 와 정 반대 파일 뒷 부분만 보고싶은 경우

history

> 입력한 명령어 기록을 확인 => !3 세번째 명령어 실행 // !! 직전 명령 실행 // !-2 2개 전의 명령을 실행 \*직전 명령에서 사용된 인수는 !$로 표시할 수 있다. Ex) cd /etc/ 한 뒤 cd !$ 하면 cd /etc/를 의미한다.

- !pw를 치면 최근 친 명령어 중 pw로 시작되는 명령어를 실행할 수 있다. + :p를 치면 실행하지 않고 명령 표시만 하는 것도 가능하다.

* ctrl + R 누르면 검색도 가능하다. 또 ctrl + R을 누르면 다음 후보로 이동 할 수 있다.

유닉스 유저 관리

cat /etc/passwd

> 첫 부분이 이름 : 암호 : 사용자 ID : 사용자 그룸 ID : 주석 : 홈 디렉터리 위치 및 쉘 명령어 // 로 표시됨

groups ~~

> 유저 ~~가 속한 그룹을 확인할 수 있다. // 루트의 경우 권한이 필요함

sudo

> 루트 사용자의 권한을 일시적으로 이용하는 입력어

- vi

> UNIX의 편집기 i를 누르면 편집 모드가 된다. 명령 모드로 돌아가려면 esc 키를 누르면 된다. 종료는 :q이다.

- #!/bin/ash => #!는 이 다음 작성되는 프로그램을 실행하라는 의미가 된다.
  echo 'hello There!' => echo는 문자열을 표시하는 커맨드 이고, 문자열에 공백이 있는 경우 ''을 이용한다.

- 저장하고 싶은 경우 :wq , 저장하고 싶지 않은 경우 :q! 가 된다.
- 커맨드 줄 삭제는 대문자 D

- 커맨드를 실행할 떄는 해당 위치를 정확하게 표시하는 편이 좋다. Ex) ./hello
- 커맨드를 찾는 건 환경 변수라는 구조로 관리되어 있고, echo $PATH를 통해 확인할 수 있다.
- export 환경 변수를 설정하기 위한 명령어 Ex) export PATH=/home/dotinstall:$PATH
  => PATH라는 이름의 디렉터리와 설정되어 있는 $PATH의 내용을 연결해 설정하라
  => 이렇게 하면 환경 변수 $PATH에 /home/dotinstall가 추가된다.
  => 이후 이 커맨드는 해당 위치가 아니라 그냥 명령어를 입력해도 실행이 가능해진다. hello
- 디렉터리나 파일을 찾는 법은 which ~ 하면 된다.

- echo 'date' 하면 date 문자열이 입력된다. 이 문자열을 파일에 넣고 싶으면 echo 'date' > commands.txt하면 된다.
- 또 다른 echo로 문자열을 입력하면 파일에 덮어쓰기가 된다. 덮어쓰기 하지 않고 다음 행에 넣고 싶으면 >> 를 사용한다.
- 다른 쉘 커맨드 넣는 것도 가능하다. /bin/ash < commands.txt
- 추가로 이걸 파일에 넣고 싶으면 /bin/ash < commands.txt > results.txt

파이프(パイプ）

- 명령 실행의 결과를 파일이 아닌 다른 명령에 전달하는 방법 명령 사이에 | 을 사용한다.

* Ex) /etc 속성을 찾고 여기서 'sudo' 문자열 포함 행을 분류하고 싶으면 가각 ls -l /etc , grep 'sudo'이다.
  이걸 한번에 하려면 | 를 써서, ls -l /etc/ | grep 'sudo'
* 파이프는 여러 개도 가능하며 마지막에 파일에 저장하고 싶으면 > 파일명 하면 된다.

브레이스 전개(ブレイス展開）

> echo {1..10}{a..g} ＝＞ 1a 1b 1c .. 1g 2a .. 10g 이렇게 출력이 된다.

- mkdir test && cd test => test 디렉터리를 만들어서 이동하라
- mkdir app{1..5} 하면 app1 app2 .. app5 까지 디렉터리가 생성된다.
- 파일의 경우도 동일한데 touch app{1..5}/test{1..3}{.jpg,.png,.gif} => app 폴더 1~5 까지 만들고 각각 폴더 안에는 test1.jpg , test1.png, test1.gif ~~ test3.png 까지 생성된다.

find

> 파일 검색 명령어 Ex) find test -name 'app.pmg' => test 폴더에서 이름이 app.png 인 거 찾기

- 와일드카드를 쓰면 Ex) find test -name 'appl\*'
- 마지막에 -type f 를 쓰면 파일만 검색 -type d 면 폴더만 검색
