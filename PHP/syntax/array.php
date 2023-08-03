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

echo $arr[0]; // 「値1」を出力
echo $arr[3]; // 「値4」を出力

*/

/*
Associative Array 連想配列 연관 배열
=> 배열의 인덱스를 숫자가 아닌 문자로도 사용되는 배열

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

*/