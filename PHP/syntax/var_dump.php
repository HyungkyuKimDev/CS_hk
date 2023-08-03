<?php

/*
var_dump 이용해서 변수의 정보를 확인한다.
=> html으로 값을 입력한 다음, 값이 잘 입력되었는 지 확인하기 위해서 사용됨. 

실행 예

$isBool = false;
var_dump($isBool);

$str = 'ほげほげ';
var_dump($str);

$number = 123;
var_dump($number);

$shiritori = [
    'apple',
    'english',
    'hour',
    'ruby',
    // 英語だとずっとしりとりできますね
];
var_dump($shiritori);

실행 결과

php > $isBool = false;
php > var_dump($isBool);var_dump($isBool);
bool(false)

php > $str = 'ほげほげ';
php > var_dump($str);
string(12) "ほげほげ"

php > $number = 123;
php > var_dump($number);
int(123)

php > $shiritori = ['apple', 'english', 'hour', 'ruby'];
php > var_dump($shiritori);var_dump($shiritori);
array(4) {
  [0]=>
  string(5) "apple"
  [1]=>
  string(7) "english"
  [2]=>
  string(4) "hour"
  [3]=>
  string(4) "ruby"
}

*/