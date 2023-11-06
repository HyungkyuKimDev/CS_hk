# Git Commit Rule

<Br>

## Title

- Tag

    - Feat	새로운 기능 추가
    - Fix	에러 수정
    - Design	CSS 등 UI 디자인 변경
    - BREAKING CHANGE	중대한 API 변경
    - HOTFIX	급하거나 치명적인 에러 수정
    - Style	코드 포맷 변경, 세미 콜론 누락하여 추가했으나 코드 수정은 없음
    - Refactor	코드를 리팩토링한 경우
    - Comment	주석을 추가하거나 변경한 경우
    - Docs	문서 수정
    - Test	테스트 코드 추가, 변경, 리팩토링
    - Chore	기타 변경사항 (빌드 스크립트 수정, 패키지 매니징 설정 등)
    - Rename	파일 or 폴더명 수정 이동
    - Remove	파일 삭제

- [Tag] : [Summary Message] 형식

<br>

## Body

본문은 한 줄 당 72자 이내로 작성한다.

<br>

## Footer

- issue tracker
    - Fixes: 이슈 수정중 (아직 해결되지 않은 경우)
    - Resolves: 이슈를 해결했을 때 사용
    - Ref: 참고할 이슈가 있을 때 사용
    - Related to: 해당 커밋에 관련된 이슈번호 (아직 해결되지 않은 경우)

<br>

## Example

<pre>
<code>
Feat: 사용자 인증 기능 구현

- OAuth 연동
- 회원가입과 로그인 로직 구현
- 로그인, 회원가입 폼 컴포넌트 구현

Fixes: #13
Resolves: #11, #12
Ref: #10
Related to: # 14
</code>
</pre>

<pre>
<code>
fix: fix foo to enable bar

This fixes the broken behavior of the component by doing xyz. 

BREAKING CHANGE
Before this fix foo wasn't enabled at all, behavior changes from <old> to <new>

Closes D2IQ-12345
</code>
</pre>


### Reference
1. [How to Write Better Git Commit Messages – A Step-By-Step Guide](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)   
2. [life-code.log](https://velog.io/@dkdlel102/Git-%EC%BB%A4%EB%B0%8B-%EB%A9%94%EC%8B%9C%EC%A7%80-%EC%BB%A8%EB%B2%A4%EC%85%98)
