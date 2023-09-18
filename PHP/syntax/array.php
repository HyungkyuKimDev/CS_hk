<?php

/*
array 配列


$answers = ['A', 'B' ,'C', 'D'];

echo $answers[0]; // Aを出力
echo $answers[3]; // Cを出力


배열의 선언과 값 추가 예

$arr = []; // 空の配列を定義
$arr[] = '値1';
$arr[] = '値2';
$arr[] = '値3';
$arr[] = '値4';

array_push($a, 5); // 값 추가 
unset($a[0]); // 값 제거

echo $arr[0]; // 「値1」を出力
echo $arr[3]; // 「値4」を出力

*/

/*
Associative Array 連想配列 연관 배열
=> 배열의 인덱스를 숫자가 아닌 문자로도 사용되는 배열

$b = array('a' => 10);

연관 배열 값 추가
$b['b'] = 20;

연관 배열 값 제거
unset($b['a']);

$key => $value 구조

$human = [
    'name' => [
        'first_name' => 'taro',
        'last_name' => 'yamada',
    ],
    'age' => 30,
    '座右の銘' => '虚仮の一念岩をも通す', // 
];

echo $human['name']['first_name']; // 「taro」を出力
echo $human['age'];                // 「30」を出力
echo $human['座右の銘'];            // 「虚仮の一念岩をも通す」を出力
```

*/



/*

php 배열 내장 함수

count: 갯수 출력

$fruitsList = ['apple', 'orange', 'grape'];

echo '果物の数: '.count($fruitsList);


foreach: 모든 배열 참조(반복해서 참조하는 개념)

1) 

$fruitsList = ['apple', 'orange', 'grape'];

foreach ($fruitsList as $fruits) {
    echo '果物: '.$fruits."\n";
}

foreach ($fruitsList as $index => $fruits) {
    echo '番号: '.$index."\n";
    echo '果物: '.$fruits."\n\n";
}

2) 

endforeach 를 쓰는 경우

foreach ($fruitsList as $fruits):
    echo '果物: '.$fruits."\n";
endforeach;

<?php
$a = array(1,2,3,4,5);
foreach($a as $item){
    echo $item;
    echo "<br />";
}

echo "<br />";
$b = array('a'=>10, 'b'=>20, 'c'=> 'hi php');
foreach($b as $key=>$value){
    echo "$key => $value";
    echo "<br />";
}

특이사항

반복문은 보통 배열항목 in 배열 인 반면
php에서는 배열 as 배열항목 이다.

*/