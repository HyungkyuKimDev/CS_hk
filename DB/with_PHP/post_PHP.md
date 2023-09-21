# SQL With PHP

## PHP로 SQL 값 입력하기

```
function db_insert($query, $param = array())
{
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $result = $st->execute($param);
        $last_id = $pdo->lastInsertId();
        $pdo = null;
        if ($result) {
            return $last_id;
        } else {
            return false;
        }
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}

var_dump(
    db_insert(
        "insert into tbl_person (name, age) values (?,?)",
        array("php", 25)
    )
);

// 실행 확인 후 삭제 시작
var_dump(
    db_insert(
        "insert into tbl_person (name, age) values (:name,:age)",
        array("name" =>"php7", "age" => 5)
    )
);
// 실행 확인 후 삭제 끝
```

=> 위 코드는 `db_get_pdo()` 함수를 사용하므로 db.php 파일 아래에 이어붙인다.

=> 브라우저에서 결과를 확인한다.

```
string(1) "2" string(1) "3" 
```

=> 브라우저에서 결과를 확인한 후에는 `var_dump` 부분은 삭제한다.

---

$pdo->lastInsertId() 메소드는 자동으로 설정되는 PK 를 가지고 온다.

```
$last_id = $pdo->lastInsertId();
```

---

`db_insert` 함수는 성공할 경우 `PK` 를, 실패할 경우 `false` 를 반환하므로 `=== false` 체크 후 사용하면 된다.

### Reference : https://wikidocs.net/116938