# GET Parameter

브라우저에서 서버에 요청하기 위해, 부가적 정보인 `파라미터`를 요청한다.   
PHP에서는 브라우저가 서버에 요청시 전달한 파라미터를 읽어 처리한다.

```PHP
<?php

$name = $_GET['name'];
$age = $_GET['age'];

echo "name is $name, age is $age";
```

---

브라우저에서 주소창으로 전달하는 GET 파라미터는 `?`로 시작하고, 각 항목은 `키:값` 형태로 구성하며 항목간의 연결에는 `&` 로 표시한다. 이를 `쿼리스트링(Query String)`이라고 한다.

주소창으로 전달되는 쿼리스트링 파라미터는 PHP에서 연관배열 형식인 `$_GET` 슈퍼 글로벌 변수를 이용 `$_GET[파라미터키]` 형식으로 읽을 수 있다.

위에서는 파라미터 `name=yse`를 `$_GET['name']`으로, `age==22` 파라미터는 `$_GET['age']`로 주소창의 파라미터를 읽었다.

## Reference : https://wikidocs.net/116883