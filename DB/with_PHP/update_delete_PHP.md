# SQL With PHP

## PHP로 SQL 값 수정 / 삭제

```
function db_update_delete($query, $param = array())
{
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $result = $st->execute($param);
        $pdo = null;
        return $result;
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}

// 확인 후 삭제 시작
var_dump(
    db_update_delete(
        "update tbl_person set age=:age where person_id = :person_id", 
        array("age" => 4, "person_id" => 1) 
    )
);

var_dump(
    db_update_delete(
        "delete from tbl_person where person_id = ?", 
        array(3) 
    )
);
// 확인 후 삭제 끝
```

위 코드는 db_get_pdo() 함수를 사용하므로 db.php 파일 아래에 이어붙인다.

```
bool(true) bool(true) 
```

브라우저에서 결과를 확인한 후에는 var_dump 부분은 삭제한다.

---

수정 / 삭제는 각자 쿼리문은 다르지만 php에서 처리하는 부분은 동일하다. 따라서 하나의 함수 `db_update_delete` 에서 처리한다.

수정 / 삭제는 특별히 리턴할 값이 없기 때문에 `db_update_delete` 함수는 성공/실패 여부를 반환한다.

### Reference : https://wikidocs.net/116938