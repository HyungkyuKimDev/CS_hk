# Syntax

## String

---

### 문자열이 특정 문자열로 시작되는지 검사

```
function string_starts_with($input, $value) {    
    return $value === "" ||  mb_strrpos($input, $value, -mb_strlen($input)) !== false;
}

var_dump(string_starts_with("안녕하세요.", "안녕"));
var_dump(string_starts_with("안녕하세요.", "하이"));
```

---

php에서 앞에 mb_ 가 붙는 함수는 멀티바이트(Multi Byte) 를 다루는 함수들이다.
원래 php는 영어를 기준으로 설계되었기 때문에 한글같은 멀티바이트 글자를 잘 처리하지 못한다. 따라서 멀티바이트 글자를 처리하기 위한 함수들이 일부 존재한다.

=> `mb_strrpos` 함수는 input 문자열 안에서 value 문자열의 위치를 오른쪽에서부터 찾는 strrpos의 멀티바이트 버전이다.   
=> `mb_strlen` 함수는 문자열의 길이를 세는 strlen의 멀티 바이트 버전이다.


---

### 문자열이 특정 문자열로 끝나는지 검사

```
function string_ends_with($input, $value)
{
    return $value === "" || (($temp = mb_strlen($input) - mb_strlen($value)) >= 0 && mb_strpos($input, $value, $temp) !== false);
}

var_dump(string_ends_with("안녕하세요.", "하세요."));
var_dump(string_ends_with("안녕하세요.", "하이"));
```

string_ends_with 함수의 첫번째 파라미터는 전체 문자열, 두번째 문자열은 끝나는 문자열이다.
아래 예제는 "안녕하세요" 가 "하세요"로 끝나는지 검사한다.


---

### 문자열이 특정 문자열을 포함하는지 검사

```
function string_contains($input, $value)
{    
    return mb_strpos($input, $value) !== false;
}

var_dump(string_contains("안녕하세요.", "녕하"));
var_dump(string_contains("안녕하세요.", "하이"));
```

---

### 문자열 자르기

```
function string_split($input, $seperater)
{
    return explode($seperater, $input);
}

var_dump(string_split("a,b,c,d,ef,ghi,j", ","));
exit();
```

---

### 문자열 줄 단위로 자르기

```
function string_splitlines($input)
{
    return explode(PHP_EOL, $input);
}

$data = <<<CDATA
안녕
하신가
요?
CDATA;

var_dump(string_splitlines($data));
```

---

PHP_EOL 은 End Of Line 의 약자로 줄바꿈 기호를 의미한다.
줄바꿈 기호는 OS 에 따라 \r\n, \r, \n 등으로 각자 다르다. 윈도우즈는 \r\n을 사용하고, 리눅스 계열은 \n을 쓴다. 맥 OS 9 버전까지는 \r을 사용했었다.
PHP_EOL은 OS 에 따른 줄바꿈 기호를 리턴하는 내장 상수다. 따라서 OS에 따른 줄바꿈 기호 혼용 문제를 해결 가능하다. 즉, 윈도우즈에서는 \r\n, 리눅스 계열에서는 \n을 리턴한다.

---

<<<특정문자 로 시작하고 특정문자; 로 끝나는 문법을 히어닥(heredoc) 이라고 부른다. PHP에서 여러줄 문자열을 쓸 때 사용한다.
한 줄 문자열 "" 와 비슷하게 문자열 안의 변수를 치환한다.

```
$name = 'PHP';
$data = <<<CDATA
안녕
$name
만나서 반가워
CDATA;
```

```
안녕
PHP
만나서 반가워
```

---

히어닥과 비슷한 것으로 <<<'특정문자' 로 시작하고 특정문자; 로 끝나는 나우닥(nowdoc)도 있다. 나우닥은 변수를 치환하지 않는다.

```
$name = 'PHP';
$data = <<<'CDATA'
안녕
$name
만나서 반가워
CDATA;
```

```
안녕
$name
만나서 반가워
```

---

### 문자열 바꾸기

```
function string_replace($input, $old_str, $new_str)
{
    return str_replace($old_str, $new_str, $input);
}

var_dump(string_replace("안녕하세요.", "하세요", "히 가세요"));
```

string_replace 함수의 첫번째 파라미터는 전체 문자열, 두번째 문자열은 원본 문자열. 세번째는 바꿀 문자열이다.

### Reference : https://wikidocs.net/116946