# Syntax

## 테이블 값 수정하기

```
UPDATE tbl_person set name='yse', age='30' where person_id = 1;
```

=> 데이터베이스에 값을 수정하기 위한 쿼리는 `UPDATE` 이며 `UPDATE 테이블명 set 컬럼1이름=컬럼1값, 컬럼2이름=컬럼2값, 컬럼3이름=컬럼3값 where 조건` 이다.

=> 업데이트하고자 하는 컬럼은 미리 만들어져 있어야 한다.

=> 위 예제는 tbl_person 테이블(tbl_person) 의 데이터 중 person_id 가 1인 사람들(where person_id=1) 의 데이터를 설정(set) 하는데 이름은 yse (name='yse'), 나이는 30세(age=30) 로 수정(update) 하라는 뜻이다.


### Reference : https://wikidocs.net/116928