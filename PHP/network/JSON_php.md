# JSON

```PHP
<?php
$data = array(
    'key1' => `value1`,
    'key2' => 2,
    'key3' => array(
        'name' => 'yse',
        'age' => 105
    )
);

$json_data = json_encode($data);
$decode_object = json_decode($json_data);
$decode_array = json_decode($json_data, true);

var_dump($data);
echo "<br /><br />";
var_dump($json_data);
echo "<br /><br />";
var_dump($decode_object);
echo "<br /><br />";
var_dump($decode_array);
echo "<br /><br />";

```

---
`json_encode` 함수는 PHP 데이터 타입을 JSON 문자열로 바꾼다.

```
$json_data = json_encode($data);
```

```
string(54) "{"key1":null,"key2":2,"key3":{"name":"yse","age":105}}"
```

---
`json_decode` 함수는 JSON 문자열을 PHP 의 객체 형식으로 바꾼다.

```
json_decode($json_data)
```

```
object(stdClass)#1 (3) { ["key1"]=> NULL ["key2"]=> int(2) ["key3"]=> object(stdClass)#2 (2) { ["name"]=> string(3) "yse" ["age"]=> int(105) } } 
```

---
`json_decode` 함수에서 2번째 파라미터에 `true` 를 전달하면 PHP의 객체 대신 배열 형식으로 바꾼다.

```
json_decode($json_data, true)
```

```
array(3) { ["key1"]=> NULL ["key2"]=> int(2) ["key3"]=> array(2) { ["name"]=> string(3) "yse" ["age"]=> int(105) } }
```


## Reference : https://wikidocs.net/116921