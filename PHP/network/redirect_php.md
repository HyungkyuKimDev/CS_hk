# Redirect

리다이렉트는 다른 페이지로 이동하는 걸 말한다.

```PHP
<?php
header("Location: /target_url");
exit();
```

위 코드를 `redirect.php` 파일에 저장하고 브라우저에서 결과를 확인한다.
`http://localhost/redirect.php`에 접속하면 `http://localhost/target_url`로 이동된다.

---
이때, `http://localhost/target_url`에 해당하는 서버 리소스가 없어서 404 오류가 발생하지만. 페이지 이동은 확인 할 수 있다.

---

http 규약상 다른페이지로의 이동은 http 응답 헤더 (response header) 에 301 혹은 302 코드와 이동할 페이지로의 이동 주소를 함께 보냄으로써 이루어진다. php 는 header 함수를 통해 응답 헤더에 보낼 데이터를 설정한다.

```
header("Location: /target_url");
```

___

`exit()` 는 php 실행을 끝내는 표시다. 이후에 어떤 코드가 있어도 실행하지 않로 응답을 브라우저에 되돌린다.

`exit()` 를 굳이 쓰는 이유는 이후에 나오는 코드가 리다이렉트가 아닌 다른 상태로 바꿀 가능성을 차단하기 위해서이다.

## Reference : https://wikidocs.net/116886