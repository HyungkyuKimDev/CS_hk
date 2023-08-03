<?php

include __DIR__."/PHP/IncludeRequire.php";


/* include & require 

 공통점 : 다른 파일에 해당 php 파일의 내용을 사용한다는 점에서 동일

차이점 :

- requrie
 - 해당 파일이 없는 경우, require 부분에서 실행되지 않고 에러가 출력됨
- include
 - 해당 파일이 없는 경우, include 부분 뒤는 실행된다. 에러는 출력되나 이어서 실행됨.

 */

 /* 일반적 디렉토리 구성
공개되어도 상관 없는 파일의 경우
=> html 폴더에 저장

공개되면 안 되는 파일의 경우
=> template 폴더에 저장

서버를 작동할 경우, html 폴더에서 작동시켜 공개되어도 상관 없는 부분만 보여지도록 한다.
공개 되면 안 되는 파일의 경우, include 나 require을 이용해서 사용하자.
 */

?>


