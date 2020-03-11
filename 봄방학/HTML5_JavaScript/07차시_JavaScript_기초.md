# JavaScript 기초

## JavaScript 기능

- HTML & CSS
    - 웹 문서의 구조와 외형 정의
    - 문법이 서로 다름
- JavaScript
    - 웹 문서의 기능 정의

## JavaScript의 특징

### 1. 스크립트 언어이다.
- 스크립트 언어와 컴파일 언어
    - 스크립트 언어 : 인터프리터로 실행, 속도 느림, 실행환경 제한
    - 컴파일 언어 : 컴파일 후 실행,   데이터 타입, 형변환 엄격
- 텍스트 에디터 + 웹 브라우저로 프로그래밍 가능
- 데이터 타입 수월해 쉽게 학습 가능
- 코드 테스트가 수월

### 2. 함수형 언어이다.
- 함수를 기본으로 하는 방식
- 선언적 프로그래밍 : HTML요소 동적 처리 가능
- 1급 함수 : 함수 자체를 데이터처럼 사용 가능
- 변수의 유효 범위 == 함수의 유효범위

### 3. Java와는 전혀 다른 프로그래밍 언어이다.
- 네스케이프 사에서 마케팅 목적으로 라이센스 받아 사용
- JavaScript = ECMA-262

### 4. 초보적인 언어가 아니다.
- 엄격하지 않고, 고급 프로그래밍 기술을 지원하지 않아 생긴 오해

### 5. 웹 표준이다.
- HTML5 : HTML5 + CSS3 + JavaScript

### HTML에 CSS js 파일 불러오기
```html
<html>
    <title>HTML과 JavaScript</title>
    <link rel="stylesheet" href="css/style.css"> <!--relation, hypertext reference-->
    <script src="script.js"></script>
</html>
```

## 데이터 타입과 변수

### JavaScript 구문

1. 해석순서 : Interpreter 위에서 아래로 해석
2. 대소문자구분
    - HTML은 대소문자 구분하지 않음
    - HTML의 속성값은 소문자로 구분
3. 구문 끝 : `;`
4. 공백과 들여쓰기
    - 공백이 필요할 때 : 키워드와 데이터 구분
        - 변수 정의 : `var intvar`
        - 함수의 선언 : `function f(){}`
    - 공백이 필요하지 않을때 : 키워드 뒤에 `쉼표,괄포,연산자` 존재시
    - 가독성 높이는 들여쓰기
5. 주석
    - `/*여러줄 주석*/`
    - `//한줄 주석//`

### 기본 데이터 타입
숫자 문자 불린 단순데이터 객체데이터

1. Number
    - 정수와 실수 구분X
    - **literal : `그 자신으로 해석되어야 하는 값`**
    - 정수리터럴 : -253 ~ 253
    - 정수 : -9007199254740992 ~ 9007199254740992
    - 실수 : 무한대
    - 상수 : 미리정해져있는 숫자
        NaN : 숫자가 아닌 값
        Number.NaN : 숫자가 아닌 값
        Number.MAX_VALUE : 최대 수
        Number.MIN_VALUE : 최소 수
        INFINITY : 무한대를 의미

2. 문자열
    - 텍스트 표현하는 문자 집합
    - char형 존재 X
    - 문자리터럴 : `'`,`''`로 둘러싸인 문자 집합
    - Escape Sequence
        - \b : backpace
        - \f : Form feed
        - \n : Newline
        - \O : Nul character
        - \r : Carriage Return
        - \t : Horisontal tab
        - \v : Vertical tab
        - \' : Single quote or apostrophe
        - \" : Double quote
        - \\ : Backslash
        - \ddd : 라틴 0~377
        - \xdd : 라틴 16진수00~FF
        - \uddd : 우니코드 16진수

3. Boolean
    - True, False

4. 단순 데이터 타입
    - null
        - 0,""와는 다름
        - 어떠한 데이터 타입고 가지지 않음
        - 변수에 아무 값이 없음
    - undefine
        - 정의되어 있지 않음
        - 값이 할당된적 없는 변수, 생성되지 않는 객체

5. 객체 데이터 타입
    - Object
        - 다양한 값의 집합
        - 값 : Property, 이름이 붙여져 있음
        - 객체 리터럴
            - `var a = {property1, property2, ...}`
            - property : [속성:값] 의 쌍
            - 빈 객체 : `ver a = {};`, `ver a = new Object();`
            - 미리 정의된 객체 : `ver a = new Data();`
        - 객체 property 접근 : 객체이름.property이름
    
    - Array
        - 배열 : 값의 집합
        - 배열의 값 : 연속되는 숫자의 인덱스
        - 배열 생성
            - ver a = new Array();
            - ver a = {10, true, 3.5, "orange"};
        - 배열 요소 : 어떠한 데이터 타입이라도 가능
        - 할당 : a[0] = 값
    
    - fuction
        - 미리 정의되어 실행 가능한 코드 덩어리
        - 반복 호출 가능
        - 자바프로그래밍 기본 단위
        - 하나의 데이터 타입으로 변수에 할당 가능
        - 함수 생성
            - function 함수이름(전달인자) { return 리턴값; }
        - 함수 리터럴
            - var 변수이름 = 함수이름(전달인자) { return 리턴값; }
            - 호출 : var 변수이름2 = 변수이름1(전달값);
    
    - 변수
        - 타입 설정하지 않아도 됨
        - 선언 : `var 변수이름 = 값`
        - 선언 되지 않은 변수에 변수 값 할당시 전연변수로 선언
        - 유효범위 : 함수를 기준으로 결정
            - 지역변수 : 함수 안에서 선언된 변수, 함수 내부로 사용 제한
            - 전역변수 : 모든 함수에서 사용 가능한 변수
            - 전연변수 선언 : 최상위 위치에서 변수 선언
    -변수_참조 타입 : 문자열, 객체 등은 변수에 담을 수 없음