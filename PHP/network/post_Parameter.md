# POST Parameter

HTTP POST 메소드로 전달된 파라미터 읽기

```PHP
<form method="post">
    name : <input type="text" name="name" />
    age : <input type="text" name="age" />
    <input type="submit" />
</form>

<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $age = $_POST['age'];

    echo "name is $name, age is $age";
}
?>
```

위 코드를 파일에 저장하고 브라우저에서 결과를 확인한다.   
`name` 에 `aaa` 를, `age`에 `222`를 입력하고 제출한다.

```
name is aaa, age is 222
```

위와 같이 출력된다.

---

HTTP 메소드는 크게 9개가 있고. 브라우저에서는 GET POST 2개를 주로 사용한다.
1. GET은 데이터를 읽을 때, POST는 데이터를 저장 수정 삭제하는 역할
2. GET 요청은 주소창에 파라미터를 담아 서버에 요청 보낸다.
3. POST 요청은 파라미터가 Body에 실려서 서버에 전송되기 때문에 주소창에 변화는 없다.

---

`<?php`가 나오기 전까지는 php 엔진은 일반 html로 인식하고 처리를 하지 않는다.

`<form>` 태그 안에 `method='POST'` 속성으로 http 메소드를 POST로 결정한다.

`<form>` 태그에 다른 속성이 없으면 기본 HTTP 메소드는 `GET`이다.

---

`<input>` 태그는 html 사용자 입력을 나타내는 태그다. `name` 속성을 키로 `value` 속성을 값으로 서버에 전달한다.

```
<input type="text" name="name />
```

---

`$_SERVER['REQUSET_METHOD]`는 PHP에서 요청 HTTP 메소드를 읽는다.

```
 if ( $_SERVER['REQUEST_METHOD'] == 'POST' ) {
    // HTTP 메소드가 POST 일 때 실행되는 부분
 }
```

요청 메소드 결과가 `POST` 일 때, `if` 문이 실행되어 아래 코드 블럭이 실행된다.

---

전달된 파라미터는 `$_POST`로 읽을 수 있다.

```
$name = $_POST['name'];
$age = $_POST['name'];
```

`$_POST`는 연관배열 타입으로 `$_POST[파라미터 이름]` 형식으로 HTML에서 입력한 데이터를 읽는다.

## Reference : https://wikidocs.net/116884