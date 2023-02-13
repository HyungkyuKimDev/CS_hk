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

git add ~(파일명)

> 파일을 작업 디렉터리에서 스테이징 영역으로 이동시킴
> 여러 개의 파일을 이동시키기 위해서는 Ex) git add index.html style.css ~~
> 모든 파일을 이동시키기 위해서는 git add .

- git add . 에서 이동시키고 싶지 않은 파일을 지정하는 방법(효율적인 커밋 방법)
  vim .gitignore을 만든다.(해당 폴더부터 하위 파일이나 폴더까지 영향 끼침)
  이 파일 안에 제외할 파일들을 와일드 카드등으로 저장
  Ex) \*.log // .log 파일은 전부 무시하라

> 파일을 스테이징 영역에서 리포지토리 영역으로 이동시킴(커밋 완료)

git commit

> 스테이징 영역에 이동시킨 파일의 깃 메세지를 입력함
> git commit -m "~" 을 쓰면 에디터를 사용하지 않고 커밋이 가능하다.

git log

> 커밋 기록을 확인할 수 있다.

- commit 옆 영어와 숫자는 커밋의 고유한 아이디이다.
- 다음 작성자와 날짜가 표시되고. 다음으로 커밋 메세지가 표시된다.
- 커밋 메세지의 경우 알기 쉽도록 작성하게 유의하자.

* git log --oneline // 아이디와 커밋 메세지를 간단히 표시
* git log -p // 커밋을 자세히 표시, 커밋 정보(이전에서 변경 사항등등)을 알려준다.
* git log --stat // 변경된 파일 개수 알려줌

git status

> 깃에서 현재 상황(파일이 어느 영역에 있는지 등등)을 확인할 수 있다.
> changes not staged for commit // 파일이 아직 스테이징 영역 또는 커밋에 오지 않았다.
> modified: ~ // ~ 파일에 변경 사항이 발생하였다.(로컬 파일)
> changes to be committed // 파일이 스테이징 영역에서 아직 커밋되지 않았다.

git diff

> 깃에서 파일 변경 사항 자세히 알고 싶을 때 사용
> git diff --cached // 스테이징 영역에 있는 파일이 커밋될 시, 어느 영역이 어떻게 변경되는 지 알려줌

git rm

> 깃에서는 단순히 rm mv로 파일을 삭제하지 않고. git rm / git rv를 사용항 (이동 삭제의 경우 )

git commit --amend

> 깃에서 변경 사항을 굳이 커밋 메세지에 남길 필요가 없을 경우 git add 한 뒤 git commit --amend 한다. 이후 커밋 메세지 변경 여부를 물어본다. :wq 입력하면 마무리

git reset

> 깃을 이전 상태로 돌리기 위해서 사용

- git reset --hard HEAD // 깃을 헤드로 돌린다, 헤드(가장 최신 버전)
- git reset --hard HEAD^ // 깃 헤드 바로 직전 버전으로 돌린다.
- git reset --hard ~(commit ID 최소 7자리) 입력 // 깃을 그 커밋 아이디 버전으로 돌아간다.
- git reset --hard ORIG_HEAD // 가장 최근 변경되 버젼으로 돌아간다.

branch

> 깃의 별개의 버젼을 관리하고 싶을 때 브랜치를 이용한다. 기존의 것은 master이다.

- git branch // 깃 상의 브랜치를 보여준다.
- git branch ~ // ~ 브랜치를 생성해준다.
- git checkout ~ // ~ 브런치로 이동한다.
- git merge ~ // ~ 브런치의 내용을master에 병합시킨다.
- git branch -d ~ // ~ 브런치를 삭제한다.
- git checkout -b ~ // ~ 브런치를 만들어서 전환까지 한다.

* CONFLICT (Content): Merge conflict in ~
  // 브런치에서 수정한 파일과 마스터에서 수정한 파일이 같은 파일인 경우 수정 내용이 달라 커밋 시에 오류가 발생한다.
