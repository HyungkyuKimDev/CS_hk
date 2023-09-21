# Syntax

## 테이블 값 입력하기

```
INSERT INTO tbl_person (name, age) values ('yse', 50);
```

=> 데이터베이스에 값을 입력하기 위한 쿼리는 `INSERT` 이며 `INSERT INTO 테이블 이름 (컬럼1이름,컬럼2이름) values( 컬럼1값, 컬럼2값);` 형태로 사용한다.

=> 컬럼과 값은 각각 , 로 구분하며 컬럼의 갯수와 값의 갯수는 일치해야 한다.

=> 컬럼은 미리 테이블에 만들어져 있어야 한다.

=> 위 예제는 tbl_person 테이블에 (into tbl_person) 이름과 나이 (name, age) 를 yse, 50 으로('yse',50) 입력(Insert) 하겠다는 의미가 된다. SQL은 문자열을 감쌀 때 '(홑따옴표) 로 감싼다. "(쌍따옴표) 는 동작하지 않으므로 유의한다.



### Reference : https://wikidocs.net/116930