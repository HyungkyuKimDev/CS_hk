## 출처 : ihoneymon 마크다운 글

- 해당 링크 : [ihoneymon](https://gist.github.com/ihoneymon/652be052a0727ad59601)

---

# 1. 마크다운

## 1.1. Outline

Markdown은 텍스트 기반의 마크업 언어이며, HTML로 변환이 가능하다. 주로 Github 내에서 설치방법, 소스코드 설명, 이슈을 가독성 높게 작성할 수 있다는 강점이 있다.

## 1.2. Markdown's pros and cons

### 1.2.1. 장점

    1. 다양한 형태로 변환이 가능하다.
    2. 텍스트(Text)로 저장되기 때문에 용량이 적어 보관이 용이하다.
    3. 텍스트파일이기 때문에 버전관리시스템을 이용하여 변경이력을 관리할 수 있다.
    4. 지원하는 프로그램과 플랫폼이 다양하다.

### 1.2.2. 단점

    1. 표준이 없다.
    2. 표준이 없기 때문에 도구에 따라서 변환방식이나 생성물이 다르다.
    3. 모든 HTML 마크업을 대신하지 못한다.

---

# 2. 마크다운 사용법(문법)

## 2.1. 헤더 Headers

- 큰제목: 문서 제목

  ```
  # {Text}
  ```

  # {Title}

- 작은제목: 문서 부제목

  ```
  {Text}
  ```

  Text

  ***

- 글자 크기는 # 개수로 1 ~ 6 까지 표현 가능, 1이 가장 큼

```
# 크기순 1 (자동으로 문단 나눠짐)
## 크기순 2
### 크기순 3
#### 크기순 4
##### 크기순 5
###### 크기순 6
```

# 크기순 1

## 크기순 2

### 크기순 3

#### 크기순 4

##### 크기순 5

###### 크기순 6

## 2.2. BlockQuote

하위 블럭 단위는 `>` 블럭인용문자를 이용한다.

```
> This is a first blockqute.
>	> This is a second blockqute.
>	>	> This is a third blockqute.
```

> This is a first blockqute. > This is a second blockqute. > > This is a third blockqute.

> ### This is a H3
>
> - List
>
> ```
> code
> ```

## 2.3. 목록

### ● 순서있는 목록(번호)

순서있는 목록은 숫자와 점을 사용한다.

```
1. 첫번째
2. 두번째
3. 세번째
```

1. 첫번째
2. 두번째
3. 세번째

**순서를 잘 못 적더라도 순서가 맞게 수정됨**

```
1. 첫번째
3. 세번째
2. 두번째
```

1. 첫번째
2. 세번째
3. 두번째

### ● 순서없는 목록(글머리 기호: `*`, `+`, `-` 지원 => 혼합되어도 상관 없음)

```
* 빨강
  * 녹색
    * 파랑
```

- 빨강
  - 녹색
    - 파랑

## 2.4. 코드

4개의 공백 또는 하나의 탭으로 들여쓰기 사용시, 코드 블럭으로 변환됨.

### 2.4.1. 들여쓰기

```
This is a normal paragraph:

    This is a code block.

end code block.
```

## 실제 출력시

---

This is a normal paragraph:

    This is a code block.

end code block.

---

### 2.4.1. 코드블럭

코드블럭은 다음과 같이 2가지 방식을 사용할 수 있습니다:

1. `<pre><code>{code}</code></pre>` 이용방식

```
<pre>
<code>
print("Hello, World!")
</code>
</pre>
```

<pre>
<code>
print("Hello, World!")
</code>
</pre>

2. 코드블럭코드("\```") 을 이용하는 방법

<pre>
<code>
```
print("Hello, World!")
```
</code>
</pre>

```
print("Hello, World!")
```

코드블럭코드("\```") 시작점에 사용되는 언어를 작성해 [문법강조(Syntax highlighting)](https://docs.github.com/en/github/writing-on-github/creating-and-highlighting-code-blocks#syntax-highlighting)이 가능하다.

<pre>
<code>
```python
print("Hello, World!")
```
</code>
</pre>

```python
print("Hello, World!")
```

## 2.5. 수평선 `<hr/>`

아래 줄은 모두 수평선을 만든다. 마크다운 문서를 미리보기로 출력할 때 _페이지 나누기_ 용도로 많이 사용한다.

```
* * *

***

*****

- - -

---------------------------------------
```

- 적용예

---

## 2.6. 링크

- 참조링크

```
[link keyword][id]

[id]: URL "Optional Title here"

// code
Link: [Google][googlelink]

[googlelink]: https://google.com "Go google"
```

Link: [Google][googlelink]

[googlelink]: https://google.com "Go google"

- 외부링크

```
사용문법: [Title](link)
적용예: [Google](https://google.com, "google link")
```

Link: [Google](https://google.com, "google link")

- 자동연결

```
일반적인 URL 혹은 이메일주소인 경우 적절한 형식으로 링크를 형성한다.

* 외부링크: <http://example.com/>
* 이메일링크: <address@example.com>
```

- 외부링크: <http://example.com/>
- 이메일링크: <address@example.com>

## 2.7. 강조

```
*single asterisks*
_single underscores_
**double asterisks**
__double underscores__
~~cancelline~~
```

- _single asterisks_
- _single underscores_
- **double asterisks**
- **double underscores**
- ~~삭제~~

> `문장 중간에 사용할 경우에는 **띄어쓰기** 를 사용하는 것이 좋다.`  
> 문장 중간에 사용할 경우에는 띄어쓰기를 사용하는 것이 좋다.

## 2.8. 이미지

```
![Alt text](/path/to/img.jpg)
![Alt text](/path/to/img.jpg "Optional title")
```

![석촌호수 러버덕](http://cfile6.uf.tistory.com/image/2426E646543C9B4532C7B0)
![석촌호수 러버덕](http://cfile6.uf.tistory.com/image/2426E646543C9B4532C7B0 "RubberDuck")

사이즈 조절 기능은 없기 때문에 `<img width="" height=""></img>`를 이용한다.

예

```
<img src="/path/to/img.jpg" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
<img src="/path/to/img.jpg" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>
```

<img src="http://cfile6.uf.tistory.com/image/2426E646543C9B4532C7B0" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
<img src="http://cfile6.uf.tistory.com/image/2426E646543C9B4532C7B0" width="40%" height="30%" title="%(비율) 크기 설정" alt="RubberDuck"></img>

## 2.9. 줄바꿈

3칸 이상 띄어쓰기(` `)를 하면 줄이 바뀐다.

```
* 줄 바꿈을 하기 위해서는 문장 마지막에서 3칸이상을 띄어쓰기해야 한다.
이렇게
```

- 줄 바꿈을 하기 위해서는 문장 마지막에서 3칸이상을 띄어쓰기해야 한다. 이렇게

---

## Reference

- [78 Tools for writing and previewing Markdown](http://mashable.com/2013/06/24/markdown-tools/)
- [John gruber 마크다운 번역](http://nolboo.github.io/blog/2013/09/07/john-gruber-markdown/)
- [깃허브 취향의 마크다운 번역](http://nolboo.github.io/blog/2014/03/25/github-flavored-markdown/)
- [허니몬의 마크다운 작성법](http://www.slideshare.net/ihoneymon/ss-40575068)
- Document : [markdownguide](https://www.markdownguide.org/getting-started/)
