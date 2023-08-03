<?php


/*
if 条件分岐

if

if ([条件 true / false]) {
// trueのとき実行
}

if / else

if ([条件 true / false]) {
// trueのとき実行
} else {
// falseのとき実行
}

if / else if / else

if ([条件1 true / false]) {
// 条件1がtrueのとき実行
} else if ([条件2 true / false]) {
// 条件2がtrueのとき実行
} else {
// 条件1,条件2がfalseのとき実行
}

수 , 문자열, 배열 사용 if 예

// ifではfalseと同じ扱いになる
$zeroInt = 0;
$emptyString = '';
$emptyArray = [];

if (!$zeroInt) {
echo '$zeroIntの値は空です';
}
if (!$emptyString) {
echo '$emptyStringの値は空です';
}
if (!$emptyArray) {
echo '$emptyArrayの値は空です';
}

if 사용 함수들 関数

isset

변수가 정의되어있는지 확인

if (isset($hoge)) {
echo '$hogeは定義されています';
} else {
echo '$hogeは定義されていません';
}

$arr = [
'key1' => 'value1',
];
if (!isset($arr['hoge'])) {
echo '$arrの中にhogeのキーはありません';
}

// null인 경우, false를 반환한다.

$noValue = null;
if (!isset($noValue)) {
echo '$noValueの中に値が指定されていません';
}



empty

값이 비워져있는지 확인

// 変数自体が未定義の場合
if (empty($hoge)) {
echo '$hogeは値が入っていません';
}

// 変数が定義されていても値が空の場合
$fuga = '';
if (empty($fuga)) {
echo '$fugaは値が入っていません';
}



in_array

특정 값이 배열에 포함 되어있는지 확인

$answers = ['A', 'B', 'C', 'D'];
if (in_array('A', $answers)) {
echo '配列$answersの中にAが見つかりました!';
}

*/