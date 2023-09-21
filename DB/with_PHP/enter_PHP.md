# SQL With PHP

## PHP로 SQL 접속하기

```
<?php
function db_get_pdo()
{
    $host = 'localhost';
    $port = '3306';
    $dbname = 'php3min';
    $charset = 'utf8';
    $username = 'php3min';
    $db_pw = "1234";
    $dsn = "mysql:host=$host;port=$port;dbname=$dbname;charset=$charset";
    $pdo = new PDO($dsn, $username, $db_pw);
    return $pdo;
}
```


=>위 코드를 `db.php` 로 저장한다. 이 코드는 데이터베이스 섹션 전반에 쓰인다.

=> php에서 데이터베이스에 접속하기 위해서는 `PDO` 라는 내장 객체를 사용한다. 데이터베이스에 쿼리를 실행할 때마다 늘 똑같이 해야 하는 일이 데이터베이스에 연결하는 것이므로 `db_get_pdo()` 함수를 분리했다.

1. `host` 는 데이터베이스 서버의 주소다. `localhost` 는 본인의 컴퓨터라는 뜻이다.
2. `port` 는 데이터베이스 서버의 포트. MySQL의 데이터가 오가는 통로다.
3. `dbname` 은 데이터베이스 이름이다.
4. `charset` 은 인코딩 방법이다. 대부분 utf8 을 사용한다.
5. `username` 은 데이터베이스 사용자 이름이다.
6. `db_pw` 은 데이터베이스 사용자 비밀번호다.
7. `dsn` 은 데이터베이스 관련 정보를 바탕으로 만든 데이터베이스 연결 문자열이다.
8. `PDO` 객체는 `dsn, 사용자 이름, 사용자 비밀번호` 를 파라미터로 받아서 데이터베이스에 실제로 연결하는 역할을 한다.

* PDO 외에도 mysql_ 계열 함수가 있으나 PHP 7 이상에서 deprecated(사용 권장 안함) 처리되었으므로 사용하지 말자. 


### Reference : https://wikidocs.net/116936