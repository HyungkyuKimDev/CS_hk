<?php 
/*

PSR-12-extended-coding-style-guide

2. 일반

2.1 기본 코딩 표준
코드는 에 요약 된 모든 규칙을 따라야합니다.

PSR-1의 'StudlyCaps'라는 용어는 PascalCase로 해석해야하며(MUST) 첫 단어가 첫 문자를 포함하여 대문자로 표시해야합니다.

2.2 Files

모든 PHP 파일은 Unix LF (linefeed) 줄만 사용해야합니다 (MUST).
    => LF 는 줄바꿈 방식 중 하나, LF / LF / CR이 있고. 
        CR : Carriage Return (\r) => 현재 커서를 줄 올림 없이 가장 앞으로 옮기는 동작
        LF : Line Feed (\n) => 커서는 그 자리에 그대로 둔 상황에서 종이만 한 줄 올려 줄을 바꾸는 동작

모든 PHP 파일은 단일 LF로 끝나는 비어 있지 않은 라인으로 끝나야합니다 (MUST).

PHP code만 존재하는 파일에서는 닫는 ?>태그를 생략해야합니다 (MUST).

2.3 Lines

라인 길이에 엄격한 제한이 있어서는 안됩니다(MUST NOT).

한줄에 들어가는 글자수에 대한 가벼운 제한은 120자여야 합니다. (MUST).

한줄은 80자를 넘지 않아야합니다 (SHOULD NOT). 그보다 긴 줄은 각각 80자 이하의 여러 줄으로 나눠야합니다 (SHOULD).

HEREDOC/NOWDOC 구문을 제외하고 줄의 끝에 공백이 있으면 안됩니다(MUST NOT).
=> quotes에 따른 문자열 처리 방식의 문제

"" double quotes 사용
$foo = 'world';
echo "hello $foo";
//결과: hello world

'' single quotes 사용
echo 'hello $foo';
//결과: hello $foo

heredoc 사용시 double quotes 방식으로 문자열 처리, <<< 하고 사용하고 싶은 큰 대문자로 식별자(identifier) 만들어 처리. 
끝에 식별자 ; 하면 끝 

$error2=<<<ERROR 
what are youdoing 
ERROR; 

nowdoc 사용시 '' single quotes 방식으로 문자열 처리, <<< 하고 '' 안에 사용하고 싶은 큰 대문자로 식별자(identifier) 만들어 처리 끝에 식별자 ; 하면 끝 

$echo <<<'NOWDOC' 
heredoc과 nowdoc은 큰따옴표와 작은따옴표의 차이를 갖고 있다 
NOWDOC; 

명시적으로 금지 된 경우를 제외하고 가독성을 높이고 관련 코드 블록을 표시하기 위해 빈줄을 추가 할 수 있습니다 (MAY). 

한 줄에 하나 이상의 문장이 있어서는 안됩니다 (MUST NOT). ?>

2.4 들여쓰기

코드는 4개의 스페이스로 들여쓰기를 사용해야만하며(MUST), 탭을 사용하지 않아야만 합니다 (MUST NOT).

2.5 Keyword와 Type

모든 PHP 예약 키워드와 타입 ​은 소문자 여야만합니다 (MUST).

향후 PHP 버전에 추가되는 모든 새로운 유형과 키워드는 반드시 소문자 여야만합니다 (MUST).

반드시 boolean 대신 bool, integer 대신 int 등 짧은 형태의 타입 키워드를 사용해야합니다 (MUST).

3. Declare 선언문, 네임 스페이스 및 Import 선언문

PHP 파일의 머릿글은 여러 블록으로 구성 될 수 있습니다. 이미 존재한다면, 아래의 각 블록은 하나의 빈 행으로 분리해야하며 빈 행을 포함해서는 안됩니다 (MUST NOT). 
관련이 없는 블록은 생략 할 수 있지만(MUST) 각 블록은 아래에 나열된 순서여야 합니다.

1.
<?php로 태그 열기.
2.
파일 수준의 docblock.
3.
하나 이상의 declare 선언문.
4.
파일의 네임 스페이스 선언.
5.
하나 이상의 클래스 기반 use import 문.
6.
하나 이상의 함수 기반 use import 문.
7.
하나 이상의 상수 기반 use import 문.
8.
파일의 나머지 코드.

파일에 HTML과 PHP가 섞여 있다면 위 섹션 중 하나라도 여전히 사용할 수 있습니다. 
그럴땐 파일의 최상단에는 declare 문이 있어야 하며 (MUST), 
나머지 부분은 닫는 PHP 태그와 HTML과 PHP가 섞인 코드가 있어야합니다.
열기 태그 <?php가 파일의 첫 번째 줄에 있을 때, PHP 열기 및 닫기 태그 외부에 마크업을 포함하는 파일이 아니라면 다른 문장이 없는 자체 라인 상에 있어야 합니다(MUST).

Import 문은 항상 정규화된 형식이어야 하므로 백 슬래시로 시작해서는 안됩니다 (MUST).
다음은 모든 블록의 전체 목록의 예제를 보여줍니다.
*/

/**
 * This file contains an example of coding styles.
 */

