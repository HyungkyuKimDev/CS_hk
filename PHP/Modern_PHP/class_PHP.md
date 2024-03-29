# 모던 PHP

---

## Class

객체지향 프로그래밍의 클래스와 인스턴스, 정적 메소드가 있다.


```
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

    public static function factory2()
    {
        return self::factory();
    }    
}

$sample = new Sample();
$sample->tell();

echo "<br />";
Sample::factory()->add_age(3)->tell();
```

---

클래스 선언은 class 키워드로 한다. 이후 바로 클래스 이름이 나온다. 클래스 이름은 PSR(PHP 표준 권고 - PHP Standard Recommendation)-01 에 따라 대문자로 시작하고 단어간의 연결마다 대문자를 사용하는 StudlyCaps 형식을 따른다. Pascal Case 라고 부르기도 한다.

```
class Sample
```

---

클래스는 특정 역할을 하는 타입을 말한다. 내부적으로 멤버변수와 메소드를 가질 수 있다. 클래스 타입의 변수를 인스턴스라고 부른다.

```
$sample = new Sample();
```

위 예시에서 $sample 은 인스턴스, Sample은 타입을 정의하는 클래스다.

---

멤버 변수는 클래스의 인스턴스가 가지는 속성이다. 클래스 안에서 선언된 변수를 멤버 변수라고 부른다. 프로퍼티라고 부르기도 한다.

```
// member variable
private $name;
private $age;
```

클래스 안에 정의된 함수를 메소드라고 부른다.

```
public function tell()
```

add_age 예제에서 보듯 메소드는 함수와 동일하게 리턴값을 가질 수 있다.

```
public function add_age($age)
{
    $this->age += $age;
    return $this;
}
```

---

생성자는 인스턴스가 처음 생성될 때 자동으로 실행되는 초기화 메소드이다. __construct 라는 이름의 메소드가 무조건 생성자가 된다.

```
// constructor
public function __construct()
{
    $this->name = "yse";
    $this->age = "10";
}
```


---

$this 는 인스턴스 자신을 나타내는 키워드다. 인스턴스에 속한 메소드나 멤버 변수를 호출할 때 $this 로 참조한다.

```
// member variable
private $name;
... 생략

// constructor
public function __construct()
{
    $this->name = "yse";
    ... 생략

```

위 예시에서 멤버 변수 $name을 참조하기 위해 $this를 사용했다.
멤버 변수에서 주의해야 할 점이 하나 더 있다. PHP의 변수는 $ 기호를 붙이지만, 멤버 변수에 접근할 때는 $ 기호를 붙이지 않는다.

```
$this->name = "yse";
```

하지만 멤버 변수를 정의할 때는 $ 기호를 붙여야 한다.

```
private $name;
```

---

인스턴스의 멤버 변수나 메소드를 참조할 때는 -> 키워드를 쓴다. 배열에서 키, 값을 가지고 올 때 사용하는 => 와 비슷하므로 헷깔리면 안된다. 다른 언어에서 . 으로 가지고 오는 것과 헷깔려서도 안된다.
아래 코드는 클래스 내부에서 멤버 변수를 참조하는 예시다.

```
$this->name = "yse";
```

아래 코드는 클래스 외부에서 메소드를 참조하는 예시다.

```
$sample->tell();
```

---

return $this 는 인스턴스 자신을 리턴한다는 뜻이다. 주로 하나의 객체에 여러가지 메소드를 연쇄적으로 호출하는 메소드 체이닝을 사용할 때 사용한다.

```
public function add_age($age)
{
    $this->age += $age;
    return $this;
}
```

아래처럼 사용한다.

```
add_age(3)->tell()
```

---

"" 문자열이나 히어닥 문법은 내부에서 변수를 치환할 수 있다. 이 때 만약 복합형 변수일 경우 ${변수} 형식을 이용해서 복합형 변수의 값을 가져올 수 있다. 이 규칙은 클래스와 무관하게 PHP 전체에서 동일하다.

```
public function tell()
{
    echo "my name is {$this->name} .";
    echo " and my age is {$this->age} .";
}
```

---

멤버 변수나 메소드 이름 앞에 static 을 붙이면 정적인 속성을 갖는다. 정적인 변수나 메소드는 인스턴스에 속하지 않고 클래스에 속한다.

```
// static method
public static function factory()
{
    return new Sample();
}
```

---

정적인 메소드나 프로퍼티를 호출할 때는 -> 를 사용하지 않고 :: 를 사용한다.

```
Sample::factory()
```


---

static 이라는 키워드가 메소드가 아닌 일반 함수 안에서 사용되면 함수 자체가 실행이 끝났음에도 상태를 가지고 있는 코루틴으로 작동한다. 같은 키워드지만 사용되는 곳에 따라 의미가 다르다.

```
function func_static(){
    static $cnt = 1;    
    echo $cnt;
    $cnt ++;
}

func_static();
func_static();
```

---

예제에서 정적 메소드 factory 는 팩토리 디자인 패턴으로 인스턴스를 생성한다.

```
// static method
public static function factory()
{
    return new Sample();
}
```

php 는 new Sample()->add_age() 처럼 생성자 호출 후 곧바로 다른 인스턴스의 메소드를 호출하는 생성자 메서드 체이닝이 불가능하다. 꼭 하고 싶다면 (new Sample())->add_age() 형식으로 생성자를 () 로 감싸줘야 한다. 이러한 불편함 때문에 정적 팩토리 메소드를 만드는 경우가 많다.

추가적으로 팩토리 패턴은 생성자를 여러번 호출해도 인스턴스를 하나만 만드는 싱글톤 패턴과 결합되어 사용되는 경우도 있다. 아래는 팩토리 + 싱글톤 패턴의 예시다.

```
private static $sample = null;
public static function factory()
{
    if (self::$sample == null){
        self::$sample = new Sample();
    }

    return self::$sample;
}
```

정적 메소드 factory()를 통해 인스턴스를 생성할 경우, 이미 생성된 Sample 객체가 있으면 생성된 객체를 반환한다. 객체가 없다면 객체를 생성 후 반환한다.



### Refernce : https://wikidocs.net/116967