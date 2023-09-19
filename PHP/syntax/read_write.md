# File Read Write

php 는 디스크의 파일을 읽고 쓸 수 있는 기능을 제공한다.

```PHP
<?php
$data = "hi";
file_put_contents("data.txt", $data);

$load_data = file_get_contents('data.txt');

echo $load_data;

```

---
데이터를 파일로 저장할 때는 `file_put_contents` 함수를 사용한다.

```
file_put_contents("data.txt", $data);
```

---
데이터를 파일에서 읽어올 때는 `file_get_contents` 함수를 사용한다.

```
echo file_get_contents('data.txt');
```


## Reference : https://wikidocs.net/116892