declare(strict_types=1);

namespace Vendor\Package;

use Vendor\Package\{ClassA as A, ClassB, ClassC as C};
use Vendor\Package\SomeNamespace\ClassD as D;
use Vendor\Package\AnotherNamespace\ClassE as E;

use function Vendor\Package\{functionA, functionB, functionC};
use function Another\Vendor\functionD;

use const Vendor\Package\{CONSTANT_A, CONSTANT_B, CONSTANT_C};
use const Another\Vendor\CONSTANT_D;

/**
 * FooBar is an example class.
 */
class FooBar
{
    // ... additional PHP code ...
}

/*

두 단계 이상의 복합 네임 스페이스는 사용해서는 안됩니다 (MUST NOT). 그러므로 허용하는 최대 복합 단계는 다음과 같습니다.

*/

use Vendor\Package\SomeNamespace\{
    SubnamespaceOne\ClassA,
    SubnamespaceOne\ClassB,
    SubnamespaceTwo\ClassY,
    ClassZ,
};


/*

그리고 다음은 허용되지 않습니다(MUST NOT).

*/


use Vendor\Package\SomeNamespace\{
    SubnamespaceOne\AnotherNamespace\ClassA,
    SubnamespaceOne\ClassB,
    ClassZ,
};


# PHP를 열고 닫는 태그 외부에서 마크 업을 포함하는 파일에 엄격한 유형을 선언하고자 할 때, 
# 선언문은 파일의 첫 번째 줄에 있어야하며 (MUST), 여는 PHP 태그와 strict types 선언과 닫는 태그를 포함해야합니다.

/*

<?php declare(strict_types=1) ?>
<html>
<body>
    <?php
        // ... additional PHP code ...
    ?>
</body>
</html>

*/

// Declare 문은 공백을 포함하지 않아야하며(MUST) declare(strict_types=1) 
// (선택 항목 인 세미콜론 종결자 포함)이어야합니다(MUST).

// 블록 선언문은 허용되며 반드시 아래와 같은 형식이여야합니다(MUST). 중괄호와 간격의 위치 참고 :

declare(ticks=1) {
    // some code
}


// 4. 클래스, 프로퍼티, 메소드

// "클래스"라는 용어는 모든 클래스, 인터페이스 및 특성-trait을 나타냅니다.

// 닫는 중괄호는 같은 줄의 주석이나 명령문 다음에 와서는 안됩니다(MUST NOT).

// 새 클래스를 인스턴스화 할 때 생성자에 전달 된 인수가 없는 경우에도 항상 괄호가 있어야합니다(MUST).

new Foo(); # 가능
new Foo; # 불가능

// 4.1 확장과 구현

// extends와 implements 키워드는 클래스 이름과 같은 줄에 선언해야합니다 (MUST).

// 해당 클래스의 여는 중괄호는 바로 다음 줄에 있어야만 합니다(MUST). 클래스의 닫는 중괄호는 본문 뒤의 다음 줄로 가야만 합니다(MUST).

// 여는 중괄호는 반드시(MUST) 바로 다음 줄에 있어야하며 중간에 빈 줄이 있어서는 안됩니다.

// 닫는 중괄호는 반드시(MUST) 바로 다음 줄에 있어야하며 빈 줄이 앞에 있어서는 안됩니다(MUST NOT).

namespace Vendor\Package;

use FooClass;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

class ClassName extends ParentClass implements \ArrayAccess, \Countable
{
    // constants, properties, methods
}

// implements의 목록과 인터페이스의 경우, extends는 여러 줄에 걸쳐 나뉘어 질 수 있으며(MAY), 각 줄은 한 번의 들여쓰기를 합니다. 
// 그렇게 할 때 목록의 첫 번째 항목은 다음 줄에 있어야하며 한 줄에 하나의 인터페이스만 있어야합니다.


namespace Vendor\Package;

use FooClass;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

class ClassName extends ParentClass implements
    \ArrayAccess,
    \Countable,
    \Serializable
{
    // constants, properties, methods
}

// 4.2 특성-trait 사용

// 특성-trait을 구현하기 위해 클래스 내에서 사용되는 use 키워드는 클래스를 여는 중괄호 다음 줄에 선언해야합니다 (MUST).


namespace Vendor\Package;

use Vendor\Package\FirstTrait;

class ClassName
{
    use FirstTrait;
}

// 클래스로 가져온 각각의 특성-trait은 반드시 한 줄에 하나씩 포함해야하며(MUST), 
// 각 포함내역은 반드시 고유한 use import 문을 가져야합니다 (MUST).


namespace Vendor\Package;
​
use Vendor\Package\FirstTrait;
use Vendor\Package\SecondTrait;
use Vendor\Package\ThirdTrait;
​
class ClassName
{
    use FirstTrait;
    use SecondTrait;
    use ThirdTrait;
}

// 클래스에 use import 문 다음에 아무것도 없는 경우, 클래스를 닫는 중괄호는 마지막 use import 문 다음에 있어야합니다 (MUST).


namespace Vendor\Package;
​
use Vendor\Package\FirstTrait;
​
class ClassName
{
    use FirstTrait;
}

