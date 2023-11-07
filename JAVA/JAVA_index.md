# Java

<br>

## Features
Java는 제임스 고슬링과 연구원들이 개발한 객체 지향적 프로그래밍 언어이다.

Write Once, Run Anywhere
직역을 하면, '한 번 작성하면 어디에서나 실행된다'는 의미로, 자바로 개발된 프로그램은 자바 실행 환경 JRE가 설치된 모든 환경에서 실행이 가능하다는 것을 의미한다.

### javac
Java Compiler

### JVM (Java Virtual Machine)
Java Application을 Class Loader를 통해 읽어 Java API와 함께 실행한다.   
Java 와 OS 사이에서 OS에 관계없이 독립적으로 작동하도록 한다.

### JRE (Java Runtime Environment)
JVM + Libraries + Other Components  
JVM과 JAVA 실행시 필요한 라이브러리 및 기타 Components를 묶어 배포하는 패키지   
Java 실행을 위해 필요

### JDK (Java Development Kit)
JDK = JRE + Compilers + Debuggers  
Java 프로그램을 compile 하고 Run 하는데 필요

### Package

클래스들을 패키지 단위로 묶어서, 정리한다.
> com.[pakage].[class Name]

클래스 사용
> package com.[package];



## Syntax

### 1. 자료형   
- Java의 자료형은 크게 Primitive type(기본자료형)과 Reference type(참조자료형)으로 구분된다.

- primitive type의 종류:  
    - short, int, long, float, double, char, boolean, byte 등이 있다.   
    - short, int, long은 숫자형으로 각각 나타낼 수 있는 숫자의 크기가 다르며, 이는 각 타입에 할당되는 메모리의 크기가 다르기 때문이다.   
    - 순서대로 각 2바이트, 4바이트, 8바이트가 할당 가능하다.   
    - 또한 아래의 코드로 최소 및 최대값을 찍어보며 실제 값을 볼 수 있다.

        > System.out.println(Short.MAX_VALUE);  
        System.out.println(Short.MIN_VALUE);

- reference type의 종류:   
    - 참조 자료형은 위의 기본 자료형을 제외한 모든 자료형을 말한다.    
    - 쉽게 말해 자바의 인스턴스를 가리킬 수 있는 자료형이다.   
    - 클래스, 배열, 열거, 인터페이스 등이 존재한다.  
    - 가장 친근한 String 또한 참조 자료형에 속한다.(클래스)


### 2. 배열 (Array)
- 배열 변수명 선언 (아래의 코드에선 arr이 배열의 변수 명)  
    > int arr[];
- 배열 생성 (크기 지정도 이 때 해준다.)
    > arr = new int[5]
- 초기화 (생성된 배열에 값을 넣어준다.)

- 배열은 선언과 동시에 크기를 지정받는다, 따라서 고정된 크기를 갖는다.   
하지만 실제로 고정된 크기의 배열만을 쓰기는 쉽지 않기 때문에,   
보통 배열보다는 ArrayList라는 Collection을 사용한다.


### 3. 조건문
- 사전지식: char는 문자열 하나만을 담으며 작은 따옴표로 표현된다.

- if else문 
```java
public class ElseIfEx {
	public static void main(String[] args) {
		int age = 22;
		if(age>=20 && age<30){	// 조건식 1
			// 조건식 1이 true일 때 실행
			System.out.println("20대");
		}else if(age<20){	// 조건식 2
			// 조건식 1이 false이면서 조건식 2가 true일 때 실행
			System.out.println("10대 이하");
		}else{
			// 조건식 1과 2가 false일 때 실행
			System.out.println("30대 이상");
		}
	}
}
```

- switch문
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String score = sc.next();

        switch(score){
            case "A":
                System.out.println("A등급입니다.");
                break;
            case "B":
                System.out.println("B등급입니다.");
                break;
            case "C":
                System.out.println("C등급입니다.");
                break;
            default:
                System.out.println("D등급 이하 입니다.");
                break;
        }
    }
}
```

- 삼항 연산자  
    - 변수명 = (논리 조건) ? true일 때 실행되는 기능 : false일 때 실행되는 기능   

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();
		
        // result의 값은 조건에 따라 좌항 혹은 우항으로 결정된다.
        String result = ( score < 10 ) ? "10보다 작습니다." : "10보다 큽니다.";
        System.out.println(result);
    }
}
```

### 4. 반복문
- for 반복문은 자바스크립트와 형태가 비슷하여 익숙했다.

```java
for( int i = 0 ; i < 100; i++){
	//이와 같은 형태로 사용한다.
}
```

- for each 반복문   
    - 파이썬에서 주로 쓰이는 반복문의 형식이었다.  
    - 배열, 리스트 등에서 하나 하나의 원소들을 iterate하며 사용하는 방식이다.

```java
public class Main {
    public static void main(String[] args) {
        // write your code here
        String[] days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};

        for (String day : days){
            System.out.println(day);
        }
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        // write your code here
        int i = 0;
        int sum = 0;
        
        while (i<10){
        	sum += (i+1);
            i++;
        }
        System.out.println(sum);
    }
}
```

- do - while문

```java
public class Main {
    public static void main(String[] args) {
        // write your code here
        int i = 0;
        int sum = 0;
        
        do{
        	sum += (i+1);
            i ++;
        }while (i<10);
        System.out.println(sum);
    }
}
```

### 5. 클래스, 인스턴스, 메소드

