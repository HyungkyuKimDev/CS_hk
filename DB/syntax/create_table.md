# Syntax

## 테이블 생성

테이블 생성
```
CREATE  TABLE  `tbl_person` ( 
    `person_id`  INT  NOT  NULL AUTO_INCREMENT , 
    `name`  VARCHAR(256) NOT  NULL , 
    `age`  INT NOT  NULL ,     
    PRIMARY  KEY (`person_id`)
) ENGINE = InnoDB;
```

=> 테이블 이름은 `tbl_person` 열 `person_id` `name` `age` 행 `1` `yse` `80`이다.  
=> 테이블 생성 문법은 `CREATE TABLE 테이블 이름 (열 1이름, 열 2이름 ... , 인덱스) ENGINE=MYSQL 엔진이름;`

---

```
`person_id`  INT  NOT  NULL AUTO_INCREMENT , 
```

=> `INT` 정수 타입이고 `AUTO_INCREMENT` 자동 증가라는 뜻이다. 데이터베이스 시스템에 데이터가 입력될 때 자동으로 숫자가 증가한다.

---

```
`name`  VARCHAR(256) NOT  NULL , 
```

=> `VARCHAR` 문자열 타입. 데이터 베이스 시스템에서는 효율성을 위해 문자열 길이를 미리 정해야 한다. `name`에는 256자가 최대로 들어간다.   
=> `NOT NULL`은 비워져있으면 안 된다는 뜻이다.

---

PK(Primary Key)는 각 열 구분하는 유일한 식별자로 위 예제에서는 `person_id`가 PK다. 엑셀에서 자동으로 생기는 행 번호를 의미한다.

---

인덱스는 데이터베이스 성능을 위해서 미리 참조를 만들어놓는 것을 말하고. PK는 주 키 인덱스 (primary key index)로 인덱스의 종류 중 하나다.

----

```
ENGINE = InnoDB;
```

=> `InnoDB`는 MySQL 데이터베이스 엔진이다. MySQL은 오래된 텍스트 기반 엔진 `MyISAM` 과 현대 바이너리 기반 엔진 `InnoDB` 가 있다.

---

데이터베이스는 행렬을 가정해서 만들었기 떄문에. `insert`를 제외한 DML(Data Manipulation Language)들 (Select, Update, Delete)는 조건에 해당하는 모든 행에 영향을 준다.


### Reference : https://wikidocs.net/116924
