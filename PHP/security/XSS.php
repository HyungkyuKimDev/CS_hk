<?php

/*

XSS, Cross Site Scripting

게시판 등에 javascript 등의 스크립트 코드를 넣어, 개발자가 고려하지 않은 기능을 작동시켜.
사용자를 공격하는 해킹 방식이다.

XSS에는 세 가지가 있고.

각각 Reflected XSS / Stored XSS / DOM Based XSS 가 있다.

Reflected XSS의 경우.

예를 들어 데이터를 입력 받는 부분에. <script><alert>"error"</alert></script> 를 삽입하게 되면.
해당 자바스크립트가 작동하게 된다.

이처럼 XSS 공격에 취약한 사이트를 찾아. 공격한 뒤, 해당 URL를 다른 사용자에게 노출시키고.
데이터를 취득하는 등의 방식을 사용한다.

==> 방지 방법

htmlspecialchars($변수)

이러면, 변수 문자열에 & " ' < > 가 포함되어있어도. 스크립트로 인식하지 않고 단순 문자열로 인식하게 된다.

Ex)

& (ampersand) becomes &amp;
" (double quote) becomes &quot;
' (single quote) becomes &#039;
< (less than) becomes &lt;
> (greater than) becomes &gt;

====> 스크립트를 문자열로 만듦으로써 의도적인 기능 작동 방지를 통해 해결.
*/
