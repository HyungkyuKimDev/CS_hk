# 모던 PHP

---

## 네임스페이스

네임스페이스는 이름 공간을 분리해서 같은 함수 이름이나 변수 이름, 클래스를 분리할 수 있다.
이러한 특성은 여러 벤더들이 여러 기능을 만들 때 이름 충돌을 걱정하지 않게 만든다. PHP의 함수는 한번 실행되면 전역으로 설정되기 때문에 예전에는 고유의 접두어를 붙여서 어색한 함수 이름이 되던 것을 방지할 수 있게 되었다.


```
<?php
namespace yse;

class Sample
{
    // member variable
    private $name;
    private $age;

    // constructor
    public function __construct()
    {
        $this->name = "yse";
        $this->age = "10";
    }

    // method
    public function tell()
    {
        echo "my name is {$this->name} .";
        echo " and my age is {$this->age} .";
    }

    // method. return $this
    public function add_age($age)
    {
        $this->age += $age;
        return $this;
    }

    // static method
    public static function factory()
    {
        return new Sample();
    }
}
```

네임스페이스는 각각의 기능에 이름공간을 붙여서 구분할 수 있게 해 주는 기능이다.
namespace 키워드로 선언한다.

```
namespace yse;
```

사용할 때는 use 네임스페이스\클래스; 형식으로 사용한다고 알린 후 사용하면 된다.

```
use yse\Sample;
```

use 문을 사용하고 싶지 않을 때는 곧바로 new 네임스페이스\클래스() 형식으로 사용하는 것도 가능하다.

```
$sample = new yse\Sample();
```

네임스페이스를 나누는 기호는 역슬래시 \ 이다.

```
new yse\Sample();
```


### Refernce : https://wikidocs.net/116969