# Date time

```PHP
<?php
$date1 = date("Y-m-d H:i:s");
$date2 = new DateTime();
$date2_str = $date2->format("Y-m-d H:i:s");

var_dump($date1); echo "<br />";
var_dump($date2); echo "<br />";
var_dump($date2_str); echo "<br />";

$tomorrow = $date2->add(new DateInterval("P1D"));
var_dump($tomorrow); echo "<br />";

```

결과

```
string(19) "2020-07-23 07:28:18" 
object(DateTime)#1 (3) { ["date"]=> string(26) "2020-07-23 07:28:18.498365" ["timezone_type"]=> int(3) ["timezone"]=> string(13) "Europe/Berlin" } 
string(19) "2020-07-23 07:28:18" 
object(DateTime)#1 (3) { ["date"]=> string(26) "2020-07-24 07:28:18.498365" ["timezone_type"]=> int(3) ["timezone"]=> string(13) "Europe/Berlin" } 

```

---
고전적인 php 는 날짜를 문자열로 처리한다. $date1 이 예시이다.

```
$date1 = date("Y-m-d H:i:s");
```

---
PHP 5.2.0 버전 이상부터는 날짜 타입 DateTime 이 있다. 단순 문자열이 아니라 날짜를 더하거나 빼거나 비교하는 것이 가능하다.

```
$date2 = new DateTime();
```

---
`DateTime` 타입을 포멧 문자열로 바꾸고 싶으면 `->format(날짜포메터)` 메소드를 사용한다.

```
$date2->format("Y-m-d H:i:s")
```

---
날짜를 더하고 싶으면 `add` 메소드를 사용한다. `add` 함수의 메소드는 `DateInterval` 객체 타입을 파라미터로 받는다. `DateInterval` 객체의 파라미터 "P1D" 는 Period one(1) Day 의 약자로 하루 간격 이란 뜻이다.

```
$date2 = new DateTime();
$date2->add(new DateInterval("P1D"));
```

---
`DateTime` 타입 객체를 사용하지 않고 문자열을 이용해 하루를 추가하려면 아래와 같이 한다.

```
date("Y-m-d", strtotime($date1.'+ 1 days'))
```

---
만약 `require_once` 혹은 `include_once` 를 사용할 때 만약 함수 내부 등 제한된 스코프에서 사용되면 불러온 변수 등은 현재 스코프가 끝나는 순간 없어진다. 만약 함수가 한번 더 호출되어도 `_once` 여서 다시 한번 `include` 나 `require` 가 동작하지 않기 때문에 변수가 현재 스코프에서 불러지지 않아 오류가 나는 경우가 있으므로 유의해야 한다.


## Reference : https://wikidocs.net/116895