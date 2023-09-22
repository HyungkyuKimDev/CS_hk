# 유효성 검사

=> 사용자의 입력을 검증하거나 필요한 데이터만 추출하는 방법

---

## 값이 비어있는지 검사

```
<?php
function valid_required($input)
{
    return is_array($input) ? empty($input) === False : trim($input) !== '';
}

var_dump(valid_required(""));
var_dump(valid_required(array()));
var_dump(valid_required("php"));
var_dump(valid_required(array(1)));
```

변수가 존재한다는 가정 하에 `(isset($var) === true)` 변수의 값이 빈 문자열("") 이거나 빈 배열이면 거짓(false) 아니면 (true) 를 반환하는 함수를 작성한다.

---

파라미터가 배열이라면 배열이 비어있는지 검사한다.

```
is_array($input) ? empty($input)
```

`is_array` 함수는 배열인지 검사하는 함수다.
`empty`는 값이 비어있는지 검사하는 함수다.


---

문자열이라면 좌우 공백을 제거했을 때 빈 문자열인지 검사한다.

```
trim($input) !== ''
```
=> trim ; 좌, 우 공백을 제거한다. 비슷한 함수로 ltrim 함수는 왼쪽의 공백만 제거하고, rtrim 함수는 오른쪽의 공백만 제거한다.

---

따라서 valid_required 함수를 유사 코드(pseudo code)로 표현하면 아래와 같다.
배열이면 ? 배열이 비어있지 않을 것 : 아니면 좌우 공백을 제거했을 때 빈 문자열이 아닐 것.

---

보통 파라미터로 들어온 값이 있는지 유효성을 검증하기 위해 쓰인다. 예를 들어 쿼리스트링으로 param이라는 키를 가진 값이 서버로 전달되었는지 확인하는 코드는 아래와 같다.

```
$is_valid_required = isset($_GET['param']) && valid_required($_GET['param']);
```

&& 기호는 앞의 결과가 참(true)일 때만 다음 표현을 실행한다. 이유는 &&는 앞 뒤 둘 다 참이어야 참을 나타내기 때문에 앞의 결과가 거짓(false) 이라면 뒤의 것이 참이든 거짓이든간에 결과적으로는 거짓이기 때문이다.
이런 &&의 특성을 이용해서 값이 있다면 값이 비어있는지 검사할 수 있게 된다.

---

함수를 조금 더 추상화해 보자. 쿼리 스트링이 꼭 있어야 하는지 유효성 검사를 하는 함수를 작성한다.

```
function valid_required_get($key){
    return isset($_GET[$key]) && valid_required($_GET[$key]);
}
```

```
$is_valid_required = valid_required_get("param");
```

### Refernce : https://wikidocs.net/116954