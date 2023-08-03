<!-- 
Reference
https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md
https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-12-extended-coding-style-guide.md 
-->


<?php

/*

PSR-1-basic-coding-standard

1. Overview
반드시 <?php 와 <?= 태그만을 사용해야 합니다.

반드시 BOM이 없는 UTF-8로만 PHP코드를 작성해야 합니다. 
    => BOM(Byte Order Mark)  HTML 파일을 생성할 때의 문자 인코딩 방식인 UTF-8인데. UTF-8 인코딩 과정에서 BOM이라는 문자가 강제로 삽입된다.
       다른 UTF간의 인코딩 방식을 구분하기 위함이다. 인코딩 방식을 구분하지 않아도 되는 경우에는 사용하지 않아도 된다.

각 파일은 무언가를 선언하거나 (클래스, 함수, 상수 등) 또는 사이드이펙트의 원인이 되는(예 : 출력 생성, .ini 설정 변경 등) 형태로 작성해야하지만(SHOULD) 둘 모두를 수행하면 안됩니다(SHOULD NOT).

네임스페이스와 클래스는 반드시(MUST) "autoloading"에 관한 PSR: [, ]을 따라 작성해야 합니다.

Class 는 반드시(MUST) StudlyCaps에 따라 작성해야합니다.
    => StudlyCaps 라는것은 단어의 첫글자가 대문자인 규칙 ex: DefaultClass

Class의 상수(constants)는 반드시(MUST) 전부 대문자와 밑줄_만으로 작성해야합니다.

Method는 반드시(MUST) camelCase로 작성해야합니다.

2. Files
2.1. PHP Tags
PHP 코드는 반드시(MUST) 긴 <?php ?> 태그나 짧은 <?= ?> 태그를 사용해야합니다 그외의 태그를 사용해서는 안됩니다 (MUST NOT).

2.2. Character Encoding
PHP 코드는 반드시(MUST) BOM이 없는 UTF-8 문자열만 사용해야합니다

2.3. 사이드이펙트 side effect
각 파일은 새로운 무언가 (클래스, 함수, 상수 등)를 선언하고 다른 사이드이펙트를 일으키지 않거나, 사이드이펙트가 있는 로직를 실행하지만(SHOULD) 둘 다 수행하면 안됩니다(SHOULD NOT).
"사이드이펙트"는 클래스, 함수, 상수 등을 선언하는 것과 직접적으로 관련이없는 논리를 파일에 단순히 포함하는 것부터 실행하는 것 전부를 의미합니다.

"사이드이펙트"에는 Output 생성, 명시적인 "require"또는 "include"의 사용, 외부 서비스 연결, ini 설정 변경, 오류 또는 예외 발생, 전역 변수 또는 정적 변수 변경, 파일의 읽기 또는 쓰기
등이 있습니다.
다음은 선언과 사이드이펙트가 모두 포함 된 파일의 예입니다.

*/

?>