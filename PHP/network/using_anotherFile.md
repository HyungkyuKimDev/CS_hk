# Another File

php 에서 다른 php 파일을 불러올 때 쓰는 명령어는 include, include_once, require, require_once 4개가 있다.

1. `include` 는 파일이 없어도 경고만 나올 뿐 PHP는 계속 동작한다. 파일 하나가 여러번 호출되면 호출되는 횟수만큼 파일을 포함시킨다.

2. `include_once` 는 파일이 없어도 경고만 나올 뿐 PHP는 계속 동작한다. 파일 하나가 여러번 호출되어도 처음 한번만 파일을 불러온다.

3. `require` 는 파일이 없으면 오류가 나며 PHP의 실행이 완전히 멈춘다. 파일 하나가 여러번 호출되면 호출되는 횟수만큼 파일을 포함시킨다.

4. `require_once`는 파일이 없으면 오류가 나며 PHP의 실행이 완전히 멈춘다. 파일 하나가 여러번 호출되어도 처음 한번만 파일을 불러온다.

```PHP
<?php

include("inc.php");

include_once("inc.php");

require("before.php");

require_once("inc.php");

```

---
php에서 `require` 는 단순히 다른 파일을 내 파일의 일부처럼 가지고 온다는 뜻이다. 불러오는 순간 전역변수와 함수와 클래스등 모든 것이 현재 스택이 존재하는 스코프 안에서 동작한다.

---
만약 `require_once` 혹은 `include_once` 를 사용할 때 만약 함수 내부 등 제한된 스코프에서 사용되면 불러온 변수 등은 현재 스코프가 끝나는 순간 없어진다. 만약 함수가 한번 더 호출되어도 `_once` 여서 다시 한번 `include` 나 `require` 가 동작하지 않기 때문에 변수가 현재 스코프에서 불러지지 않아 오류가 나는 경우가 있으므로 유의해야 한다.


## Reference : https://wikidocs.net/116895