# 유효성 검사

=> 사용자의 입력을 검증하거나 필요한 데이터만 추출하는 방법

---

## 값이 이메일인지 검사


```
$emails = array(
    'aaa@bbb.com',
    'abc',
    '.com',
    '@.com'
);

foreach ($emails as $email) {
    echo "$email : ";
    var_dump(filter_var($email, FILTER_VALIDATE_EMAIL));
    echo "<br />";
}
```

`filter_var($email, FILTER_VALIDATE_EMAIL)` 는 이메일이면 입력 이메일을, 이메일 형식이 맞지 않으면 false 를 리턴한다.

filter_var 함수는 파라미터로 도메인인지 검사하는 FILTER_VALIDATE_DOMAIN 이나, IP를 검사하는 FILTER_VALIDATE_IP, URL 형식을 검사하는 FILTER_VAR_URL 등을 지원한다. 중요 상수는 아래에서 확인할 수 있다.

상수	의미
FILTER_VALIDATE_DOMAIN	도메인 형식인지 검사한다.
FILTER_VALIDATE_EMAIL	이메일 형식인지 검사한다.
FILTER_VALIDATE_FLOAT	실수형인지 검사한다.
FILTER_VALIDATE_INT	정수형인지 검사한다.
FILTER_VALIDATE_IP	IPV4 혹은 IPV6 형식인지 검사한다.
FILTER_VALIDATE_MAC	맥 어드레스 형식인지 검사한다.
FILTER_VALIDATE_REGEXP	올바른 유효성 검사 형식인지 검사한다.
FILTER_VALIDATE_URL	URL 형식인지 검사한다.

### Refernce : https://wikidocs.net/116956