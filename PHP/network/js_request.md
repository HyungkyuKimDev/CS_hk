# 参考：https://www.udemy.com/course/web-app-development/

# JS에서 요청 전송해서 ・PHP로 응답하기
JS를 이용해 서버에 요청 가능하다.

## 전송 데이터 생성
HTML에서 `<form>` 나 `<input>`을 이용해서 POST 메소드로 데이터 지정이 가능하다.  


```js
const formData = new FormData();

formData.append('id', questionId);
formData.append('selectedAnswer', selectedAnswer);
```

## 요청 실행
요청을 보내기 위해서 `XMLHttpRequest`를 사용한다.   
아래와 같이 작성해 JS에 요청이 전송된다.

```js
const xhr = new XMLHttpRequest();

xhr.open('POST', 'answer.php');

xhr.send(formData);
```

## PHP측에서 JavaScript에 대한 응답 만들기
JavaScript에서 요청이 도착하면 PHP에서는 요청 정보를 받고 처리한다.  
그런 다음 응답을 반환하면, JS에서 HTML를 그대로 반환해도 처리할 수 없다.   
JavaScript의 경우. JSON(JavaScript Object Notation)를 이용해 객체로써 활용해서 처리한다.

PHP에선 배열 또는 연관 배열을 JSON으로 변환하는 함수, json_encode를 사용해서 JSON을 만들 수 있다.

```php
$response = [
    'result' => true,
    'correctAnswer' => 'A',
    'correctAnswerValue' => '1万円',
    'explanation' => '渋沢栄一の1人のファンとして考えると、新しい日本銀行券（一万円札）が新たなファングッズの一つになります（？）',
];

echo json_encode($response);
```

## 응답 받기
PHP로 부터 응답을 받은 뒤, 응답 내용에 따라 처리한다.

응답의 HTTP status code를 보고 통신 성공 여부를 확인한다.   
다음 PHP에서 전달한 JSON 내용을 바탕으로 JS 처리를 구현한다.

```js
// loadend는 요청 완료 되었을 때, 이벤트 발생
xhr.addEventListener('loadend', receivedResponse);

function receivedResponse(event) {
    // addEventListener를 통해 XML 객체를 가져온다.
    const xhr = event.currentTarget;

    // http status code 확인
    if (xhr.status === 200) {
        // 성공

        // 서버로부터 응답이 JSON이면 JSON.parse에서 JS 객체로 변환한다.
        const response = JSON.parse(xhr.response);

        // response 내용에 따른 처리
    } else {
        // 에러
    }
}
```