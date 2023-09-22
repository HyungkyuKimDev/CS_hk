# 모던 PHP

---

## 의존성 라이브러리 관리자 컴포저

현대의 개발은 대부분 모든 걸 직접 만드는 것이 아니라 타인이 만들어놓은 라이브러리를 가져다 쓰면서 작업하게 된다. 이를 수월하게 만들어주는 의존성 라이브러리 관리자인 컴포저를 사용해본다.

컴포저는 php에서 사용하는 의존성 관리 라이브러리이다. 필요한 라이브러리와 버전을 기술해 놓으면 명시한 라이브러리 뿐만 아니라 라이브러리가 필요로하는 다른 라이브러리까지 찾아서 한번에 설치해 준다.


```
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === 'e21205b207c3ff031906575712edab6f13eb0b361f2085f1f1237b7126d785e826a450292b6cfd1d64d92e6563bbde02') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"
```

