# Session

세션은 서버에 저장되는 접속 클라이언트별 사용자의 정보다.

```PHP
<?php
function redirect($url){
    header('Location: ' . $url);
    exit();
}

session_start();
$action = $_GET['action'];

if ($action == "set"){
    $_SESSION['key'] = 'session_value';
    redirect("?action=get");

}elseif ($action == "get"){
    if (isset($_SESSION['key'])){
        echo $_SESSION['key'];
    }else{
        echo "NO SESSION";
    }
}elseif ($action == "remove"){
    if (isset($_SESSION['key'])){
        unset($_SESSION['key']);
    }
    redirect("?action=get");
}

```

---

1. 처음 세션이 없을 때 http://localhost/session.php?action=get 로 접속한 결과

```
NO SESSION
```

2. 세션 세팅하는 http://localhost/session.php?action=set 결과를 확인한다. 세션을 세팅하고 나서 확인을 위해 http://localhost/session.php?action=get 으로 이동한다.

```
session_value
```

3. 세션 삭제 http://localhost/session.php?action=remove 결과를 확인한다. 세션을 삭제하고 나서 http://localhost/session.php?action=get 으로 이동했다.

위 코드를 `redirect.php` 파일에 저장하고 브라우저에서 결과를 확인한다.
`http://localhost/redirect.php`에 접속하면 `http://localhost/target_url`로 이동된다.

```
NO SESSION
```

---
기술적으로 보면, 세션은 아래와 같이 작동한다.

1. 클라이언트가 서버에 요청한다.
2. 서버는 클라이언트가 보낸 데이터 중 세션키에 해당하는 쿠키가 있는지 확인한다. PHP의 경우 기본값은 PHPSESSIONID이다.
3. 세션 키가 없다면 PHP는 새로운 세션 키를 생성하고 데이터를 서버에 저장한다.
4. 클라이언트에 PHPSESSIONID=세션키 형태의 쿠키를 응답한다.
5. 다음번에 클라이언트가 서버에 요청할 때는 PHPSESSIONID=세션키 형태의 쿠키를 함께 전달하게 된다.
6. PHP는 PHPSESSIONID=세션키 쿠키가 요청 안에 포함되었으므로 기존에 서버에 저장된 데이터를 읽어서 처리할 수 있다.

---

php에서 세션을 사용하려면 `session_start()`` 를 반드시 사용하기 전에 써서 세션을 준비해야 한다. PHP의 기본 세션은 단순한 파일로 저장되기 때문에 파일을 읽어오는 것이다.

---

`$action` 변수는 파라미터에 따라 하는 일을 구분하기 위해 쿼리 스트링으로 입력을 받았다.
`$action` 의 값이 `set` 일 경우 세션을 설정 하고, `get` 일 경우 세션을 가지고 오는 역할 을 하고, `remove` 일 경우 세션을 삭제 하게 된다.

```
$action = $_GET['action'];

if ($action == "set"){
    세션 설정
}elseif ($action == "get"){
    if (세션이 있다면){
        세션을 출력한다.
    }else{
         "NO SESSION" 메세지를 출력한다.;
    }
}elseif ($action == "remove"){
    if (세션이 있다면){
        세션을 삭제한다.
    }
    세션 삭제 후 "?action=get" 주소로 이동한다.
}
```

---
세션은 $_SESSION 글로벌 전역 변수를 통해 사용할 수 있다. 연관 배열 형태이기 때문에 사용법은 연관배열과 동일하다.

세션에 값을 넣기 위해서는 `$_SESSION[세션키] = 세션값` 형태로 쓰면 된다.

```
$_SESSION['key'] = 'session_value';
```

---
세션에서 값을 가져오기 위해서는 `$_SESSION[세션키]` 형태로 가지고 오면 된다.

```
echo $_SESSION['key'];
```

---
세션에 특정 키나 값이 있는지 확인하기 위해서는 `isset($_SESSION[세션키])` 형태로 쓰면 된다. `isset` 은 변수가 존재하는지 확인하는 내장 함수이다.

```
isset($_SESSION['key'])
```

---
세션이 이미 시작했는지 확인하기 위해서는 `isset($_SESSION)` 으로 확인할 수 있다. 세션이 시작해야만 `$_SESSION`변수가 생기기 때문이다. 따라서 `session_start()` 함수를 쓸 때는 보통 아래와 같이 사용한다.

```
if (isset($_SESSION) == false){
  session_start();
}
```

---
세션에서 값을 삭제하기 위해서는 `unset $_SESSION[세션키]` 으로 삭제하면 된다.

```
unset($_SESSION['key']);
```




## Reference : https://wikidocs.net/116888