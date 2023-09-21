# SQL With PHP

## PHP로 SQL 값 가져오기

```
function db_select($query, $param=array()){
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $st->execute($param);
        $result =$st->fetchAll(PDO::FETCH_ASSOC);
        $pdo = null;
        return $result;
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}

var_dump(db_select("select * from tbl_person"));
echo "<br />";
var_dump(db_select("select * from tbl_person where person_id = ?", array(1)));
echo "<br />";
var_dump(db_select("select * from tbl_person where person_id = :person_id", array('person_id' => 1)));
```

=> 위 코드는 `db_get_pdo()` 함수를 사용하므로 db.php 파일 아래에 이어붙인다.

=> 브라우저에서 결과를 확인한다.

```
array(1) { [0]=> array(3) { ["person_id"]=> string(1) "1" ["name"]=> string(3) "yse" ["age"]=> string(2) "30" } } 
```

=> 브라우저에서 결과를 확인한 후에는 `var_dump` 와 `echo` 부분은 삭제한다.


```
function db_select($query, $param=array()){
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $st->execute($param);
        $result =$st->fetchAll(PDO::FETCH_ASSOC);
        $pdo = null;
        return $result;
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}

// 여기서부터 삭제
var_dump(db_select("select * from tbl_person"));
echo "<br />";
var_dump(db_select("select * from tbl_person where person_id = ?", array(1)));
echo "<br />";
var_dump(db_select("select * from tbl_person where person_id = :person_id", array('person_id' => 1)));
// 여기까지 삭제
```

---

MySQL에 저장된 값을 가지고 오는 일은 많이 사용되기 때문에 db_select 라는 이름으로 함수화했다.
```
function db_select($query, $param=array()){}
```

---

$pdo 는 MySQL에 접속하는 객체다.

```
$pdo = db_get_pdo();
```

```
$st = $pdo->prepare($query);
```

pdo 객체에서 쿼리를 세팅하면서 `statement 객체 $st` 를 리턴받는다.   
`StatemenT 객체`는 실제로 쿼리를 실행하는 역할이다. 조금 더 구체적으로 말하면 `prepare statement`라고 해서 쿼리 문자열을 직접 만들어내는 대신 `플레이스 홀더(? 혹은 :이름)를 통해 쿼리에 파라미터를 전달하는 객체`다.   
`프리페어 스테이트먼트(prepare statement)`는 플레이스 홀더를 통해 전달된 파라미터들의 SQL Injection을 방지하는 역할을 한다.

---

쿼리를 실행한다.
```
$st->execute($param)
```

---

실행한 데이터 전부를 가져온다.
```
$st->fetchAll(PDO::FETCH_ASSOC);
```

`fetchAll` 은 데이터를 전부 가지고 오는 메소드다. `PDO::FETCH_ASSOC` 는 데이터를 연관배열로 가지고 오라는 뜻이다. 

만일 쿼리가 실패할 경우 fetchAll 메소드는 false 를 반환한다. 쿼리가 정상 실행되지 않았는지 확인하려면 우선 쿼리 실행 결과가 !== false 인지 확인하고 나서 다음 프로세스를 진행하면 된다.

---

객체를 null 로 초기화해야 데이터베이스 커넥션이 끊긴다.
```
$pdo = null;
```

---

쿼리가 실패하거나 다른 문제가 생기더라도 데이터베이스와의 연결을 끊는다.
```
finally {
    $pdo = null;
}
```

연결을 제 때 끊어주지 않으면 데이터베이스 커넥션이 무한대로 늘어나서 성능에 영향을 미치거나 `too many connections` 오류를 맞이할 수도 있으므로 반드시 쿼리를 실행하고 나면 연결을 끊어야 한다.
`finally`는 오류가 발생해도 실행되는 구문이므로 쿼리의 성공/실패 여부와 관계없이 연결이 끊김을 보장할 수 있다.

---

db_select 함수 사용법은 아래와 같다.

파라미터가 없는 경우 db_select(쿼리 문자열); 형태로 사용한다.

```
db_select("select * from tbl_person");
```

쿼리에 전달할 파라미터가 있는 경우 db_select(쿼리 문자열, array(파라미터들)) 형식으로 사용한다.

```
db_select("select * from tbl_person where person_id = ?", array(1))
```

```
db_select("select * from tbl_person where person_id = :person_id", array('person_id' => 1))
```

---

쿼리에 파라미터를 전달하는 방법은 두개가 있다.

첫번째로는 쿼리 문자열 안에 ? 로 넣는 것이다. 이 때 파라미터 배열은 순차 배열로 전달하며 ? 의 갯수만큼 순서대로 적용된다.

```
db_select("select * from tbl_person where person_id = ?", array(1))
```

?가 배열의 값 1로 대체되었다. 위 구문은 아래와 같은 쿼리를 실행한다.

```
select * from tbl_person where person_id = 1
```

두번째는 쿼리 문자열 안에 :키 로 넣을 수 있다. 파라미터 배열은 연관 배열로 전달하며 각 키에 바인딩된다.

```
db_select("select * from tbl_person where person_id = :person_id", array('person_id' => 1))
```

위 구문은 아래와 같은 쿼리를 실행한다.

```
select * from tbl_person where person_id = 1
```


### Reference : https://wikidocs.net/116943