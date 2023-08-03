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

각 파일은 무언가를 선언하거나 (클래스, 함수, 상수 등) 
또는 사이드이펙트의 원인이 되는(예 : 출력 생성, .ini 설정 변경 등) 형태로 작성해야하지만(SHOULD) 둘 모두를 수행하면 안됩니다(SHOULD NOT).

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
=> x = 2 하면 x 변수의 값이 변화된다. 따라서 사이드 이펙트가 발생했다. and y = x++ 하면 y 변수, x 변수 두 개의 변수의 값이 변화하므로 사이드 이펙트가 두 번 발생했다고 볼 수 있다.

"사이드이펙트"에는 Output 생성, 명시적인 "require"또는 "include"의 사용, 외부 서비스 연결, ini 설정 변경, 오류 또는 예외 발생, 전역 변수 또는 정적 변수 변경, 파일의 읽기 또는 쓰기
등이 있습니다.

다음은 선언과 사이드이펙트가 모두 포함 된 파일의 예입니다.

<?php
// side effect: change ini settings
ini_set('error_reporting', E_ALL);

// side effect: loads a file
include "file.php";

// side effect: generates output
echo "<html>\n";

// declaration
function foo()
{
    // function body
}

다음 예제는 사이드이펙트가 없이 작성된 파일입니다.

<?php
// declaration
function foo()
{
    // function body
}
​
// conditional declaration is *not* a side effect
if (! function_exists('bar')) {
    function bar()
    {
        // function body
    }
}

==> 추가 side effect 사용 시 발생 가능 문제들
1.매크로에서의 실수
	
잘못된 예

#define sqr(x) x*x
sqr(a+b)
=> a+b*a+b

고친 예

long value = a + b;
sqr(value)

2. sizeof에서의 실수

잘못된 에
	
int a = 14;
int b = sizeof(a++);
=> sizeof에 side effect가 있을 시, 오류 발생

3. && 혹은 || 에서 사용

잘못된 예

if ( logical_expression && ++x) // 문제
{
// some expression
}
function(x);
=> 조건에 따라 실행 여부가 결정되는 데다가, 연산 순서에 따라 조건 결과가 달라지기 때문에 사용하면 안 된다.




3. Namespace 와 Class

네임 스페이스와 Class는 반드시(MUST) [자동 로딩 (autoloading)] PSR [, ]을 따라야합니다.

이것은 클래스가 각각의 개별 파일에 작성되어있으며, 공급자(vendor)의 이름으로 시작하는 네임스페이스를 사용했다는 것을 의미합니다.

클래스 이름은 반드시(MUST) StudlyCaps 규칙으로 작성되어야 합니다.

PHP 5.3 및 이후 버전 용으로 작성된 코드는 정식 네임 스페이스를 사용해야합니다.

예제:

<?php
// PHP 5.3 and later:
namespace Vendor\Model;

class Foo
{
}

4. Class의 상수(Constants), Properties, Methods

"Class"라는 용어는 모든 Class, Interface 및 Trait을 의미합니다.

4.1. 상수(Constants)
클래스 상수는 모두 대문자 또는 밑줄_로 선언해야합니다 (MUST).

예제:
<?php
namespace Vendor\Model;

class Foo
{
    const VERSION = '1.0';
    const DATE_APPROVED = '2012-06-01';
}

4.2. Properties
이 가이드는 의도적으로 $StudlyCaps , $camelCase 또는 $under_score 같은 형태로 property 이름을 권장하는 것을 피하고 있습니다.

Properties는 어떤 규칙이 사용 되든 상관없지만 합리적인 범위 내에서 일관되게 적용되어야 합니다(SHOULD). 
이 범위는 공급자 수준(vendor-level), 패키지 수준(package-level), Class 수준(class-level) 또는 Method(method-level) 수준 일 수 있습니다.

4.3. Methods
Method의 이름은 반드시(MUST) camelCase로 작성해야 합니다.

*/

?>