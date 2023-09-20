# Syntax

## 테이블 값 가져오기

```
SELECT * FROM  tbl_person  where person_id = 1;
```

=> Query는 데이터베이스에서 질의를 구하는 구문을 말하고. 데이터베이스 에서 SQL(Structured Query Language) 라는 문법을 통해 데이터 관리하는 방법을 제공   
=> 데이터베이스에서 값을 가져오는 쿼리는 `SELECT`이며 `SELECT [column] from [table] where [column = value]`이다. column을 모두 가져오려면 `*` 사용.  
=> 위 예제는 tbl_person 테이블에서 person_id 가 1인 행들의 모든 컬럼들을 조회하라는 뜻

### Reference : https://wikidocs.net/116929
