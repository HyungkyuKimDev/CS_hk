<?php

/*

CSV

「Comma Separated Value」 약자로. ','를 이용해 데이터를 행과 열로 표현한 파일

PHP로 CSV 파일 열기

fopen 커맨드 이용. 파일이나 URL를 열기 위한 커맨드

$variable_name = fopen("URL or File name", "mode");

mode = {
    'r' = 읽기
    'w' = 쓰기, 있으면 덮어쓰기
    'a' = 추가로 쓰기, 없으면 작성
}

파일로부터 데이터 가져오기

fgetcsv($handle);

EX)

no,date,status,todo                                      <--- $row1
1,2021-05-02,done,HTML5を勉強する                          <--- $row2
2,2021-05-12,done,セレクタについて理解する                   <--- $row3
3,2021-05-22,yet,ブロック要素とインライン要素について理解する    <--- $row4
4,2021-06-01,yet,domの操作について理解する                   <--- $row5

$row1 = fgetcsv($handle);
$row2 = fgetcsv($handle);
$row3 = fgetcsv($handle);
$row4 = fgetcsv($handle);
$row5 = fgetcsv($handle);

=> 실제로는 일일이 작성하지 않고, while을 이용

==> 결과

array(4) {
  [0]=>
  string(1) "2"
  [1]=>
  string(10) "2021-05-12"
  [2]=>
  string(4) "done"
  [3]=>
  string(36) "セレクタについて理解する"
}

fopen 커맨드 뒤에 fclose 붙인다.

fclose($handle);

PHP로 CSV 파일 쓰기

파일 열고
$handle = fopen('todo_list.csv', 'a');

데이터 작성 후
fputcsv($handle, $row);

전체 흐름

EX)
$handle = fopen('todo_list.csv', 'a');

$row = [
  "5",
  "2021-05-20",
  "yet",
  "PHPを理解する",
];
fputcsv($handle, $row);

fclose($handle);

*/