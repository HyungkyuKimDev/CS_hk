# Password

아무도 복호화할 수 없도록 비밀번호를 단방향으로 암호화하고 추후 검증시 올바른 암호인지 확인하는 방법을 알아본다.

```PHP
<?php

$origin_pw = "1234asdf";
$hash_pw = password_hash($origin_pw, PASSWORD_BCRYPT);

$match = password_verify($origin_pw, $hash_pw);
$not_match = password_verify($origin_pw . "zxcv", $hash_pw);

var_dump($origin_pw);
echo "<br />";
var_dump($hash_pw);
echo "<br />";
var_dump($match);
echo "<br />";
var_dump($not_match);
echo "<br />";

```

위 코드를 `pw_hash.php` 파일에 저장하고 브라우저에서 결과를 확인한다.

```
string(8) "1234asdf" 
string(60) "$2y$10$NGaX1nkkf1jChwrGrMpisO9g5a44mI1jcKle5WIA.34vABfBnY6ru" 
bool(true) 
bool(false) 

```

---
비밀번호 암호화는 관리자도 알 수 없도록 단방향 암호화를 해야 한다. 단방향 암호화는 다시 원래 암호로 되돌릴 수 없는 암호화다.

`password_hash` 함수는 암호화 함수다. `PASSWORD_BCRYPT` 옵션은 암호화에 `Bcrypt` 알고리즘을 사용한다는 의미다.

```
password_hash($origin_pw, PASSWORD_BCRYPT)
```

---
단방향 암호화기 때문에 원래 암호가 뭔지는 아무도 모른다. 따라서 검증을 위한 비밀번호와 암호화된 비밀번호를 함께 입력받아서 정상 비밀번호인지 확인하는 `password_verify` 함수가 존재한다.

```
password_verify($origin_pw, $hash_pw);
```

---
암호가 원래 암호가 같은지 확인하는 예제는 아래와 같다.

```
$match = password_verify($origin_pw, $hash_pw);
```

---
암호가 원래 암호와 다른지 확인하는 예제는 아래와 같다.

```
$not_match = password_verify($origin_pw . "zxcv", $hash_pw);
```

## Reference : https://wikidocs.net/116891