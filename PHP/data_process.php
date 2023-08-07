<?php

/* 

클라이언트 송신 데이터 처리

クライアントとは、例えばHTMLを表示しているブラウザなどを指します。
HTMLの中に`<form>`、`<input>`などを組み込むと、利用者がデータを入力をするためのフォームが表示されます。  
値を入力した後に、送信するボタンを押すことでサーバーへデータが送信されます。

클라이언트는 예를 들어, HTML를 표시하는 브라우저를 가리킨다.
HTML 안에는 <form> <input> 등에, 사용자가 정보를 넣고 송신을 버튼을 누르면 서버로 정보가 이동된다.

EX)

```
  クライアント       リクエスト           サーバー
+-------------+   (入力データ込)    +------------+
|    HTML     | ----------------> |    PHP     | 
|   <form>    |                   |   $_GET    |
|    <input>  |                   |   $_POST   |
|   </form>   | <---------------- |            |
+-------------+     レスポンス      +------------+

처리 방법 

1. GET: URL에 파라미터 값을 붙여서 송신

? 뒤에 값이 파라미터 값이다. 이처럼 파라미터 값을 URL에 붙여서 송신하게되면
서버는 요청된 내용의 필요한 정보를 클라이언트에게 제공한다.

EX)
http://localhost:8080/question.php?id=2&value=test

PHP가 URL 파라미터 값을 참조하는 방법

echo $_GET['id']; // id=2の値「2」が出力される
echo $_GET['value']; // value=testの値「test」が出力される

2. POST: Request의 Body에 두고 송신

HTML의 <form> <input>를 이용, 서버에 데이터를 보낼 수 있다.
POST 라고 하는 HTTP 메소드를 이용해 데이터를 보내는 경우 이처럼 된다.

EX)
<form method="POST" action="answer.php">
    <p>ID: <br><input name="id" type="text" value="1"></p>
    <p>選んだ答え: <br><input name="selectedAnswer" type="text" value="C"></p>
    <p><input type="submit" value="送信"></p>
</form>

```

위의 예에 ex: answer.php 에 id 또는 selectedAnswer에 값을 보낼 수 있다.
PHP (ex: answer.php)에서 이 정보를 참조하기 위해서 아래와 같이 기술한다.

echo $_POST['id'];             // 「1」が出力される
echo $_POST['selectedAnswer']; // 「C」が出力される

----

GET / POST HTTP Request Example

1. localhost:8080가 요청을 받을 수 있도록 설정

php -S localhost:8080

2. nc 명령어 사용, 요청 실행

3-1. GET HTTP 요청을 수동으로 실행

nc localhost 8080 < requestHttpGet.txt

==> Result

$ nc localhost 8080 < requestHttpGet.txt
HTTP/1.1 200 OK
Host: localhost:8080
Date: Tue, 04 May 2021 00:27:10 GMT
Connection: close
X-Powered-By: PHP/7.3.24-(to be removed in future macOS)
Content-type: text/html; charset=UTF-8

<!DOCTYPE html>
<html lang="ja">
<head>
...以下省略

3-2. POST HTTP 요청을 수동으로 실행

nc localhost 8080 < requestHttpPost.txt

==> Result

$ nc localhost 8080 < requestHttpPost.txt
HTTP/1.1 200 OK
Host: localhost:8080
Date: Tue, 04 May 2021 00:24:48 GMT
Connection: close
X-Powered-By: PHP/7.3.24-(to be removed in future macOS)
Content-type: text/html; charset=UTF-8

{"result":false,"correctAnswer":"B","correctAnswerValue":"HyperTextMarkupLanguage","explanation":"\u3053\u308c\u304c\u9593\u9055\u3048\u3066\u305f\u3089\u300cHTML\u3068\u306f\uff1f\u300d\u306e\u52d5\u753b\u3092\u5fa9\u7fd2\u304a\u9858\u3044\u3057\u307e\u3059\uff01"}% 


*?