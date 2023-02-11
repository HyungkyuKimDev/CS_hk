git

파일 저장의 흐름

1.  작업 디렉터리

    > 파일 작성 수정

2.  스테이징 영역 (인덱스)

    > 작성한 파일을 리포지토리에 저장하기 전에 중간 단계(리포지토리에 효율적으로 저장하기 위해)

3.  리포지토리(로컬 / 원격)
    > 혼자 작성할 때는 로컬 리포지터리에 저장해 버젼을 저장하거나 하고. 팀 단위의 경우 원격을 이용한다.

깃 기본 설정
:
유저 이름 / 유저 이메일 설정

> git config --global user.name " ~ "  
> git config --global user.email " ~ "

- 설정 확인은 git config -l 로 함
- git config 사용법은 git help config 이용

git init

> 현재 디렉터리를 깃으로 이용하겠다는 명령
