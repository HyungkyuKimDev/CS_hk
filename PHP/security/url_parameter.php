<?php

/*
Null coalescing operator 결합 연산자　合体演算子

??를 사용하는 방식으로

ex)
$id = $_GET['id'] ?? '';

이렇게 되면. $_GET['id']가 null 이면, 빈 글자가 $id로 대입되고. null이 아닌 경우 그 값이 대입된다.

*
이처럼 정의 되지 않은 변수를 참조하는 경우, 아래와 같은 에러가 발생한다.

php > var_dump($_GET['id']); # => 변수의 정보를 출력하는 함수
PHP Notice:  Undefined index: id in php shell code on line 1

Notice: Undefined index: id in php shell code on line 1
NULL

반대로 null 병합 연산자를 사용하면 해결할 수 있다.

php > var_dump($_GET['id'] ?? 'defaultの値');
string(13) "defaultの値"

?? 뒤에 값이 출력하게 된다는 뜻이다.

*
POST 나 GET 값은 유저가 입력하는 값이므로 존재하는 값을 전제로 할 필요가 있다. 그러기 위해서 null 병합 연산자나 if(isset(변수명)) , if(empty(변수명)) 등을 사용해 값을 처리하도록 한다.

isset 사용법 => 변수의 값이 설정되었으면 True 아니면 False

$id = '';
if (isset($_GET['id'])) {
  $id = $_GET['id'];
}

** 추가로 사용자 임의로 URL를 통해서 input에 js 코드를 입력하는 등의 문제를 일으킬 경우 <alert></alert>
=> htmlspecialchars() 를 $_GET[] 로 감싸. < 값이 js 코드가 아닌 단순 html 문자열로 처리하게 한다. 

exit(0)를 쓰면 php 코드가 종료되버린다.