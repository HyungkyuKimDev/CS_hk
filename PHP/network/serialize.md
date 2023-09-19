# Serialize

직렬화는 객체나 배열 등 복합형 타입의 데이터를 저장하고 복호화할 수 있도록 문자열 혹은 바이트 배열 형태로 변환하는 것을 말한다.

데이터를 직렬화해서 데이터베이스에 넣거나 파일에 저장하거나 하는 용도로 많이 사용된다.

```PHP
<?php
$data = array(1, 2, 3, 4);
$serial_data = serialize($data);
file_put_contents("data.txt", $serial_data);

$load_data = file_get_contents('data.txt');
$unserial_data = unserialize($load_data);

var_dump($load_data);
echo "<br />";
var_dump($unserial_data);

```

---
PHP에서 직렬화된 데이터는 문자열 타입이다. 저장된 데이터를 그대로 읽은 변수 `$load_data`를 보면 알 수 있다.

```
string(38) "a:4:{i:0;i:1;i:1;i:2;i:2;i:3;i:3;i:4;}"
```

---
php 에서 직렬화는 `serialize` 함수를 사용한다.

```
$serial_data = serialize($data);
```

---
역직렬화는 unserialize 함수를 사용한다.

```
$unserial_data = unserialize($load_data);
```


## Reference : https://wikidocs.net/116893