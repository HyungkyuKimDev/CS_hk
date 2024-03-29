# 모던 PHP

---

## 익명 함수 사용

익명 함수는 한번만 사용할 일회성 함수로 이름이 없는 함수라는 뜻이다.   
익명 함수의 경우, 다시 호출되기 위해 메모리를 차지하는 일반 함수와 달리 메모리를 차지하지 않아 메모리를 아낄 수 있다. 


```
<?php
$datas = [1,2,"3","4","오","률",7];

$checker = 2;

$filter_data = array_filter($datas, 
    function($item) use ($checker) {
        return $item == $checker;
    }
);

var_dump($filter_data);
```

---

위 코드에서 익명 함수는 아래 부분이다.

```
    function($item) use ($checker) {
        return $item == $checker;
    }
```

익명함수는 일회성 함수로 이름이 없는 함수다. 주로 콜백(callback) 을 파라미터로 입력받는 함수의 파라미터로 사용된다. 일회성 함수이기 때문에 재활용은 불가능하다.

---

array_filter 함수는 배열에서 특정 조건에 맞는 항목만 뽑아내는 내장 함수다. 인수로 콜백 함수를 받는다.

```
array_filter(배열, 콜백 함수);
```

array_filter 함수의 동작 방식은 다음과 같다.

array_filter 함수는 내부적으로 배열 항목을 순회하면서 하나씩 파라미터로 전달받은 콜백 함수에 파라미터로 전달한다.
콜백 함수는 배열 항목이 조건에 맞는지 검사하고 true 혹은 false를 리턴한다.
array_filter 함수는 콜백 함수에서 true 가 리턴된 것만 따로 모아서 새로운 배열을 만들어낸다.


---


위 예제의 경우, 최종적으로 일치하는 값은 $datas[1]에 해당하는 값 2 하나이므로 $filter_data의 변수에는 array(1) { [1]=> int(2) } 값이 담긴다.

---

익명 함수는 function ($item) 처럼 function 뒤에 함수 이름이 아니라 바로 파라미터가 선언된다.

함수 파라미터 뒤의 use 는 익명 함수에서 클로져(closure) 를 이용하기 위해 use(사용할 외부 변수) 형식으로 선언된다.

```
function($item) use ($checker) {
```

클로져란 함수가 스코프 밖의 범위에 접근하기 위해 사용되는 것이다.
php 의 함수는 외부의 변수와 소통할 방법이 파라미터 혹은 global 키워드를 쓰는 방법밖에 없는 블랙박스 모델이기 때문에 외부 변수를 자연스럽게 참조할 수 있는 방법이 없다. 이 문제를 해결하기 위해 use (외부변수명) 으로 함수가 외부 스코프를 명시적으로 참고할 수 있게 한다.
만약 위 예시에서 use ($checker) 를 사용하지 않으면 함수 내부에서 $checker 변수에 접근하지 못하므로 undefined variable 오류가 난다.

use 키워드는 클로져를 사용할 때 외에 네임스페이스를 사용할 때도 쓰인다. 물론 용도는 전혀 다르다. 네임스페이스를 사용할 때는 이렇게 사용한다.

```
use app\yse\component;
```


### Refernce : https://wikidocs.net/116966