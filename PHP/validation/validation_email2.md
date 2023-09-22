# 유효성 검사

=> 사용자의 입력을 검증하거나 필요한 데이터만 추출하는 방법

---

## 값이 이메일 형식만 남기고 삭제하기


```
<?php

$emails = array(
    'aaa@bbb.com',
    'abc',
    '.com',
    '@.com',
    'aaa@bbb.com ds'
);

foreach ($emails as $email) {
    echo "$email : ";
    var_dump(filter_var($email, FILTER_SANITIZE_EMAIL));
    echo "<br />";
}
```


`filter_var($email, FILTER_SANITIZE_EMAIL)` 는 이메일 형식에는 쓸 수 없는 글자들을 모두 삭제한다. 허용하는 글자는 `일반 글자, 숫자,!,#,$,%,&,',*,+,-,=,?,^,_,{,|,},~,@,.,[,]` 이다.



### Refernce : https://wikidocs.net/116961