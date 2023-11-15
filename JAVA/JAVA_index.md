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

[1. 자료형](#1-자료형)  
[2. 배열 (Array)](#2-배열-array)
[3. 조건문](#3-조건문)
[4. 반복문](#4-반복문)
[5. 클래스, 인스턴스, 메소드](#5-클래스-인스턴스-메소드)
[6. 생성자](#6-생성자)
[7. Method](#7-method)
[8. Scanner ](#8-scanner)
[9. wrapper class](#9-wrapper-class)
[10. list](#10-list)
[11. OOP](#11-oop)

### 1. 자료형

- Java의 자료형은 크게 Primitive type(기본자료형)과 Reference type(참조자료형)으로 구분된다.

- primitive type의 종류:

  - short, int, long, float, double, char, boolean, byte 등이 있다.
  - short, int, long은 숫자형으로 각각 나타낼 수 있는 숫자의 크기가 다르며, 이는 각 타입에 할당되는 메모리의 크기가 다르기 때문이다.
  - 순서대로 각 2바이트, 4바이트, 8바이트가 할당 가능하다.
  - 또한 아래의 코드로 최소 및 최대값을 찍어보며 실제 값을 볼 수 있다.

    > System.out.println(Short.MAX_VALUE);  
    >  System.out.println(Short.MIN_VALUE);

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

```java
public class MyChar {

    public boolean isVowel(char ch) {

        switch (ch) {

            case 'a', 'e', 'i', 'o', 'u' :
            case 'A', 'E', 'I', 'O', 'U' : return true;

            default: return false;
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
> // 수행되어야 할 코드  
> //}

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
> // 인스턴스 생성 될 때에 수행하여할 코드  
> // 변수의 초기화 코드  
> //}

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
> 따라서 변수의 선언부나 생성자를 통해서 초기화를 해주지 않는다면, 각 자료형의 디폴트 값이 할당된다.  
> 아래 코드로 각 자료형의 디폴트 값을 확인할 수 있다.  
> 단 필드의 마지막에 정의된 참조 자료형은 디폴트 값이 아닌 참조할 값이 없다는 뜻인 null이 된다.

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

```Java
public class Square {

    private int side;

    public Square(int side) {
        // TODO: Initialize side with the passed value
        this.side = side;
    }

    public int calculateArea() {
        // TODO: Calculate and return the area of the square
        if(this.side <= 0){
            return -1;
        }else{
            return this.side * this.side;
        }
    }

    public int calculatePerimeter() {
        // TODO: Calculate and return the perimeter of the square
        if(this.side <= 0){
            return -1;
        }else{
            return this.side * 4;
        }
    }

}
```

<br></br>

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

<br></br>

### 8. Scanner

- 사용 입력 받는 방법

- 사용 전, 클래스 생성
  > import java.util.Scanner; // Scanner 클래스 호출
- 사용 전, 객체 생성
  > Scanner in = new Scanner(System.in); // Scanner 객체 생성
- 입력 메소드 선택

  ```java
  in.nextByte()		// byte 형 입력 및 리턴
  in.nextShort()		// short 형 입력 및 리턴
  in.nextInt()		// int 형 입력 및 리턴
  in.nextLong()		// long 형 입력 및 리턴

  in.nextFloat()		// float 형 입력 및 리턴
  in.nextDouble()		// double 형 입력 및 리턴

  in.nextBoolean()	// boolean 형 입력 및 리턴

  in.next()			// String 형 입력 및 리턴	(공백을 기준으로 한 단어를 읽음)
  in.nextLine()		// String 형 입력 및 리턴 (개행을 기준으로 한 줄을 읽음)
  ```

- EX

  ```java
  import java.util.Scanner;	// Scanner 클래스 호출

  public class Main {
    public static void main(String[] args) {

  	    Scanner in = new Scanner(System.in);	//      Scanner 객체 생성

  	    byte a = in.nextByte(); 		// byte 형 입력 및 리턴
  	    short b = in.nextShort(); 		// short 형 입력 및 리턴
  	    int c = in.nextInt(); 			// int 형 입력 및 리턴
  	    long d = in.nextLong(); 		// long 형 입력 및 리턴

  	    float e = in.nextFloat(); 		// float 형 입력 및 리턴
  	    double f = in.nextDouble(); 	// double 형 입력 및 리턴

  	    boolean g = in.nextBoolean(); 	// boolean 형 입력 및 리턴

  	    String h = in.next(); 			// String 형 입력 및 리턴 (공백을 기준으로 한 단어를 읽음)
  	    String i = in.nextLine(); 		// String 형 입력 및 리턴 (개행을 기준으로 한 줄을 읽음)
    }

  }
  ```

- next() vs nextLine()
  1. next() : 공백 기준으로 하나 처리
     - nextInt() , next()
  2. nextLine() : 한 줄씩 처리

### 8. String Method

- isEmpty

  - 문자열이 비었는지 확인
  - str.isEmpty()

- split

  - 문자열을 배열로 나눠준다.
  - str.split(" "); // 빈칸 단위로 나누는 경우

- length

  - 문자열 길이를 알려준다.
  - str.length();

- Character.isDigit

  - 해당 값이 숫자 인지 아닌지 판명
  - Character.isDigit()

- Characher.getNumericValue
  - 문자형의 숫자를 숫자로 받아온다.
  - Character.getNumericValue()

```java
public class StringMagic {

    public String findLongestWord(String sentence) {

        // Edge Case: If the sentence is empty, return an empty string
        if (sentence.isEmpty()) {
            return "";
        }

        // Split the sentence into words using space as the separator
        String[] words = sentence.split(" ");

        // Initialize variables to keep track of the longest word and its length
        String longestWord = "";
        int maxLength = 0;

        // Iterate over each word in the words array
        for (String word : words) {

            // If the length of the current word is more than maxLength, update longestWord and maxLength
            if (word.length() > maxLength) {
                longestWord = word;
                maxLength = word.length();
            }
        }

        // Return the longest word found in the sentence


        return longestWord;
        }
}
```

<br></br>

### 9. wrapper class

- 기본 타입의 데이터를 객체로 표현하기 위해 사용하는 class
- wrapper class로 감싼 기본 타입 값은 외부에서 변경할 수 없으며, 변경을 위해선 새로운 wrapper object를 만들어야 한다.
- java.lang package에 포함되어 있기 때문에, 사용에 있어 package를 불러올 필요 없다.

- wrapper class 이용, 데이터를 parameter로 받아 해당 값을 가지는 객체 생성

```java
Integer num1 = new Integer(5); // 기본형 타입 정수를 래퍼 클래스로 감싸 객체화
Integer num1 = 5; // 이런식으로도 표현 가능

Double num2 = new Double(1.11); // 기본형 타입 실수를 래퍼 클래스로 감싸 객체화
Double num2 = 1.11;
```

- 기본 타입

  - byte short int long float double char boolean

- wrapper class

  - Byte Short Integer Long Float Double Character Boolean

- 상호 변환
  - Boxing : 기본 타입의 데이터 → 래퍼 클래스의 인스턴스로 변환
  - UnBoxing : 래퍼 클래스의 인스턴스에 저장된 값 → 기본 타입의 데이터로 변환

```java
// Boxing
Integer num = new Integer(20); // Integer 래퍼 클래스 num 에 21 의 값을 저장

// Unboxing (intValue)
int n = num.intValue(); // 래퍼 클래스 num 의 값을 꺼내 가져온다.

// 재 포장(박싱)
n = n + 100; // 120
num = new Integer(n);
```

- unboxing method

  - booleanValue() byteValue() doubleValue() floatValue() intValue() longValue() shortValue()

- AutoBoxing & AutoUnBoxing
  - JDK 1.5 부터는 박싱과 언박싱이 필요한 상황에 자바 컴파일러가 자동으로 처리해주기 시작했다.이러한 자동화된 박싱과 언박싱이 오토박싱 (AutoBoxing) 과  오토언박싱 (AutoUnBoxing)
  - 기본타입 값을 직접 박싱, 언박싱하지 않아도 래퍼 클래스 변수에 대입만 하면 자동으로 박싱과 언박싱 처리

```java
/* 기존 박싱 & 언박싱 */
Integer num = new Integer(17); // 박싱
int n = num.intValue();        // 언박싱

/* 오토 박싱 & 언박싱 */
Integer num = 17; // new Integer() 생략
int n = num; // intValue() 생략
```

- 오토 박싱 & 언박싱 기능을 이용해 다음과 같이 래퍼 객체를 직접 연산이 가능
- 원래는 래퍼 클래스는 직접 연산이 불가능 하지만 컴파일러가 스스로 판단해 자동으로 언박싱하여 연산 하기 때문에 다음 구문이 허용

```java
Integer num1 = new Integer(7); // 박싱
Integer num2 = new Integer(3); // 박싱

int int1 = num1.intValue();    // 언박싱
int int2 = num2.intValue();    // 언박싱

// 박싱된 객체를 오토 언박싱하여 연산하고 다시 박싱하여 저장
Integer result1 = num1 + num2; // 10
Integer result2 = int1 - int2; // 4
int result3 = num1 * int2;     // 21
```

- 오토 언박싱을 통해 객체 값을 더하고 빼고는 문제는 없지만, 객체 값을 비교를 할때 문제 발생 가능
  - 인스턴스에 저장된 값에 대한 동등 여부 판단은 동등 연산자 == 으로는 값을 비교하는게 아닌 객체의 주소값을 비교해서 의도적이지 않은 작동 발생 가능

```java
Integer num1 = new Integer(10);
Integer num2 = new Integer(20);
Integer num3 = new Integer(10);

System.out.println(num1 == num3);      // false
System.out.println(num1.equals(num3)); // true

// 동등 비교 외의 연산은 문제 없다.
System.out.println(num1 < num2);       // true
System.out.println(num1 + num2);       // 30
```

- 대신 래퍼 클래스와 기본 자료형과의 비교는 자동으로 오토박싱과 언박싱을 해주기 때문에 == 연산과 equals 연산 모두 가능하다.

```java
Integer num = new Integer(10); // 래퍼 클래스1
Integer num2 = new Integer(10); // 래퍼 클래스2
int i = 10; // 기본타입

// 래퍼클래스 == 기본타입
System.out.println(num == i); // true

// 래퍼클래스.equals(기본타입)
System.out.println(num.equals(i)); // true

// 래퍼클래스 == 래퍼클래스
System.out.println(num == num2); // false (invalid)

// 래퍼클래스.equals(래퍼클래스)
System.out.println(num.equals(num2)); // true
```

- 객체를 포장하는 기능 외에도, 래퍼 클래스는 자체 지원하는 parse타입() 메소드를 이용하여 데이터 타입을 형 변환 할때도 유용히 쓰임

```java
String str = "10";
String str2 = "10.5";
String str3 = "true";

byte b = Byte.parseByte(str);
int i = Integer.parseInt(str);
short s = Short.parseShort(str);
long l = Long.parseLong(str);
float f = Float.parseFloat(str2);
double d = Double.parseDouble(str2);
boolean bool = Boolean.parseBoolean(str3);

System.out.println("문자열 byte값 변환 : "+b);
System.out.println("문자열 int값 변환 : "+i);
System.out.println("문자열 short값 변환 : "+s);
System.out.println("문자열 long값 변환 : "+l);
System.out.println("문자열 float값 변환 : "+f);
System.out.println("문자열 double값 변환 : "+d);
System.out.println("문자열 boolean값 변환 : "+bool);
```

- 주의 사항
  - 기능적 편의성을 위하여 오토 박싱 / 언박싱을 제공하지만, 다른 타입간의 형 변환은 어플리케이션의 성능에 영향 존재. 비록 사소한 차이 일지라도 어플리케이션의 성능 측면에서 봤을때 반드시 필요한 상황이 아니라면 지양 해야함

#### Reference

[Inpa Dev 👨‍💻:티스토리](https://inpa.tistory.com/entry/JAVA-☕-wrapper-class-Boxing-UnBoxing)

### 10. list

저장된 요소들의 순서가 있고, 데이터 간 중복이 가능하고, index 번호에 의해 정렬된다.

- 특징

  - Collection 인터페이스 중 하나
  - 배열로 이루어진 ArrayList 와 LinkedList 두 종류
  - 크기 조절이 가능
  - 초기 크기 지정하지 않아도 됨
  - 삭제는 공간을 지우는 것

- 선언 방식  
   `java List<자료형> 리스트 명 = new ArrayList(or LinkedList)<자료형(생략가능)>();`

  ```java
  import java.util.ArrayList;  // ArratList 선언 시

  import java.util.LinkedList; // LinkedList 선언 시
  import java.util.List;
  ```

  <br>은 제네릭이다.

- list 사용 - List.add(value); : 값 삽입

      - List.add(index, value); : index 중간에 넣을 인덱스(배열 인덱스), value: 중간에 넣을 값. 중간에 값을 넣을 경우 중간에 넣은 값 이후에 값들은 한 칸씩 밀림

      - List.set(index, value); : index는 치환할 값 자리 인덱스, value는 치환할 자리 값

      - List.remove(index); : 인덱스 위치에 있는 값 삭제

      - List.clear(); 모든 요소 삭제

      - List.get(index) : 인덱스 위치에 있는 값 출력

      - List.size() : 리스트 크기 출력

  <br></br>

- Ex) array list

  ````java
  import java.util.ArrayList;
  import java.util.List;
  import java.util.Random;

      public class ArrayListTest01 {

      public static void main(String[] args) {

      	// ArrayList 생성
      	// 컬렉션 계열에서 데이터 타입을 지정하기 위해서 제네릭 사용
      	// <데이터 타입> 을 쓴다.
      	// 데이터 타입은 일반 변수 타입이 아닌 Wrapper class 타입으로 지정
      	// ArrayList와 배열에 차이는 ArrayList는 크기를 먼저 지정하지 않아도 된다. 배열은 크기를 먼저 지정하고 사용해야 한다.
      	List<Integer> list = new ArrayList<>();

      	// 데이터 타입 - random 클래스
      	Random ran = new Random();
      	for (int i = 0; i < 5; i++) {
      		list.add(ran.nextInt(30) + 1); // random에 +1을 안 해 주면 0 ~ 29까지만 사용된다.
      	}
      	// 출력 - 출력은 배열 출력과 거의 비슷하다.

      	for (int i = 0; i < 5; i++) {
      		System.out.print(list.get(i) + "\t");
      	}
      	System.out.println();

      	// 중간 삽입 - index 3 (4 번째) 중간 삽입
      	list.add(3, 35);
      	for (int i = 0; i < list.size(); i++) {
      		System.out.print(list.get(i) + "\t");
      	}
      	System.out.println();

      	// 치환 - 첫 번째 값을 치환
      	list.set(0, 40);

      	// 삭제 전 list 크기
      	System.out.println("삭제 전 lsit 크기: " + list.size());

      	// 삭제 - 마지막 인덱스 삭제
      	list.remove(4);

      	// 삭제 후 list 크기
      	System.out.println("삭제 후 list 크기: " + list.size());

      	for (int i = 0; i < 5; i++) {
      		System.out.print(list.get(i) + "\t");
      	}
      	System.out.println();
      	System.out.print("iterator 사용: "+"\t");
      	for (int i : list) {
      		System.out.print(i + "\t");
      	}
      }
      }
      ```

      ```java
      import java.util.ArrayList;
      import java.util.List;

      public class NumberMagic {

      public List<Integer> determineMultiples(int number, int limit) {

          // Edge case: If the number is 0 or negative, or the limit is 0 or less, return an empty list
          if (number <= 0 || limit <= 0) {
              return new ArrayList<>();
          }

          List<Integer> multiples = new ArrayList<>();

          // Starting from 1, multiply the number by each integer until the product is less than the limit
          for (int i = 1; i * number < limit; i++) {
              // Add the product to the list
              multiples.add(i * number);
          }

          return multiples;
      }

  }
  ````

  <br></br>

- Ex) linked list

  ```java
  import java.util.LinkedList;
  import java.util.List;

  public class LinkedListTest01 {

  public static void main(String[] args) {

  	List<Integer> list = new LinkedList<>(); // LinkedList 생성

  	list.add(1); // 값 추가
  	list.add(2);
  	list.add(3);
  	list.add(4);

  	System.out.print("추가된 값: ");
  	for (int l : list) { // iterator를 이용해 리스트에 값 출력
  		System.out.print(l + "\t");
  	}
  	System.out.println();

  	list.set(2, 5); // 리스트 수정

  	System.out.print("수정된 값: ");
  	for (int l : list) { // iterator를 이용해 리스트에 값 출력
  		System.out.print(l + "\t");
  	}
  	System.out.println();

  	list.remove(1); // 리스트 삭제

  	System.out.print("삭제된 값: ");
  	for (int i = 0; i < list.size(); i++) { // 일반 for를 이용해서 반복
  		System.out.print(list.get(i) + "\t"); // .get() 메서드를 이용해 리스트에 값 출력
  	}
  	System.out.println();
  }
  }
  ```

### 11. OOP(Object Oriented Programming)

#### 0. Concept

OOP의 핵심은 객체와 클래스  
또한, 객체의 속성(Attribute)과 상태(State)를 나타내는 데이터  
객체 또는 스스로 변화하는 행동(Method)로도 볼 수 있음

객체는 클래스의 인스턴스로 각각의 객체는 상태 행동 식별자를 가지고 있음  
또한, 상호간 호출을 통해 통신(message passing)

하나의 클래스를 통해 필요로 하는 어플리케이션에 여러개의 객체 생성 가능  
각 객체의 식별은 JVM에 의해 유지되며, Java 객체를 만들 때 마다  
JVM은 객체에 대한 해시코드를 만들고 할당하여 각 객체가 고유하게 식별되도록 함

생성자는 반환 값이 없는 특수한 메서드  
생성자의 이름은 항상 클래스의 이름과 동일하며 초기 객체 상태를 설정하기 위한 매개 변수를 사용할 수 있음  
생성자를 작성하지 않는 경우 JVM은 기본 생성자를 할당하며 이는 매개변수를 허용하지 않기 때문에 매개변수가 필요한 경우, 개발자가 직접 생성자를 작성해야함

4개 원칙

1.  추상화(Abstraction)  
    추상화는 공개할 정보와 숨길 정보를 구분하는 것  
    일반적으로 데이터 추상화와 제어 추상확가 있음

    데이터 추상화는 복잡한 데이터 형태를 생성하기 위해 여러 작은 데이터 타입을 사용하는 방법

    ```java
    // 데이터 추상화
    public class Employee
    {
        private Department department;
        private Address address;
        private Education education;
        //So on...
    }
    ```

    제어 추상화는 사용자에게 메소드 로직을 숨기기 위해 사용  
    메소드 내 로직의 변경이 있어도, 사용자에게 영향을 주지 않음

    ```java
    //제어 추상화
    public class EmployeeManager
    {
        public Address getPrefferedAddress(Employee e)
        {
            //Get all addresses from database
            //Apply logic to determine which address is     preferred
            //Return address
        }
    }
    ```

2.  캡슐화(Encapsulation)  
     캡슐화는 특정 변수와 함수를 하나의 클래스로 묶어 외부로의 접근을 막는 방법  
     객체가 제공하는 필드와 메소드를 통한 접근만 가능  
     정보은닉과 구현은닉으로 나뉨

    정보은닉의 방법으로 접근제어자를 사용 외부에서 접근할 수 없도록 함 (인터페이스 사용 방식)  
    구현은닉은 객체가 책임을 이행하는 방식을 수정할 수 있도록 하여 개발자에게 자유 제공  
    설계가 변경되었을 때 유용하게 사용

        ```java
        //정보 은닉(information hiding)
        class InformationHiding
        {
            //Restrict direct access to inward data
            private ArrayList items = new ArrayList();

            //Provide a way to access data - internal logic can     safely be changed in future
            public ArrayList getItems(){
                return items;
            }
        }
        ```

        ```java
        //(구현 은닉)implementation hiding

        interface ImplemenatationHiding {
        Integer sumAllItems(ArrayList items);
        }
        class InformationHiding implements  ImplemenatationHiding
        {
        //Restrict direct access to inward data
        private ArrayList items = new ArrayList();

            //Provide a way to access data - internal logic     can safely be changed in future
            public ArrayList getItems(){
            return items;
            }

            public Integer sumAllItems(ArrayList items) {
                //Here you may do N number of things in any     sequence
                //Which you do not want your clients to know
                //You can change the sequence or even whole     logic
                //without affecting the client
            }

        }
        ```

3.  상속(Inheritance)
    부모클래스의 속성과 행동을 사용하게 됨  
    코드의 재사용ㅇ성과 유지보수를 위해 사용  
    상속을 위해서 extends 키워드로 부모 클래스 명시해 사용  
    상속되는 클래스 super 클래스  
    상속받는 클래스 sub 클래스

    sub 클래스는 super 클래스의 non-private 멤버들을 상속 받음  
    생성자는 멤버가 아니기 때문에 상속되지 않으나,  
    sub 클래스에서 super 클래스의 생성자를 호출 가능

4.  다형성(polymorphism)
    다향성은 같은 자료형에 열러가지 객체 대입해 다양한 결과를 얻어내는 성질  
    동일한 이름의 여러 형태의 메소드 제작 가능  
    기본적으로 두가지 방법 compile time polymorphism / runtime polymorphism

    compile time polymorphism은 컴파일러가 필요한 모든 정보를 가지고 있고, 프로그램 컴파일 중 호출할 방법을 알기 때문에 컴파일 시간에 적절한 메소드를 각각의 객체에 바인딩 가능  
    정적바인딩이나 early binding이라함.  
    메소드 오버로딩을 통해 사용되며, 오버로딩에 따라 메소드의 매개변수의 형태가 달라짐

    runtime polymorphism 동적 바인딩이라 불리며 메소드 오버라이딩과 연관 있음  
    일반적으로 부모 클래스에 자식 클래스가 존재할때 사용  
    부모 자식 클래스에 존재하는 메소드를 실행시키면  
    런타임과정에서 해당 인스턴스에 맞는 메소드를 호출하게 됨

    ```java
    class Animal {
    public void sound() {
         System.out.println("Some sound");
    }
    }

    class Lion extends Animal {
      public void sound() {
            System.out.println("Roar");
      }
    }

    class Main
    {
      public static void main(String[] args)
      {
            //Parent class reference is pointing to a     parent object
            Animal animal = new Animal();
            animal.sound(); //Some sound

            //Parent class reference is pointing to a child     object
            Animal animal = new Lion();
            animal.sound(); //Roar
      }
    }
    ```

#### 1. Basic Class structure

##### package

선언 :  
`java package 패키지명;`

도메인 이름 역순 + 마지막에 프로젝트 이름을 붙여준다.

```java
ex)
com.samsung.projectName
com.lg.projectName
com.hyudai.projectName
```

패키지 사용 :  
import문의 역할은 컴파일러에게 소스파일에 사용된 클래스의 패키지에 대한 정보 제공.  
import문으로 사용하고자 하는 클래스의 패키지를 미리 명시해주면 소스코드에
사용되는 클래스이름에서 패키지명 생략 가능.

```java
import 패키지명.클래스명;
import 패키지명.*;

package com.mycompany;

import com.hankook.Tire;

public class Car {
	Tire tire = new Tire();
}
```

import문으로 지정된 패키지의 하위 패키지는 import 대상 아님

하위 패키지에 있는 클래스들도 사용하고 싶다면 import문을 하나 더 작성해야함  
서로 다른 패키지에 동일한 클래스 이름이 존재  
두 패키지가 모두 import되어 있을 경우 패키지 이름 전체를 기술해야함

#### 2. toString

기본적으로 Object 클래스의 toString() 메소드는 해당 인스턴스에 대한 정보를 문자열로 반환  
인스턴스에 대한 정보를 문자열로 제공하는게 목적
이때 반환되는 문자열은 클래스 이름과 함께 구분자로 @가 사용되며, 그 뒤로 16진수 해시 코드(hash code)가 추가  
해시 코드 값은 인스턴스의 주소를 해싱하여 변환한 값

객체의 고유 정보를 출력하고 싶은 경우, Overriding을 통해 toString() 메소드를 재정의 해주면 됨

```java
class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // @Overriding : 오버라이딩은 메서드 시그니처가 일치해야 한다. 블록 안의 내용만 재정의 하는 것이다.
    public String toString() {
        return String.format("이름 : %s, 나이 : %d세", this.name, this.age);
    }
}

public class Main {
    public static void main(String[] args) {
        Person p1 = new Person("홍길동", 54);

        // p1 객체를 출력하면 이름과 나이가 출력
        System.out.println(p1); // 이름 : 홍길동, 나이 : 54세
    }
}
```

#### 3. super

자신이 상속받은 부모를 가리키는 참조 변수 super

```java
// 예제 1
class Object{
  int a;
}

class A extends Object{
  int a;
}

public static void main(String args[]){
  A ins = new A();
  ins.a=2 // 여기서 a는 A의 a. 즉, 자식의 변수이다
  // 만약 자식에게 a라는 변수가 없었다면 부모의 a를 가리켰을 것이다.
  // 여기서 자식 a가 아닌 부모의 a로 접근하고 싶다면?

  ins.super.a = 20; // 이렇게 super라는 참조 변수를 사용해서 부모의 a에 접근할 수 있다
  }
  // 위와 같은 이유로 자바에서는 다중 상속이 불가능하다 (상속의 모호성)
```

자식클래스가 인스턴스를 생성하면, 인스턴스 안에는 자식 클래스의 고유 멤버 뿐만 아니라 부모 클래스의 모든 멤버까지 포함.

그러나, 생성자는 상속되지 않음  
따라서 부모클래스의 멤버를 초기화하기 위해선, 당연히 부모클래스의 생성자를 호출 필요  
자식클래스 생성자를 호출할 때 부모클래스 생성자도 동시에 호출해야함

자바 컴파일러가 자동으로 super() 메소드를 추가해줌

컴파일러가 항상 super()를 자동 추가해주는 것은 아님
아래 예제처럼 부모클래스에 기본 생성자가 아닌 매개변수를 가지는 생성자가 있다면(=부모클래스에서 생성자가 오버로딩되면) 자동으로 추가되지 않음 (=묵시적 제공을 하지 않음)  

```java
 class Parent{
     int a;
     Parent(int n){a=n;};
 }
 
 class Child extends Parent(){
     int b;
     Child(){
         super()
         b=20;
     }
 }
 // 이게 오류라면 super(20) 했을 땐 어떻게 될까? 나중에 되는지 test해보자
 // 기본생성자도 없고 매개변수가 있는 생성자도 없으면? 나중에 되는지 test
```

왜냐하면 부모클래스 자체에 기본 생성자가 추가되지 않았기 때문 기본생성자를 호출할 때 부모클래스의 생성자에 기본생성자가 없으면 에러 발생

1. 부모클래스에 기본 생성자 선언 (명시된 문제 그대로의 해결)
```java
class Parent{
    int a;
    Parent(){a=10;};
    Parent(int n){a=n;};
}

class Child extends Parent(){
    int b;
    Child(){
        super();
        b=20;
    }
}
```

2. 오버로딩된 생성자에 맞춰 super()의 인자를 맞춰줌 

```java
class Parent{
    int a;
    Parent(int n){a=n;};
}

class Child extends Parent(){
    int b;
    Child(){
        super(40);
        b=20;
    }
}
```

#### 4. abstract

추상화란 사용자가 어떤 기능을 사용할때, 그 기능에 대한 로직을 이해하지 않고도 사용할 수 있도록 함   

추상 클래스란 클래스에 추상화를 접목 시켜 보다 구조적이게 객체를 설계하고, 프로그램의 유지보수성을 올려주며, 만일 프로그램에 어떠한 기능을 업그레이드한다고 하면 수정 / 추가에 대해 유연적이게 해주어, 퀄리티 높은 프로그램과 솔루션을 개발할 수 있게함  
실제로 추상 클래스는 개별 프로젝트 보다는 범용 라이브러리나 프레임워크 시스템을 설계하는데 유용하게 사용

자바에서는 abstract 키워드를 클래스명과 메서드명 옆에 붙임으로서 컴파일러에게 추상 클래스와 추상 메서드임을 알려줌  
추상 메서드는 작동 로직은 없고 이름만 껍데기만 있는 메서드   
메서드의 선언부만 작성하고 구현부는 미완성인 채로 남겨둔 메소드   
(메소드의 구현부인 중괄호가 없는 형태)

추상 클래스 안의 메서드를 미완성으로 남겨놓는 이유는 추상 클래스를 상속받는 자식 클래스의 주제에 따라서 상속 받는 메서드의 내용이 달라질 수 있기 때문   
부모(추상) 클래스에서 메서드를 선언부만을 작성하고, 실제 내용은 상속받는 클래스에서 구현하도록 하기 위해 일부러 비워두는 개념  
따라서 추상 클래스를 상속받는 자식 클래스는 부모의 추상 메서드를 상황에 맞게 적절히 재정의 하여 구현해 주어야 비로소 사용이 가능   
즉, 클래스의 선언부에 abstract 키워드가 있다는 말은 안에 추상 메서드(abstract method)가 있으니 상속을 통해서 구현해주라는 지침 

```java
// 추상 클래스
abstract class Pet {
    abstract public void walk(); // 추상 메소드
    abstract public void eat(); // 추상 메소드
    
    public int health; // 인스턴스 필드
    public void run() {  // 인스턴스 메소드
    	System.out.println("run run");
    }
}

class Dog extends Pet {
	// 상속 받은 부모(추상) 메소드를 직접 구현
    public void walk() {
        System.out.println("Dog walk");
    }
    public void eat() {
    	System.out.println("Dog eat");
    }
}

public class main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat(); // 부모(추상) 클래스로 부터 상속받은 추상 메소드를 직접 구현한 메소드를 실행
        d.walk();
        d.run(); // 부모(추상) 클래스의 인스턴스 메소드 실행
    }
}
```

추상 클래스 생성자
추상 클래스는 클래스의 일종이라고 하지만 new 생성자를 통해 인스턴스 객체로 직접 만들 수 없음   
왜냐하면 추상클래스는 상속 구조에서 부모 클래스를 나타내는 역할로만 이용  

```java
abstract class Animal { 
}

Animal a = new Animal(); // ERROR !! - 추상 클래스는 인스턴스를 직접 바로 생성할 수 없음.
```

따라서 반드시 추상 클래스를 어느 자식의 클래스에 상속시키고, 자식 클래스를 인스턴스화 하여 사용해야함

```java
abstract class Animal { 
}

class Cat extends Animal { // 추상 클래스 상속
}

class Dog extends Animal { 
}

public class Main {
    public static void main(String[] args) {
		// 추상 클래스를 상속한 자식 클래스를 객체로 초기화
        Cat c = new Cat(); 
        Dog d = new Dog();
    }
}
```

그렇다고 추상 클래스의 생성자를 전혀 이용 못하는 것은 아님    
직접적인 인스턴스화가 불가능 하다 뿐이지, super() 메소드를 이용해 추상 클래스 생성자 호출이 가능      
이는 객체의 시본 생성자 메서드 실행 순서 원리를 그대로 따른 것

```java
// 추상 클래스
abstract class Shape {
	public String type;
    
    // 추상 클래스 생성자
    public Shape(String type) {
    	this.type = type;
    }
    
    // 추상 메서드
    public abstract void draw();
}

class Figure extends Shape {
	public String name;
    
    public Figure(String type1, String type2) {
    	super(type1); // 부모 추상 클래스 생성자 호출
        name = type2;
    }
    
    @Override
    public void draw() { ... } // 추상 메서드 구현
}

public class main {
    public static void main(String[] args) {
		Figure f = new Figure("polygon", "square");
        f.name; // "square"
        f.type; // "polygon" - 부모(추상) 클래스의 멤버를 추상 클래스 생성자를 호출하는 super()을 통해 초기화
    }
}
```

추상 클래스를 상속한 자식 클래스를 new 생성자로 객체를 초기화할때, 자식 클래스 생성자 메소드 내에서 가장 먼저 부모 클래스인 추상 클래스의 생성자가 실행되게 됨   
그래서 만일 위와 같이 부모 추상 클래스 생성자 실행에 있어 인자를 주어 제어를 하고 싶다면, 자식 클래스 생성자 메서드 내에서 super() 부모 생성자 호출 메서드를 통해 가능


추상 클래스는 미완성 설계도  
추상 클래스만으로는 인스턴스를 생성할 수 없고 자식 클래스에서 상속받아야만 완성시킬 수 있기 때문  
이처럼 추상 클래스는 클래스로서의 역할을 다 못하지만, 새로운 클래스를 작성하는 데 있어서 바탕이 되는 부모 클래스로서 중요한 의미  
추상 클래스를 이용하면 객체 지향 프로그래밍에서 중요한 특징인 다형성을 가지는 메소드의 집합을 정의할 수 있도록 멘토 

공통 멤버의 통합으로 중복 제거
다음과 같이 Marine, Tank, Dropship 클래스가 정의되어 있다고 하자 클래스의 멤버들을 자세히 살펴보니 사용처와 이름이 겹치는 필드와 메서드들이 몇몇 보임

```java
class Marine {
    int x, y;
    void move(int x, int y) {} // 지정된 위치로 이동
    void stop() {} // 현재 위치에 정지
    void stimPack() {} // 고유 능력 스팀팩 사용
}

class Tank {
    int x, y;
    void move(int x, int y) {} // 지정된 위치로 이동
    void stop() {} // 현재 위치에 정지
    void siegeMode() {} // 고유 능력 시즈 모드 사용
}

class DropShip {
    int x, y;
    void move(int x, int y) {} // 지정된 위치로 이동
    void stop() {} // 현재 위치에 정지
    void loadUnload() {} // 고유 능력 탑승 사용
}
```

따라서 상속(extends) 기능을 이용해 3개의 클래스를 대표할 수 있는 부모 추상 클래스로 묶으면, 상위 클래스의 특징을 하위클래스에서 그대로 물려 받아 사용할 수 있는 상속 특징을 이용하여 코드의 중복 제거, 코드 재사용성 증대 효과를 누릴 수 있게 됨    
즉, 자주 사용될 것이 예상되는 기능을 모아놓은 추상 클래스를 한번 만들어 놓으면 편하게 재사용을 함으로써 유지보수 효율화를 추구 가능

```java
abstract class Unit {
    int x, y;
    abstract void move(int x, int y); // 지정된 위치로 이동
    void stop() {} // 현재 위치에 정지
}

class Marine extends Unit{
    void move(int x, int y) {
        System.out.println("걸어서 이동");
    }
    void stimPack() {} // 고유 능력 스팀팩 사용
}

class Tank extends Unit{
    void move(int x, int y) {
        System.out.println("굴러서 이동");
    }
    void siegeMode() {} // 고유 능력 시즈 모드 사용
}

class DropShip extends Unit{
    void move(int x, int y) {
        System.out.println("날아서 이동");
    }
    void loadUnload() {} // 고유 능력 탑승 사용
}
```

대신에 현재 위치에 정지하는 메소드인 stop() 은 어떤 유닛이건 간에 명령이 동일하지만, 유닛이 이동하는 메소드인 move() 는 각 자식 클래스마다 이동하는 로직이 다르기 때문에 부모 클래스의 메소드를 오버라이딩 하여 재정의   
하지만 가만 생각해보면 굳이 추상 클래스로 선언할 필요가 없음         abstract 키워드를 빼고 일반 부모 클래스로 선언해도 상속하고 중복 멤버를 제거하는데 전혀 문제가 없기 때문

```java
class Unit { // abstract 뺌
    int x, y;
    void move(int x, int y) {} // abstract 뺌
    void stop() {}
}

class Marine extends Unit{
    void move(int x, int y) {
        System.out.println("걸어서 이동");
    }
    void stimPack() {} 
}

class Tank extends Unit{
    void move(int x, int y) {
        System.out.println("굴러서 이동");
    }
    void siegeMode() {} 
}

class DropShip extends Unit{
    void move(int x, int y) {
        System.out.println("날아서 이동");
    }
    void loadUnload() {} 
}
```

구현의 강제성을 통한 기능 보장
위의 자식 클래스들을 다음 메인 메소드에서 인스턴스화 하여 사용한다고 하자.
각 자식들을 Unit 이라는 부모 클래스 타입으로 묶었으니, 업캐스팅을 통해 Unit 배열에 자식 객체들을 할당 할 수 있게됨 
그리고 for문을 통해 배열 요소들을 순회하여 move() 메소드를 실행하도록 다형성을 이용한 효율적인 코드를 구성


```java
public class Test1 {
    public static void main(String[] args) {
        Unit[] group = new Unit[3];
        group[0] = new Marine();
        group[1] = new Tank();
        group[2] = new DropShip();

        for(Unit u : group) {
            u.move(100, 200);
        }
    }
}
```

이때 만일 스펙이 추가되어, Battlecruiser 클래스를 추가하게 되었고 여타 자식 클래스와 똑같이 Unit 부모 클래스에 상속 시킨다고 가정

```java
abstract class Unit {
    int x, y;
    abstract void move(int x, int y); // 지정된 위치로 이동
    void stop() {} // 현재 위치에 정지
}

class Battlecruiser extends Unit {
    void yamato() {} // 고유 능력 야마토 사용
}

class Marine extends Unit { ... }

class Tank extends Unit { ... }

class DropShip extends Unit { ... }
```

Copy
그런데 개발자가 깜빡하고 배틀크루저의 이동에 관한 메소드를 정의를 안해버렸다고 해보자. 유닛의 치명적인 버그가 일어 날 수 있는 상황임에도 불구하고 만일 추상 클래스의 추상 메소드로 상속 관계를 맺었다면 이는 큰 문제가 되지 않음   
에디터에서 미리 다음과 같이 빨간줄을 통해 추상 메서드 move() 를 재정의 하지 않았다면서 오류를 보여주어 바로 수정이 가능하기 때문

위에서 언급했듯이 자바에서 추상 클래스와 추상 메소드를 선언하여 사용하는 목적은 추상 클래스를 상속받는 자식 클래스가 반드시 추상 메소드를 구현하도록 하기 위함  
이렇게 강제적으로 구현하도록 멘토링을 하기 때문에 개발자가 실수해도 바로 고칠수 있게됨   
그럼 추상 클래스, 추상 메소드가 아닌 일반 클래스로 상속 관계를 맺는 상황에서 위와 같은 프로그래밍 실수가 일어나면 어떻게 될까?
우선 에디터에서는 어떤 에러도 내뿜지 않는다. 왜냐하면 일반 클래스의 메서드를 오버라이딩 하든 안하든 그건 자유이기 때문

하지만 문제는 메인부의 move() 메소드 호출 부분
배틀크루저 클래스내에 직접 move() 메소드를 정의해 놓지 않으면, 호출 됬을때 결국 부모 클래스의 move() 메소드가 실행 될 것이고 이는 잘못된 동작이 나타나게 하거나 아예 동작 자체가 안되는 심각한 게임 버그 현상이 일어나게 됨   
미리 에디터에서 알려주면 좋겠으려만 실제 프로그램을 구동하고 유닛을 조종해 봐야 일어날 수 있는 버그 현상이라 디버깅으로도 찾기 매우 힘든 부분

이처럼 추상 메소드를 통한 강제 구현의 멘토링은 기존 프로그램 스펙에서 수정하거나 기능을 추가할때 일어날 수 있는 문제 되는 점을 미리 방지함으로써 보다 안정적이고 구조적으로 프로그래밍 할 수 있게 도와줌

규격에 맞는 설계 구현
어떤 제품이든 그 제품이 추구하는의 설계서 즉, 규격이 정해져 있을 것이다. 실생활의 예로 USB의 단자에는 규격이 존재   
이 규격이 존재한 덕분에 우리는 어떤 제조사의 USB를 사도 모든 컴퓨터에 연결해서 저장 기능을 이용할 수 있는 것    
만일 규격이 정해져 있지 않는다면 호환성에 매우 애를 먹을 것   
이처럼 '규격'은 소비자가 제품을 사용함에 있어서 큰 장점을 발휘하지만, 개발자가 제품을 구현하는데 있어서도 도움을 줌   
예를 들어 갑자기 안드로이드 어플을 구성하는 클래스를 만들라고하면, 어플과 휴대폰의 연동에 대한 규격이 없다면, 어디서부터 설게해야 될지도 몰라 시간을 잡아 먹게 될 것   
하지만 구글이 미리 만들어둔 안드로이드 SDK에서 제공하는 추상 클래스를 상속 받아 필요한 추상 메소드를 구현함으로써 개발자는 내부 동작만 창의적인 스타일을 구현해 심장박동 어플을 내든, 배달 어플을 내든, 게임 어플을 내든 다양한 제품을 내보일 수 있는 것

만일 안드로이드 규격에 따르지 않으면 위의 배틀크루저 클래스 예시와 같이 IDE에서 에러를 일으키기 때문에 오동작에 대한 걱정을 필터링 할 수도 있음  
이처럼 실제 프로젝트에서 어플리케이션 아키텍쳐(Application Architecture)가 설계해 놓은 추상 클래스를 상속받으면, 개발자는 프로젝트에서 필요하고 공통적으로 들어가야하는 필드와 메서드를 오버라이딩해서 큰 설계를 생각할 필요 없이 구현만 하면 됨   
이렇게 하면 초기 설계 시간이 절약되고, 구현에만 집중할 수 있게 된다는 장점이 있음

정리하자면 추상클래스를 상속받아서 미리 정의된 공통 기능들을 구현하고, 실체클래스에서 필요한 기능들을 클래스별로 확장시킴으로써 소스 수정시 다른 소스의 영향도를 적게 가져가면서 변화에는 유연하게 만들 수 있음  
미리 규격에 맞게 소스가 구현되어 있기 때문에 해당 규격에 대한 구현부만 수정하면 손 쉽게 기능 수정이 가능하기 때문이다.


#### 5. 인터페이스

인터페이스 정의

인터페이스를 작성하는 것은 추상 클래스를 작성하는 것과 같다고 보면 된다. (추상 메서드 집합)   
인터페이스도 필드를 선언할 수 있지만 변수가 아닌 상수(final)로서만 정의할 수 있음    
public static final 과 public abstract 제어자는 생략이 가능  
인터페이스에 정의된 모든 멤버에 적용되는 사항이기 때문에 편의상 생략 가능하게 지원하는 것이다. 생략된 제어자는 컴파일 시에 컴파일러가 자동으로 추가해줌

```java
interface 인터페이스이름{
    public static final 타입 상수이름 = 값;
    public abstract 타입 메서드이름(매개변수목록);
}

// --------------------------------------------------------

interface TV {
    int MAX_VOLUME = 10; // public static final 생략 가능
    int MIN_VOLUME = 10;

    void turnOn(); // public abstract 생략 가능
    void turnOff();
    void changeVolume(int volume);
    void changeChannel(int channel);
}
```

인터페이스도 추상 클래스처럼 그 자체로는 인스턴스를 생성할 수 없으며, 추상 클래스가 상속을 통해 완성되는 것처럼 인터페이스도 구현부를 만들어주는 클래스에 구현(상속) 되어야 함   
해당 클래스에 인터페이스를 구현하고 싶다면, implements 키워드를 쓴 후에 인터페이스를 나열하면됨   
인터페이스를 상속 받았으면, 자식 클래스에서 인터페이스가 포함하고 있는 추상 메소드를 구체적으로 구현해줌   
인터페이스의 가장 큰 특징은 여러개를 다중 구현(다중 상속)이 가능하다는 것   
자식 클래스에 클래스 상속(extends)와 인터페이스 구현(implements)는 동시에 가능


```java
interface Animal { 
	public abstract void cry(); 
}

interface Pet { 
	public abstract void play(); 
}

class Tail {
	// ...
}

class Cat extends Tail implements Animal, Pet { // 클래스와 인터페이스를 동시에 상속

    public void cry() {
        System.out.println("냐옹냐옹!");
    }

    public void play() {
        System.out.println("쥐 잡기 놀이하자~!");
    }
}
```

만일 클래스가 구현하는 인터페이스의 메서드 중 일부만 구현한다면  abstract 를 붙여서 추상 클래스로 선언해야함  
어찌 보면 당연한게 인터페이스의 추상 메서드 멤버를 그대로 상속받기 때문에, 인터페이스를 상속한 클래스에서 메서드 구현을 안한다면, 곧 추상 메서드를 가진 추상 클래스가 되기 때문

```java
interface Animal {
    void walk();
    void run();
    void breed();
}

// Animal 인터페이스를 일부만 구현하는 포유류 추상 클래스
abstract class Mammalia implements Animal {
    public void walk() { ... }
    public void run() { ... }
    // public void breed() 는 자식 클래스에서 구체적으로 구현하도록 일부로 구현하지 않음 (추상 메서드로 처리)
}

class Lion extends Mammalia {
    @Override
    public void breed() { ... }
}
```

클래스 끼리 상속을 통해 확장을 하듯이, 인터페이스 자체를 확장 시키고 싶다면 extends를 통해 인터페이스를 상속하면됨  
클래스와 달리 인터페이스 끼리의 상속은 다중 상속이 가능 (메소드 구현부가 없으니 충돌 가능성이 없음)   
클래스의 상속과 마찬가지로 자손 인터페이스는 조상 인터페이스에 정의된 멤버를 모두 상속받음    
그러나 필드의 경우 기본적으로 static 이기 때문에 구현체를 따라가지 않게됨 (독립 상수   )
참고로 인터페이스에 클래스를 상속하는 행위는 불가능한데, 왜냐하면 인터페이스는 클래스와는 달리 Object 클래스가 최고 조상이 아니기 때문   

```java
interface Changeable{
    /* 채널을 바꾸는 기능의 메서드 */
    void change();
}

interface Powerable{
    /* 전원을 껐다 켰다 하는 메서드 */
    void power(boolean b);
}

// 채널 기능과 전원 기능을 가진 인터페이스들을 하나의 인터페이스로 통합 상속
interface Controlable extends Changeable, Powerable { 
	// 인터페이스끼리 다중 상속하면 그대로 추상 멤버들을 물려 받음
}

// 클래스에 통합된 인터페이스를 그대로 상속
class MyObject implements Controlable {
	public void change() {
        System.out.println("채널을 바꾸는 기능의 메서드");
    }
    public void power(boolean b) {
        System.out.println("전원을 껐다 켰다 하는 메서드");
    }
}

public class Main {
	public static void main(String[] args) {
        // 인터페이스 다형성 (인터페이스를 타입으로 취급해서 업캐스팅 가능)
        Controlable[] o = { new MyObject(), new MyObject() };
        o[0].change();
        o[0].power(true);
        
        // 각각 단일 인터페이스로도 타입으로 사용이 가능하다. (그러나 지니고 있는 추상 메서드만 사용이 가능하다)
        Changeable inter1 = new Changeable();
        inter1.change(); 

        Powerable inter2 = new Powerable();
        inter2.power(true);
    }
}
```

클래스의 상속일 경우 클래스 필드 멤버끼리 상속되어 덮어 씌워지지만, 인터페이스의 필드들은 모두 public static final 이기에, 서로 상속을 해도 독립적으로 운용

```java
interface Iflower {
    int ex = 10; // 각각 public static final
}

interface IPlant extends Iflower {
    int ex = 20; // 각각 public static final
}

class Tulip implements IPlant {
    int ex = 30; // 그냥 인스턴스 변수
}

public class Main {
	public static void main(String[] args) {
        // 클래스 타입 객체로 ex 멤버에 접근하면, 클래스 인스턴스 변수로 접근
        Tulip t =  new Tulip();
        System.out.println(t.ex); // 30

        // 인터페이스 타입 객체로 멤버에 접근하면, 인터페이스 static 상수로 접근
        Iflower a = new Tulip();
        System.out.println(a.ex); // 10 - 좋지않은 방법
        System.out.println(Iflower.ex); // 10 - 클래스 static 처럼 '인터페이스.멤버' 로 접근

        IPlant b = new Tulip();
        System.out.println(b.ex); // 20 - 좋지않은 방법
        System.out.println(IPlant.ex); // 20 - 클래스 static 처럼 '인터페이스.멤버' 로 접근
    }
}
```

자바에서 .class 파일을 만들 수 있는 것에는 꼭 클래스만 있는 것이 아님   
인터페이스 자체만으로도 클래스명으로 소스 파일을 만들 수 있음

자바8 인터페이스 구현 메소드
본래 인터페이스의 메서드는 몸통(구현체)을 가질 수 없지만, java8 에 이르러서 디폴트 메서드와 스태틱 메소드를 통해 추상 클래스처럼 구현 메소드를 정의 할 수 있게됨   
그래서 이러한 점 때문에 오히려 추상 클래스와의 차이점이 거의 사라졌다고 말하기도 함   
이 기능은 이전 인터페이스를 사용하여 java8의 람다 표현식 기능을 활용할 수 있도록 이전 버전과의 호환성을 위해 추가  

예를 들어 java8 버전부터 새로이 추가된 스트림이나 람다와 같은 함수형 프로그래밍을 컬렉션(Collection) 클래스에서 사용하기 위해, 기존에 만들어놓았던 인터페이스들을 구현하고 있는 컬렉션 클래스들의 구조에서 특정한 기능을 추가해야 되는 상황이 오게됨   

그런데 만일 기존 인터페이스에 추상 메서드를 추가 해버리면, 이 인터페이스를 구현하고 있는 모든 구현 클래스도 변경이 필요해지기 때문에 추상 메서드 대신 디폴트 메서드를 새로이 추가하여 해결하였다고 보면 됨   
또한 앞으로 외부 자바 라이브러리를 이용할때, 라이브러리의 각종 인터페이스에 디폴트 메서드들이 정의되어 있을텐데 이를 익명클래스로 메서드를 호출하거나 오버라이딩 해서 재정의하거나 할때 자주 애용됨
 
그리고 static 메서드는 인스턴스와 관계없는 독립적인 메서드기 때문에 인터페이스에 추가해도 상관없지만, 규칙을 단순히 할 필요가 있어서 자바에서는 허용되지 않음   
이 때문에 인터페이스와 관련된  static 메서드는 별도의 클래스에 따로 두어야 함  
대표적으로  java.util.Collection 인터페이스가 있는데, 이 인터페이스와 관련된  static 메서드들이 인터페이스에는 추상 메서드만 선언할 수 있다는 원칙 때문에 별도의 클래스인 Collections 라는 클래스에 들어가게 됨   
그렇지만 역시 자바8에 와서 위의 제약은 없어지게 되었다.

default 메소드

디폴트 메서드는 앞에 키워드 default 를 붙이며 일반 메서드처럼 구현부 { ... } 가 있어야 함   
디폴트 메서드 역시 접근제어자가 public 이며 생략 가능함   
자식 클래스(구현체)에서 default 메소드를 오버라이딩 하여 재정의 가능함 
보통 인터페이스를 구현한 이후, 수정 과정에서 인터페이스 모든 구현체에게 수정 없이 광역으로 함수를 만들어주고 싶을 때 사용됨 (대신 모든 구현체가 원하는 값을 return 하게 보장하기 위해 @implSpec 자바 doc 태그를 사용해 문서화 해줘야 함)  
주의 해야할점은 인터페이스는 Object 클래스를 상속받지 않기 때문에, Object 클래스가 제공하는 기능(equals, hasCode)는 기본 메소드로 제공할 수 없다. 따라서 구현체가 직접 재정의를 해 주어야함   

```java
interface Calculator {
    int plus(int i, int j);
    int multiple(int i, int j);

    // default로 선언함으로 메소드를 구현할 수 있다.
    default int sub(int i, int j){      
        return i - j;
    }
}

// Calculator인터페이스를 구현한 MyCalculator클래스
class MyCalculator implements Calculator {
    // 추상 메서드만 구현해줌
    @Override
    public int plus(int i, int j) { return i + j; }
    @Override
    public int multiple(int i, int j) { return i * j; }
}

public class Main {
    public static void main(String[] args){
        MyCalculator mycal = new MyCalculator();
        
        // 인터페이스 타입으로 업캐스팅
        Calculator cal = (Calculator) mycal; // 괄호 생략해도 됨

        // 인스턴스의 인터페이스 디폴트 메서드 호출
        int value = cal.sub(5, 10);
        System.out.println(value); // -5
    }
}
```
@implSpec 주석 문서
디폴트 메서드는 보통 인터페이스를 구현한 이후, 수정과정에서 인터페이스 모든 구현체에게 수정 없이 광역으로 함수를 만들어주고 싶을 때 사용됨   
예를 들어 A 와 B 업체가 협업을 해서 어떤 인터페이스를 구현하고 있는데, 개발자가 해당 인터페이스에 기능을 추가하기 위해 추상 메서드를 추가하면, 이 인터페이스를 구현하고 있는 모든 클래스에도 수정을 가해야 함   
그럴때 인터페이스에 디폴트 메서드를 추가하면, 추가된 메서드를 구현체 클래스에서 굳이 구현하지 않아도 에러 없이 사용할 수 있고, 나중에 필요하면 재정의를 통해 업그레이드된 메서드 구현도 가능해짐   
대신 모든 구현체가 원하는 값을 return 하게 보장하기 위해 @implSpec 자바 doc 태그를 사용해 문서화 해줘야함  

```java
interface IJson {
    String printJson(); // 추상 메서드

    /**
     * @impspec 
     * printJson()의 결과를 대문자 변환한다.
     */
    default void uppperString() { // default 메서드
        // 구현 로직상, 추상 메서드인 printJson()의 반환 값이 정상적인 값이 될수도 있고 null이되서 예외 오류가 발생할 수 있으니 @impspec 문서화를 한다.
        String text = printJson().toUpperCase();
        System.out.println(text);
    }
}
```

default 메소드 다중 상속 문제
다중 상속을 금지 시켰더니, 이번엔 인터페이스에 디폴트 메서드라는것이 추가되면서 인터페이스를 다중 구현할때 클래스 다중 상속 문제와 똑같은 문제가 발생되게 됨    
따라서 인터페이스 다중 구현에 한해서 자바에서는 다음과 같은 규칙을 정함
 
1. 다중 인터페이스들 간의 디폴트 메서드 충돌

애초에 똑같은 디폴트 메서드를 가진 두 인터페이스를 하나의 클래스에 구현하고 아무런 조치를 취하지 않으면 컴파일 자체가 되지 않음   
인터페이스를 구현한 클래스에서 디폴트 메서드를 오버라이딩 하여 하나로 통합   


```java
interface A1{
    public void styleA();

    // 메소드 시그니처가 같은 디폴트 메서드
    default public void styleSame(){
        System.out.println("A1 인터페이스의 디폴트 메서드 입니다.");
    }
}

interface B1{
    public void styleB();

    // 메소드 시그니처가 같은 디폴트 메서드
    default public void styleSame(){
        System.out.println("B1 인터페이스의 디폴트 메서드 입니다.");
    }
}

class MultiInterface implements A1, B1 {
    @Override
    public void styleA() {}
    @Override
    public void styleB() {}

    // 두 인터페이스 디폴트 메서드중 A1 인터페이스의 디폴트 메서드를 오버라이딩 하여 구현
    default public void styleSame(){
        System.out.println("A1 인터페이스의 디폴트 메서드 입니다.");
    }
}

public class Main {
    public static void main(String[] args) {
        MultiInterface m1 = new MultiInterface();
        m1.styleSame(); // "A1 인터페이스의 디폴트 메서드 입니다."
    }
}
```

2. 인터페이스의 디폴트 메서드와 부모 클래스 메서드 간의 충돌

위의 상황은 자식 클래스에서 인터페이스와 부모 클래스를 동시에 extends / implement 하였을때 디폴트 메서드와 인스턴스 메서드 간의 충돌을 가정한 상황    
이때는 부모 클래스의 메서드가 상속되고 디폴트 메서드는 무시됨   
만일 인터페이스 쪽의 디폴트 메서드를 사용할 필요가 있다면, 필요한 쪽의 메서드와 같은 내용으로 그냥 오버라이딩 해버리면 됨   


```java
interface A1{
    public void styleA();

    // C1 클래스와 메소드 시그니처가 같은 디폴트 메서드
    default public void styleSame() {
        System.out.println("A1 인터페이스의 디폴트 메서드 입니다.");
    }
}

abstract class C1 {
    // A1 인터페이스와 메소드 시그니처가 같은 인스턴스 메서드
    public void styleSame() {
        System.out.println("C1 클래스의 인스턴스 메서드 입니다.");
    }
}

// 메서드 시그니처가 같은 두 추상화들을 동시에 상속
class MultiClassInterface extends C1 implements A1 {
    @Override
    public void styleA() {}
}

public class Main {
    public static void main(String[] args) {
        MultiClassInterface m1 = new MultiClassInterface();
        m1.styleSame(); // "C1 클래스의 인스턴스 메서드 입니다." - 클래스의 메서드 시그니처가 우선되어 적용됨

        // 마찬가지로 인터페이스 타입으로 다운캐스팅 해도 클래스 인스턴스 메서드로 호출 됨
        ((A1) m1).styleSame(); // "C1 클래스의 인스턴스 메서드 입니다."
    }
}

// 메서드 시그니처가 같은 두 추상화들을 동시에 상속
class MultiClassInterface extends C1 implements A1 {
    @Override
    public void styleA() {}

    // 클래스의 인스턴스 메서드를 무시하고 인터페이스의 디폴트 메서드를 사용하기 위해 그대로 오버라이딩
    public void styleSame() {
        System.out.println("A1 인터페이스의 디폴트 메서드 입니다.");
    }
}

public class Main {
    public static void main(String[] args) {
        MultiClassInterface m1 = new MultiClassInterface();
        m1.styleSame(); // "A1 인터페이스의 디폴트 메서드 입니다."
    }
}
```

default 메소드의 super 
상위 클래스를 상속하고 상위의 메소드를 오버라이딩하여 재정의하였을때, 만일 부모 메서드를 호출할 일이 생긴하면 super 키워드를 통해 부모 메서드를 호출할 수 있음   
이와 같이 인터페이스도 디폴트 메서드를 구현한 클래스에서 오버라이딩 하였을때, super 키워드를 통해 인터페이스의 원래의 디폴트 메서드를 호출이 가능   
다만 문법이 클래스 방식과 약간 차이가 있음   
인터페이스의 super는 다음과 같은 구성으로 호출됨 인터페이스명.super.디폴트메서드


```java
interface IPrint{
    default void print(){
        System.out.println("인터페이스의 디폴트 메서드 입니다.");
    }
}

class MyClass implements IPrint {
    @Override
    public void print() {
        IPrint.super.print(); // 인터페이스의 super 메서드를 호출
        System.out.println("인터페이스의 디폴트 메서드를 오버라이딩한 메서드 입니다.");
    }
}

public class Main {
    public static void main(String[] args) {
        MyClass cls = new MyClass();
        cls.print();
    }
}
```

static 메소드

인스턴스 생성과 상관없이 인터페이스 타입으로 접근해 사용할 수 있는 메서드
인터페이스 전용 static 메소드라 해서 특별한 것은 없다.일반 클래스의 static 메소드와 다를 바 없음 (똑같이 취급 하면 된다)   
해당 타입 관련 헬퍼 또는 유틸리티 메소드를 제공할 때, 인터페이스에 스태틱 메소드로 제공하기도 함 

```java
interface Calculator {
    public int plus(int i, int j);
    public int multiple(int i, int j);

    // 디폴트 메서드
    default int sub(int i, int j){
        return i - j;
    }

    // 스태틱 메서드
    public static void explain(){
        System.out.println("interface static 메서드 입니다. 이 인터페이스는 pluc, multipe, sub 기능을 제공하는 메서드를 지니고 있습니다. (설명)");   
    }
}

class MyCalculator implements Calculator {
    @Override
    public int plus(int i, int j) {  return i + j; }
    @Override
    public int multiple(int i, int j) { return i * j; }
}

public class Main {
    public static void main(String[] args){
        // 클래스 처럼 static 메소드 호출 하면 된다.
        Calculator.explain(); // "interface static 메서드 입니다. 이 인터페이스는 pluc, multipe, sub 기능을 제공하는 메서드를 지니고 있습니다. (설명)"
    }
}
```

private 메소드

자바9 버전에 추가된 메서드
인터페이스에 default, static 메소드가 생긴 이후, 이러한 메소드들의 로직을 공통화하고 재사용하기 위해 생긴 메소드
private 메소드도 구현부를 가져야함   
단, private 메소드는 인터페이스 내부에서만 돌아가는 코드 (인터페이스를 구현한 클래스에서 사용하거나 재정의 할 수 없음)   
따라서 인터페이스 내부에서 private 메소드를 호출할때, default 메소드 내부에서 호출해야 하며,만일 private static 키워드를 붙인 메소드는 static 메소드에서만 호출이 가능함   

```java
interface Calculator {
    public int plus(int i, int j);
    public int multiple(int i, int j);

    // private 메서드
    private void printf() {
        System.out.println("private 메서드는 default 내부에서만 호출이 가능합니다.");
    }

    // private 스태틱 메서드
    private static void printfStatic() {
        System.out.println("private static 메서드는 static 메서드 내부에서만 호출이 가능합니다.");
    }

    // 디폴트 메서드
    default void callPrivate() {
        printf(); // private 메서드 호출
    }

    // 스태틱 메서드
    static void callPrivateStatic() {
        printfStatic(); // private 스태틱 메서드 호출
    }
}

class MyCalculator implements Calculator {
    @Override
    public int plus(int i, int j) {  return i + j; }
    @Override
    public int multiple(int i, int j) { return i * j; }
}

public class Main {
    public static void main(String[] args){
        // 인터페이스 디폴트 메서드를 통한 private 메서드 호출
        Calculator c = new MyCalculator(); // 인터페이스 타입으로 업캐스팅
        c.callPrivate(); // "private 메서드는 default 내부에서만 호출이 가능합니다."

        // 인터페이스 스태틱 메서드를 통한 private static 메서드 호출
        Calculator.callPrivateStatic(); // "private static 메서드는 static 메서드 내부에서만 호출이 가능합니다."
    }
}
```

인터페이스의 다양한 활용도

인터페이스 다형성
부모클래스 타입으로 자식 클래스 타입을 포함 시킬수 있다는 다형성의 법칙도 인터페이스에 고대로 적용이 가능함   
클래스가 여러 개의 인터페이스를 구현하게 되면, 결과적으로 변수의 타입으로도 다양하게 쓰일 수 있다는 것을 의미하게 됨   
인터페이스 타입으로 변수를 선언하게 되면 사용하는 입장에서는 뒤에 오는 모든 객체는 간단히 인터페이스만 구현한 객체이면되기 때문에 좀 더 시스템이 유연해지는 계기를 마련

```java
interface Keyboard { }

class Logitec_Keyboard implements Keyboard { }

class Samsung_Keyboard implements Keyboard { }

class Apple_Keyboard implements Keyboard { }

public class Main {
    public static void main(String[] args) {
    	// 인터페이스 타입 배열로 여러가지 클래스들을 한번에 타입 묶음을 할 수 있다.
        Keyboard[] k = {
                new Logitec_Keyboard(),
                new Samsung_Keyboard(),
                new Apple_Keyboard(),
        };
    }
}
```

또한 세간에는 인터페이스를 자료형으로 쓰는 습관을 들이면 프로그램은 훨씬 유용해진다고 이야기함   
이 말의 의미는 객체는 클래스가 아닌 인터페이스로 참조하라 라는 의미로 확장할 수 있다. 적합한 인터페이스만 있다면 매개변수뿐 아니라 반환값, 변수, 필드를 전부 인터페이스 타입으로 선언하면 좋음

객체는 인터페이스를 사용해 참조   
적당한 인터페이스가 있다면 매개변수뿐만 아니라 반환값, 변수, 필드를 전부 인터페이스 타입으로 선언   
객체의 실제 클래스를 사용할 상황은 '오직' 생성자로 생성할 때 뿐  
매개변수 타입으로는 클래스 보다는 인터페이스를 활용   

예를들어 중복이 없는 집합 자료형을 사용하기 위해 LinkedHashSet 클래스를 초기화 하려할때, 이때 객체의 타입을 똑같이 LinkedHashSet 으로 하지말고 인터페이스인 Set 타입으로 설정하여 선언   

```java
// 나쁜 예) 클래스를 바로 타입으로 사용했다.
LinkedHashSet<Object> s = new LinkedHashSet<>();

// 좋은 예) 인터페이스를 타입으로 사용했다.
Set<Object> s = new LinkedHashSet<>();
```

이런식으로 코드 구현을 해놓는다면, 나중에 변수에 담긴 구현 클래스를 다른 Set 자료형 클래스로 교체하고자 할때 그저 새 클래스의 생성자를 다시 호출해주기만 하면 되어 간편

```java
// 본래 LinkedHashSet으로 구현하였다가 사정이 생겨 TreeSet클래스로 변경해야한다고 하면, 그냥 인터페이스 타입의 변수에 재할당만 하면 된다
Set<Object> s = new LinkedHashSet<>();
s = new TreeSet<>();
```

하지만 이런식으로 인터페이스 타입으로 선언하는 습관은 꼭 좋은 것만 있는 것도 아닌데, 나쁜 예의 경우 LinkedHashSet을 HashSet으로 변환하면, LinkedHashSet 과 달리 HashSet은 반복자의 순회 순서를 보장하지 않기 떄문에 나중에 로직상 문제가 될 수 있기도 함
 
이밖에도 인터페이스는 변수 선언 타입을 넘어서, 메소드의 파라미터나 메소드의 리턴 타입으로도 즐비하게 사용됨   
이 역시 추상 클래스나 상속을 이용하는 것과 차이가 없지만 역시 인터페이스에 선언된 기능을 가진 객체이면 되기 때문에 좀 더 확장성 있는 구조가 되고 상속의 단점을 보완하는 방식의 설계가 가능   

마지막으로 무엇보다 인터페이스의 다형성의 가장 큰 특징은 바로 다중 구현을 통한 자유로운 상속 관계를 만들어 클래스의 다형성보다 더욱 다채롭게 그리고 자유롭게 사용이 가능하다는 것   
아무래도 클래스의 다형성은 기본적으로 클래스의 상속에 기반을 두기 때문에, 클래스 상속은 한번밖에 안되며 또한 클래스끼리 의미있는 연관 관계가 있어야 되어 여러모로 제약이 많다. 그러나 인터페이스는 언제어디서나 마음대로 implements를 여러개 추가하거나 빼거나 할 수 있으니 제약으로부터 많이 자유로워 짐   
이를 이용한 예시가 바로 다음에 소개할 클래스끼리 형제 관계를 맺게 해주거나 상속을 넘어선 타입 제한도 가능

형제 관계를 맺어줌
기본적으로 자바의 클래스 상속 구조는 부모 - 자식 관계로만 가능하게 되어 있음
만일 여러 자식들끼리 의미있는 관계를 맺고싶다면 또다른 부모를 두어 다시 부모 - 자식 관계를 계층형으로 만들어 주어야 함   
그러나 자바의 클래스 상속 구조는 단일 상속의 원칙을 갖기 때문에, 만일 사용하는 클래스들이 각기 다른 부모 클래스를 상속하고 있는 상황이면 위의 자료형 타입 통합을 할수가 없게 됨   
 
하지만 인터페이스는 클래스 상속 관계와는 달리, 하나의 기능에 대한 약속이기 때문에 어떤 객체이든 간에 그 약속을 지키기만 한다면 필요한 곳에서 사용할 수 있게 한다는 것을 의미    
그리고 인터페이스는 다중 상속에 대해 제약을 받지 않기 때문에, 일부만 묶고 싶은 클래스들을 implements 키워드로 등록시키면, 각기 다른 부모클래스를 상속하고 있는 자식 클래스에 인터페이스를 구현(상속) 시켜줌으로써 형제 클래스 끼리 묶는 타입 통합을 이루어 낼수 있는 것   
즉, 아무 관계도 없는 클래스들에게 하나의 인터페이스를 공통적으로 구현하도록 함으로써 관계를 맺어줄 수 있음

예를 들어 각기 다른 부모 클래스를 상속하고 있는 Soccer 클래스와 BassGuitar 클래스를 하나의 타입으로 묶어서 사용할 필요가 있을때, 인터페이스를 implements 함으로써 마치 Soccer 와 BassGuitar 클래스를 묶은 형제 클래스 타입 IBehavior 를 만든것과 같음   

이렇게 형제 타입을 구성해놓고 아래의 코드와 같이, 인터페이스를 메소드의 매개변수 타입으로 받음으로써 인터페이스에 등록된 추상메소드를 실행하면 실제 구현 클래스의 오버라이딩한 구현 메서드를 실행하게 됨

즉, 자유로운 인터페이스 다형성을 통해 코드 중복을 없애고 간편화를 시켜 설계상 이점을 얻을 수 있게 됨

타입 접근 제한
이외에도 인터페이스는 일종의 접근 제한 역할도 할 수 있음   
이는 위의 형제 관계 역할과 매우 비슷한 개념인데, 만일 똑같은 부모를 상속하고 있는 3개의 자식들중, 2개의 자식 클래스 타입만 받을 수 있는 메서드를 구현한다고 했을때 이용됨   
다형성이랍시고 부모 클래스 타입으로 파라미터를 받아버리면, 모든 자식 클래스가 접근이 가능하지 때문에 제한이 되지 않기 때문  
 
다음과 같이 스타크래프트를 구성하기 위해 Marine, SCV, Tank 클래스를 만들고 이들을 공통으로 묶을 부모 클래스 GroundUnit 클래스로 상속 관계를 맺어줌  
그리고 repair() 메서드에서 중복을 줄이기 위한 다형성 기법으로 매개변수 타입을 GroundUnit 부모 클래스 타입으로 받도록 설정


```java
class GroundUnit { }

class Marine extends GroundUnit{ }
class SCV extends GroundUnit{ }
class Tank extends GroundUnit{ }

public class Main {
    public static void main(String[] args) {   
        repair(new Marine());
    }
    
    static void repair(GroundUnit gu) {
        // 마린은 기계가 아니기 때문에 수리는 불가능 하다. 하지만 상속 관계상 마린 클래스 타입이 들어와 실행될 수 있는 위험성이 존재한다.
    }
}
```

하지만 위의 코드의 문제점은 기본적으로 repair 기능은 기계 유닛만 가능하여 SCV와 Tank 클래스 타입만 들어와야 되는데 생물 유닛인 Marine 클래스 타입도 상속 관계에 의해 들어 올수 있다는 것   
아무리 타이트하게 코딩을 해도 개발자도 결국은 사람이고, 사람은 결국은 실수를 범할 수 있기 때문에 아예 접근하지 못하도록 원천 차단하는 것이 중요  
 
따라서 별도의 Machine 이라는 인터페이스를 선언하고 SCV, Tank 클래스에 implements   
그렇게 3개의 자식중 2개의 자식만 머신 이라는 타입으로 형제 타입 관계를 맺어주면서 동시에 다른 타입의 접근 제한 역할도 해냄   

```java
interface Machine { } // SCV, Tank 클래스를 통합한 타입으로 이용하는 인터페이스

class GroundUnit { }

class Marine extends GroundUnit{ }
class SCV extends GroundUnit implements Machine{ }
class Tank extends GroundUnit implements Machine{ }

public class Main {
    public static void main(String[] args) {
        repair(new Marine()); // ! ERROR
    }

    static void repair(Machine gu) {
        // SVG와 탱크 타입만 받을 수 있게 인터페이스를 타입으로 하여 다형성을 적용
    }
}
```

메서드 접근 제한
이밖에도 객체에서 사용할 수 있는 메서드를 제한 하는 효과도 있는데, 예를들어 A, B, C라는 인터페이스를 구현한 클래스를 반환할 때 A 타입으로 변환하게 되면 외부에서는 A 인터페이스의 메소드만 보이게 됨   
따라서 별도의 접근 제한을 이용하지 않고도 사용할 수 있는 메서드 접근 제한과 마찬가지 효과를 보게 하는 방법  
이런 이유로 오히려 거꾸로 클래스에 여러 가지 메소드를 만들어 둔 다음 인터페이스로 분리하는 작업을 진행하는 경우가 있음

```java
interface PlayMovie {
    void play();
}
interface ViewImage {
    void view();
}
interface VolumeUpDown {
    void volume();
}

class MP3 implements PlayMovie, ViewImage, VolumeUpDown {
    public void play() {}
    public void view() {}
    public void volume() {}
}

public class Main {
    public static void main(String[] args) {
        PlayMovie mp3 = new MP3(); // 3개의 구현한 인터페이스중 하나로 객체 선언
        mp3.play(); // play() 이외의 메소드는 제한된다.
    }
}
```

의존성을 제거 (decoupling)
의존성이란 객체 지향 설계에 아주 중요한 개념으로 객체가 어떻게 소통하는지 나타내는 것   
만일 코드 설계를 구체 클래스로 하게 되면 객체간의 강한 의존성이 생기게 되어 만일 코드 변경이 필요하게 되면 이것저것 여러가지 변경이 필요해질 수 도 있다. 따라서 클래스 간의 관계를 구성할때 그 관계를 느슨하게 하는 것이 중요   
그래서 클래스의 관계를 상속(extends)가 아닌 구현(implements)으로 인터페이스로 확장시킨다면, 반환 타입이나 매개변수 타입으로 다른 객체와 소통하는 구간에 인터페이스 타입으로 사용함으로써, 객체간 의존성이 줄어들어 자신과 소통하는 객체의 변화에 강한 클래스를 만들 수 있게 됨  


이런 의존성은 과거부터 있었던 많은 Framework에서 발전해 MVC, MVVM 패턴등으로도 승화 되었고 depedecny injection등의 기술로도 사용됨

인터페이스 타입으로 통신
ServiceLogic 클래스의 메소드 printInt() 를 보면 파라미터로 MapStore 클래스 타입을 받아 MapStore 클래스의 메서드를 실행해 값을 얻고 출력하는 로직으로 구성됨
이러한 형태를 ServiceLogic 클래스는 MapStore 클래스에 의존적이다 라고 말함  
왜냐하면 MapStore 클래스가 잘못되면 ServiceLogic 클래스의 메서드는 동작하지 않을 것이기 때문  

```java
class ServiceLogic {
    // ServiceLogic 클래스의 메소드는 MapStore 클래스를 사용하기 때문에, ServiceLogic 는 MapStore 에 의존적이다.
    public void printInt(MapStore cls) { // 지정한 클래스 타입만 받음
        int num = cls.getNum() * 2;
        System.out.println(num);
    }
}

class MapStore {
    private int num = 10;

    public int getNum() {
        return this.num;
    }
}
```

따라서 이러한 의존성 관계를 없애기 위해 ClubStore 인터페이스를 만들고 MapStore 클래스에 implements 하여 구현함   
그러면 ServiceLogic 클래스에서 만일 MapStore 객체 데이터를 사용할 일이 생길경우, 직접 MapStore 객체를 사용하는게 아닌 오로지 ClubStore 인터페이스를 이용해 통신함으로써 클래스 간의 의존성을 없앨 수 있는 것   
이것을 변경에 유리한 유연한 설계라함

```java
interface ClubStore {
    int getNum(); // 인터페이스 타입 상태의 객체에서 메서드를 사용하기 위해선 인터페이스에도 추상 메서드 형태로 넣어져 이썽야 한다.
}

class ServiceLogic {
    // ServiceLogic 클래스의 메소드는 ClubStore 인터페이스를 사용함으로써 클래스 간의 의존성을 없앴다.
    public void printInt(ClubStore cls) { 
        int num = cls.getNum() * 2;
        System.out.println(num);
    }
}

class MapStore implements ClubStore{
    private int num = 10;

    public int getNum() {
        return this.num;
    }
}
```

표준화
 
개발 시간을 단축
인터페이스를 사용하면 클래스의 선언과 구현을 분리시킬 수 있기 때문에 실제 구현에 독립적인 프로그램을 작성하는 것이 가능   
예를 들어 기존의 클래스와 클래스 간의 직접적인 관계를, 인터페이스를 이용해서 간접적인 관계로 변경하면, 한 클래스의 변경이 관련된 다른 클래스에 영향을 미치지 않는 독립적인 프로그래밍이 가능  
따라서 메서드를 호출하는 쪽에서는 선언 부만 알면 되기 때문에 인터페이스만 가지고도 프로그램을 작성할 수 있으며, 동시에 다른 한쪽에서는 인터페이스를 구현하는 클래스를 작성하면 인터페이스의 구현을 기다리지 않고 작업이 가능  
즉, A가 B클래스의 구성 완성을 기다리지 않고, 설계도인 인터페이스를 보고 동시에 개발을 함으로써 결과적으로 개발 시간을 단축 시킬 수 있는 것

사실 이는 추상 클래스 특징과 겹치는 부분기이도 한데, 인터페이스도 결국 추상화 클래스의 일종이기 때문에 가능한 것
 
나중에 변경이 용이함
또한 프로젝트에 사용되는 기본 틀을 인터페이스로 작성한 다음 개발자들에게 인터페이스를 구현하여 프로그램을 짜도록 하면 보다 일관되고 정형화된 프로그램의 개발이 가능   
자바의 데이터베이스 인터페이스인 JDBC가 대표적인데, 이 추상화된 인터페이스 규칙에 따라 다양한 종류의 데이터베이스를 사용하더라도 인터페이스 구현만 잘하면 동일하게 접속할 수 있는 이유   

예를들어 어느 자바 어플리케이션이 있고 데이터베이스를 MySQL을 사용하고 있었는데, 만일 데이터베이스를 MySQL에서 Oracle로 변경한다고 한다고 가정
본래라면 자바 어플리케이션의 DB 커넥션 코드를 변경해야 되는데, 이를 자바에서는 JDBC 라는 인터페이스 그룹을 통해 데이터베이스와 관계 중개를 통해 통신   
그래서 자바 어플리케이션 입장에선 데이터베이스 종류는 모르고 오로지 인터페이스 기준으로 만을 데이터를 읽고 쓰고 작업을 함  
그리고 각각의 데이터베이스 제조 밴더사들은 위의 인터페이스를 구현한 구현 클래스들을 따로 만들어 자바 언어와 잘 연결되게 지원   
따라서 MySQL을 쓰다가 Oracle을 쓴다고 한다면, 기존에 쓰고 있는 오라클에서 제공하는 클래스 라이브러리들을 MySQL 클래스 라이브러리 파일로 바꾸고 약간 설정만 해주면 복잡한 수정 없이 변경이 완료됨   
만일 인터페이스라는 관계 중개 가 없다면 하드 코딩한 것을 통째로 바꿔야 할지도 모름  
이것이 자바 데이터베이스 인터페이스라는 '표준화' 가 있기 때문에 가능  

마커 인터페이스
자바의 마커 인터페이스는 일반적인 인터페이스와 동일하지만 사실상 아무 메소드도 선언하지 않은 빈 껍데기 인터페이스를 말함
예를 들면 아래와 같음


```java
interface XXXable{ // 아무런 내부 내용이 없는 빈 껍데기 인터페이스
}
```

얼핏 보기엔 인터페이스의 존재 원리와 반하는 형태   
다만 인터페이스를 자유롭게 다중 상속이 가능하다는 점에서 착안하여 이러한 형태로도 사용이 가능한 것   
아무 내용도 없어서 쓸모가 없어 보이지만, 마커 인터페이스의 역할은 객체의 타입과 관련된 정보만을 제공해주는 것   
따라서 컴파일러와 JVM은 이 마커 인터페이스를 통해 객체에 대한 추가적인 정보를 얻을 수 있음
 
상위 클래스 Animal을 만들고 그 하위들로 Lion, Chicken, Snake ...등 여러가지 동물 클래스들을 만들어 상속 관계를 맺음   
이때 born 이라는 메서드에서 Animal 타입의 매개변수를 받고 새끼를 낳는 동물인지 알을 낳는 동물인지 구분하기 위해 일일히 instanceof 연산자로 클래스 타입을 구분

```java
class Animal {
    public static void born(Animal a) {
        if(a instanceof Lion) {
            System.out.println("새끼를 낳았습니다.");
        } else if(a instanceof Chicken) {
            System.out.println("알을 낳았습니다.");
        } else if(a instanceof Snake) {
            System.out.println("알을 낳았습니다.");
        }
        // ...
    }
}

class Lion extends Animal { }
class Chicken extends Animal { }
class Snake extends Animal { }
```

하지만 이러한 방식은 자식 클래스 갯수가 많으면 많을 수록 코드가 난잡해지고 길어진다는 단점이 있음   
따라서 아무런 내용이 없는 빈 껍데기 인터페이스를 선언하고 적절한 클래스에 implements 시킴으로써, 추상화, 다형성 이런걸 떠나서 그냥 단순한 타입 체크용으로 사용하는 것   
그러면 조건문 코드도 다음과 같이 심플해질 수 있음

```java
// 새끼를 낮을 수 있다는 표식 역할을 해주는 마커 인터페이스
interface Breedable {}

class Animal {
    public static void born(Animal a) {
        if(a instanceof Breedable) {
            System.out.println("새끼를 낳았습니다.");
        } else {
            System.out.println("알을 낳았습니다.");
        }
    }
}

class Lion extends Animal implements Breedable { }
class Chicken extends Animal { }
class Snake extends Animal { }
```

### Reference

[Jun_BE.log](https://velog.io/@rlafbf222/JAVA-%EA%B8%B0%EC%B4%88-%EB%AC%B8%EB%B2%95-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC)  
[sunnamgung8.log : [자바]List(컬렉션)](https://velog.io/@sunnamgung8/%EC%9E%90%EB%B0%94List%EC%BB%AC%EB%A0%89%EC%85%98)  
[HyunHa.log : [JAVA] 패키지(Package) 정리](https://velog.io/@hyun_ha/JAVA-%ED%8C%A8%ED%82%A4%EC%A7%80Package)  
[sangwon.log : [JAVA] OOP란?](https://velog.io/@vincentj2/JAVA-OOP%EB%9E%80)  
[Inpa Dev 👨‍💻:티스토리](https://inpa.tistory.com/entry/JAVA-☕-toString-메서드-재정의-완벽-이해하기)  
[Steady : java. super와 super() 완벽하게 이해하기](https://velog.io/@rhdmstj17/java.-super%EC%99%80-super-%EC%99%84%EB%B2%BD%ED%95%98%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0)
