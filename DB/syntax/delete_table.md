# Syntax

## 테이블 값 삭제하기

```
DELETE FROM tbl_person  where person_id = 1;
```

=> 데이터베이스에 값을 삭제하기 위한 쿼리는 `DELETE` 이며 `DELETE 테이블명 where 조건` 이다. 대부분의 경우 조건은 `테이블의 PK` 이다.

위 예제는 `tbl_person 테이블에서 (FROM tbl_person) person_id 가 1 인 사람들만(where person_id = 1) 삭제(DELETE)` 하라는 뜻이다.


### Reference : https://wikidocs.net/116935