- 클래스  
표현하고자 하는 대상의 공통 속성을 한 군데에 정의해 놓은 것  
즉, 객체의 속성을 정의한 것이다.    
객체의 속성에는 필드, 메소드, 생성자 등이 있다.  
필드는 클래스 내부 전역에서 사용 가능한 전역 변수를 지칭한다.   
필드(전역변수)는 멤버 변수라고도 한다.   
반면 메소드와 생성자에서 정의된 변수는 지역변수라고 한다.

- 인스턴스  
어떠한 클래스로부터 만들어진 객체를 그 클래스의 인스턴스라고 한다.  
아래의 코드에서 Phone은 클래스이고, 메인 함수의 galaxy와 iphone은 인스턴스들이다.  

```java
class Phone {
    String model;
    String color;
    int price;
}

public class Main {
    public static void main(String[] args) {
        Phone galaxy = new Phone(); 
        galaxy.model = "Galaxy10";
        galaxy.color = "Black";
        galaxy.price = 100;
        
        Phone iphone =new Phone();
        iphone.model = "iPhoneX";
        iphone.color = "Black";
        iphone.price = 200;
        

        System.out.println("철수는 이번에 " + galaxy.model + galaxy.color + " + 색상을 " + galaxy.price + "만원에 샀다.");
        System.out.println("영희는 이번에 " + iphone.model + iphone.color + " + 색상을 " + iphone.price + "만원에 샀다.");
    }
}
```

- 클래스와 인스턴스 비유   
    따라서 클래스는 붕어빵을 만들어내는 틀이라고 할 수 있으며,    
    인스턴스는 붕어빵 틀에 의해 만들어진 붕어빵이라고 할 수 있다.

- 메소드   
메소드는 어떠한 작업을 수행하는 코드를 하나로 묶어 놓은 것이다.
함수라고도 한다.  
메소드 내의 변수는 지역변수로, 메소드 내부에서만 사용할 수 있다.  
코드 컨벤션으로는, 시작은 동사로하되 캐멀케이스를 사용한다.

> //반환타입 메소드이름 (타입 변수명,타입 변수명, ...){   
//    수행되어야 할 코드  
//}

```java
int add(int x, int y) {
    int result = x + y;
    return result;
}
```

### 6. 생성자
- 생성자  
인스턴스가 생성될 때 사용되는 인스턴스 초기화 메소드   
즉 new 와 같은 키워드로 해당 클래스의 인스턴스가 새로 생성될 때, 자동으로 호출되는 메소드   
대표적으로 인스턴스의 변수를 초기화하는 용도의 생성자가 있다.   
생성자의 이름은 클래스 명과 같아야하며, 리턴값이 없다는 특징을 지닌다.  
클래스를 선언할 때 따로 선언하지 않아도 매개변수와 내용이 없는 디폴트 생성자가 생성된다.  
+)팁 alt + insert를 누르면 자동으로 생성자, getter, setter, toString등의 코드를 작성할 수 있다.  

<br>

> //클래스이름 (타입 변수명, 타입 변수명, ...){  
//    인스턴스 생성 될 때에 수행하여할 코드  
//    변수의 초기화 코드  
//}  

```java
class Phone {
    String model;
    String color;
    int price;
	
    //생성자
    Phone(String model, String color, int price) {
        this.model = model;
        this.color = color;
        this.price = price;
    }
}
```
 
> class 에 선언된 변수는 instance 가 생성될 때 값이 초기화(initialize)된다.  
따라서 변수의 선언부나 생성자를 통해서 초기화를 해주지 않는다면, 각 자료형의 디폴트 값이 할당된다.  
아래 코드로 각 자료형의 디폴트 값을 확인할 수 있다.  
단 필드의 마지막에 정의된 참조 자료형은 디폴트 값이 아닌 참조할 값이 없다는 뜻인 null이 된다.  

```java
class DefaultValueTest {
    byte byteDefaultValue;
    int intDefaultValue;
    short shortDefaultValue;
    long longDefaultValue;
    float floatDefaultValue;
    double doubleDefaultValue;
    boolean booleanDefaultValue;
    String referenceDefaultValue;
}

public class Main {
    public static void main(String[] args) {
        DefaultValueTest defaultValueTest = new DefaultValueTest();
        System.out.println("byte default: " + defaultValueTest.byteDefaultValue);
        System.out.println("short default: " + defaultValueTest.shortDefaultValue);
        System.out.println("int default: " + defaultValueTest.intDefaultValue);
        System.out.println("long default: " + defaultValueTest.longDefaultValue);
        System.out.println("float default: " + defaultValueTest.floatDefaultValue);
        System.out.println("double default: " + defaultValueTest.doubleDefaultValue);
        System.out.println("boolean default: " + defaultValueTest.booleanDefaultValue);
        System.out.println("reference default: " + defaultValueTest.referenceDefaultValue);
    }
}
```

### 7. Method

- 메소드 제작 방법 (int num은 파라미터 역할)
```java
public class Main {
    public static void sayHelloWorld(int num){
            for(int i = 0; i < num; i++)
            {
                System.out.println("Hello Guys");
            }
        }
    
    public static void main(String[] args){
        sayHelloWorld(5);
    }
}
```


### Reference
[Jun_BE.log](https://velog.io/@rlafbf222/JAVA-%EA%B8%B0%EC%B4%88-%EB%AC%B8%EB%B2%95-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC)