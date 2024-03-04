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
[9. String Method](#9-string-method)
[10. wrapper class](#10-wrapper-class)
[11. list](#11-list)
[12. OOP](#12-oopobject-oriented-programming)

### 1. 자료형

- Java의 자료형은 크게 Primitive type(기본자료형)과 Reference type(참조자료형)으로 구분된다.

- primitive type의 종류:

  - short, int, long, float, double, char, boolean, byte 등이 있다.
  - short, int, long은 숫자형으로 각각 나타낼 수 있는 숫자의 크기가 다르며, 이는 각 타입에 할당되는 메모리의 크기가 다르기 때문이다.
  - 순서대로 각 2바이트, 4바이트, 8바이트가 할당 가능하다.
  - 또한 아래의 코드로 최소 및 최대값을 찍어보며 실제 값을 볼 수 있다.

    > System.out.println(Short.MAX_VALUE);  
    >  System.out.println(Short.MIN_VALUE);

- reference type(=Non-primitive)의 종류:
  - 참조 자료형은 위의 기본 자료형을 제외한 모든 자료형을 말한다.
  - 쉽게 말해 자바의 인스턴스를 가리킬 수 있는 자료형이다.
  - Strings, Arrays, Classes, Interface 등이 존재한다.
  - null이 될 수 있다.

- Type Casting
  - Primitive type value를 다른 type으로 변경함을 말한다.
  - Widening casting(Automatically) : 자동으로 변경 가능
    - byte -> short -> char -> int -> long -> float -> double
    ```java
    int myInt = 9;
    double myDouble = myInt; // Automatic casting: int to double
    ```
  - Narrowing Casting(Manually) : 앞에 변경할 타입을 괄호쳐서 처리해줘야 함 
    - double -> float -> long -> int -> char -> short -> byte
    ```java
    double myDouble = 9.78d;
    int myInt = (int) myDouble; // Manual casting: double to int
    ```

  - Strings
    - String Methods
      - toUpperCase() => make all letters in a sentence as Capital letter 
      - toLowerCase() => make all letters in a sentence as lowercase

      ```java
      System.out.println(txt.toUpperCase());   // Outputs "HELLO WORLD"
      System.out.println(txt.toLowerCase());   // Outputs "hello world"
      ```

      - indexOf() => find an letter in a sentence and return that index of the senetence
      ```java
      String txt = "Please locate where 'locate' occurs!";
      System.out.println(txt.indexOf("locate")); // Outputs 7
      ```

      - concat() => concatenate two strings
      ```java
      String firstName = "John ";
      String lastName = "Doe";
      System.out.println(firstName.concat(lastName));
      ```
  - Math Class
    - Math.max(x,y) => find the highest value of x and y
    ```java
    Math.max(5, 10);
    ```
    - Math.min(x,y) => find the lowest value of x and y
    ```java
    Math.min(5, 10);
    ```
    - Math.sqrt(x) => return the square root of x
    ```java
    Math.sqrt(64);
    ```
    - Math.abs(x) => method returns the absolute (positive) value of x
    ```java
    Math.abs(-4.7);
    ```
    - Math.random() => returns a random number between 0.0 (inclusive), and 1.0
    ```java
    int randomNum = (int)(Math.random() * 101);  // 0 to 100
    ```
  
  - Shift Operator
    - << : Signed Left Shift
      - The left shift operator moves all bits by a given number of bits to the left.
      ```java
      int number = 2; // 0010
      int Ans = number << 2; // 1000 => 8
      ```
    - >> : Signed Right Shift
      - The right shift operator moves all bits by a given number of bits to the right.
      ```java
      int number = 8; // 1000
      int Ans = number >> 2; // 0010 => 2
      ```
    - >>> : Unsigned Right Shift
      - the vacant leftmost position is filled with 0 instead of the sign bit.
      ```java
      byte num1 = 8; // 0000 1000
      byte num2 = -8; // 1111 1000
      
      System.out.println(num1 >>> 2); // 0000 0010   
      System.out.println(num2 >>> 2); // 0011 1110
      ```

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
  실행 가능한 메소드의 경우 함수라고도 한다.  
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

- 메소드 오버로딩(Method Overloading)
  - With method overloading, multiple methods can have the same name with different parameters
  ```java
  static int plusMethod(int x, int y) {
    return x + y;
  }

  static double plusMethod(double x, double y) {
    return x + y;
  }

  public static void main(String[] args) {
    int myNum1 = plusMethod(8, 5);
    double myNum2 = plusMethod(4.3, 6.26);
    System.out.println("int: " + myNum1);
    System.out.println("double: " + myNum2);
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

### 9. String Method

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

### 10. wrapper class

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

### 11. list

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

### 12. OOP(Object Oriented Programming)

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

- Code로 설명
  - 1. class를 만든다.
    ```java
    // Main.java
    public class Main {
      int x = 5;
    }
    ```
  - 2. 해당 class의 object를 그 class의 이름에 'new' 키워드를 사용해 만든다.
    ```java
    class Second {
      public static void main(String[] args) {
        Main myObj = new Main(); // Main class, new 키워드 사용
        System.out.println(myObj.x);
      }
    }
    ```

- Class Method
  ```java
  public class Main {
  static void myMethod() {
    System.out.println("Hello World!");
  }

  public static void main(String[] args) {
    myMethod();
  }
  }

  // Outputs "Hello World!"
  ```
  - static vs public
    - Method를 static으로 만들 경우, public과 달리 해당 class의 object 선언 없이 Method 사용이 가능하다.
    ```java
    public class Main {
    // Static method
    static void myStaticMethod() {
      System.out.println("Static methods can be called without creating objects");
    }

    // Public method
    public void myPublicMethod() {
      System.out.println("Public methods must be called by creating objects");
    }

    // Main method
    public static void main(String[] args) {
      myStaticMethod(); // Call the static method
      // myPublicMethod(); This would compile an error

      Main myObj = new Main(); // Create an object of Main
      myObj.myPublicMethod(); // Call the public method on the object
    }
    }
    ```

- Java Modifiers （제어자)
  - classes, attributes, methods 와 constructors를 접근하는 레벨을 나누기 위해 사용
  - 1. Access Modifiers (접근 수정자) - 접근 레벨을 제어
  - 2. Non-Access Modifiers (비접근 수정자) - 접근 레벨을 제어하지 않으나, 다른 기능을 제공

|Access Modifiers | |
|:---   |:---        |
|For Class| |
|Modifier | Description|
|public|	다른 모든 class 접근 가능|
|default|	같은 package 내에 class에 접근 가능. 제어자를 설정하지 않을때 사용.|  
|For attributes, methods and constructors| |
|public|	모든 class 접근 가능|
|private|	선언된 class 내에서만 사용 가능|
|default|	같은 package 내에 class에 접근 가능. 제어자를 설정하지 않을때 사용.|
|protected|	같은 package 내에 또는 서브(자식)클래스내에서만 접근 가능.|

|Non-Access Class | |
|:---   |:---        |
| For Class | |
| Modifiers | Description |
| final | 다른 클래스에서 상속할 수 없는 클래스. |
| abstract | 클래스를 객체로 생성할 수 없음. (추상 클래스에 접근하려면 다른 클래스에서 상속해야 함.) |
| For attributes, methods and constructors | |
| final | 속성 및 메서드를 재정의/수정할 수 없음. |
| static | 속성 및 메서드는 객체가 아닌 클래스에 속함. |
| abstract | 추상 클래스에서만 사용할 수 있으며, 메서드에만 사용된다. 메서드에는 본문이 없으며, 예를 들어 `abstract void run();`. 본문은 하위 클래스에서 제공 (상속됨). |
| transient | 객체를 직렬화할 때 속성 및 메서드가 건너뜀 |
| synchronized | 메서드는 한 번에 하나의 스레드만 액세스 가능 |
| volatile | 속성의 값이 스레드별로 캐시되지 않으며 항상 "메인 메모리"에서 읽힘 |

Reference : [w3School](https://www.w3schools.com/java/java_modifiers.asp)
<br></br>

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
    1. getter - private으로 설정된 값을 가져감(사용자가 접근 불가능)
    2. setter - private으로 설정된 값을 변경함(사용자가 수정)

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

    ```java
    class Vehicle {
      protected String brand = "Ford";        // Vehicle attribute
      public void honk() {                    // Vehicle method
        System.out.println("Tuut, tuut!");
      }
    }
    
    class Car extends Vehicle {
      private String modelName = "Mustang";    // Car attribute
      public static void main(String[] args) {
      
        // Create a myCar object
        Car myCar = new Car();
    
        // Call the honk() method (from the Vehicle class) on the myCar object
        myCar.honk();
    
        // Display the value of the brand attribute (from the Vehicle class) and the value of the modelName from the Car class
        System.out.println(myCar.brand + " " + myCar.modelName);
      }
    }
    ```

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

##### Access Attributes
- class의 object로 생성된 attributes에 접근하기 위해서는 . 을 이용한다.
```java
public class Main {
  int x = 10;

  public static void main(String[] args) {
    Main myObj = new Main();
    myObj.x = 25; // x is now 25
    System.out.println(myObj.x);
  }
}
```

- final로 선언하면, overriding을 막을 수 있다.
```java
public class Main {
  final int x = 10;

  public static void main(String[] args) {
    Main myObj = new Main();
    myObj.x = 25; // will generate an error: cannot assign a value to a final variable
    System.out.println(myObj.x);
  }
}
```

- 여러 Attributes의 경우
```java
public class Main {
  String fname = "John";
  String lname = "Doe";
  int age = 24;

  public static void main(String[] args) {
    Main myObj = new Main();
    System.out.println("Name: " + myObj.fname + " " + myObj.lname);
    System.out.println("Age: " + myObj.age);
  }
}
```

##### package

Tip : Java에서 사용하는 하나의 Folder라고 생각하면 편함

- 종류
  - Built-in Packages (packages from the Java API)
  - User-defined Packages (create your own packages)

- Built-in Packages (packages from the Java API)
선언 :  
`java package 패키지명;`

도메인 이름 역순 + 마지막에 프로젝트 이름을 붙여준다.

```java
ex)
import package.name.Class;   // Import a single class
import package.name.*;   // Import the whole package

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

- User-defined Packages (create your own packages)

package 제작을 위해서는 package 키워드를 사용한다.
```java
package mypack;
class MyPackageClass {
  public static void main(String[] args) {
    System.out.println("This is my package!");
  }
}
```

제작한 뒤에는 저장하고 compile하는 과정을 거친다.
```java
C:\Users\Your Name>javac MyPackageClass.java
C:\Users\Your Name>javac -d . MyPackageClass.java // -d는 compile 위치를 지정한다. .은 현재 디렉터리를 의미 
``` 

해당 패키지 실행
```java
C:\Users\Your Name>java mypack.MyPackageClass
```

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

### Reference

[Jun_BE.log](https://velog.io/@rlafbf222/JAVA-%EA%B8%B0%EC%B4%88-%EB%AC%B8%EB%B2%95-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC)  
[sunnamgung8.log : [자바]List(컬렉션)](https://velog.io/@sunnamgung8/%EC%9E%90%EB%B0%94List%EC%BB%AC%EB%A0%89%EC%85%98)  
[HyunHa.log : [JAVA] 패키지(Package) 정리](https://velog.io/@hyun_ha/JAVA-%ED%8C%A8%ED%82%A4%EC%A7%80Package)  
[sangwon.log : [JAVA] OOP란?](https://velog.io/@vincentj2/JAVA-OOP%EB%9E%80)  
[Inpa Dev 👨‍💻:티스토리](https://inpa.tistory.com/entry/JAVA-☕-toString-메서드-재정의-완벽-이해하기)  
[Steady : java. super와 super() 완벽하게 이해하기](https://velog.io/@rhdmstj17/java.-super%EC%99%80-super-%EC%99%84%EB%B2%BD%ED%95%98%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0)
[W3 School](https://www.w3schools.com/java)