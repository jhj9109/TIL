# 문서객체모델 (DOM)

## DOM의 이해와 window 객체

### 코어 JavaScript와 클라이언트 측 JavaScript

- 코어 JS : JS의 기본이 되는 부분만 정의
- DOM 스크립트 : 웹 브라우저 관련된 JS
  - 웹 브라우저, 웹 문서의 내용 객체화 > property로 read / write

### DOM 레벨과 혼란

- 웹브라우저의 비호환의 주범 : DOM

- DOM : 객체화 > 구조화 > 계층
- 웹 브라우저 윈도우
  - Window 객체
    - Window 객체 이외의 객체는 Window 객체의 property로 접근
  - Document 객체



### 윈도우의 크기와 위치 정보 (읽기 부분만)

- 브라우저 창의 크기
  - UI 포함 : `window.outerWidth`, `window.outerHeight`
  - UI 제외 : `window.innerWidth`, `window.innerHeight`
- 창의 위치 정보
  - 모니터 좌측 상단으로부터 창까지 거리 : `window.screenX`, `window.screenY`
  - 브라우저 창 내부 스크롤 조작 : `window.pageXoffset`, `window.pageYoffset` > 특정 이미지 부분 확대 관찰 기능 구현에 사용



### 윈도우의 생성

- `window.open( "HTML페이지주소", "새로 생성될 창의 이름", "width=값, height=값, menubar, location, resizable, scrollbars, status=yes")` 

```javascript
window.addEventListener('load', init, false); //윈도우 로딩 완료시 init이란 함수 호출
fuction init(){
	var p = document.getElementsByTagName("p"); //태그에서 요소 get
	p[0].addEventListener('click', 함수명, false); // 예제에서 p 2개 > 배열로
    function 함수명(){
        var w = window.open("HTML주소", "창 name", "속성들");
    }
}
```

- open시 창의 이름이 같으면 수정된다.

- `window.close()` 

### alert

- '승인' 단추를 누르기 전까지 모든 스크립트 정지
- `웹페이지의 메시지`, `JavaScript` 표시는 보안상의 이유로 지울수없다
- `window.alert("멘트");`, `alert("멘트");`
- window객체 : 전역객체

## 웹 문서 접근

- CSS : 선택자 > HTML 문서 내의 요소에 접근
- DOM : 웹 브라우저와 HTML 문서의 모든 기능과 요소에 접근
- 레벨 0
  - 문서 객체 배열로 접근 `document.프로퍼티[인덱스]`
    - anchors
    - images
    - applets
    - links
    - forms
  - name 속성 접근 `document.personalInfo.네임`
    -  `document.personalInfo.button.addEventListener(인자들)`
    - var 변수1 = document.personalInfo.네임;
    - 변수1.함수 : checked, value, focus(), 

- 표준 DOM
  - 모든 요소에 접근하기 위해 문서를 트리로 표현
  - 중첩된 요소들은 부모와 자식 관계로 계층화
  - 노드 객체 : HTML 요소, 도큐먼트, 텍스트, 속성까지 의미

### 새로운 방법_문서 내 노드 접근 1

- getElementsByTagName()
  - 배열로 반환
- getElemetById()
  - Id = 유일 : 하나만 반환

### 새로운 방법_노드의 순환

- 자식 노드 접근
  - `chidNodes[]`
  - `firstChild`
  - `lastChild`
  - ex : `documnet.getElementById("ol 아이디").childNodes[인덱스].lastchild.textContent`
    - ol : id
    - li : childNodes[인덱스] **내가 알고있는것과 다른듯 ㅠㅠ**
    - li내부 ==`<span class="listTitle">습관1:</span>습관내용`
    - 습관내용 : lastchild 
    - 텍스트 : textContext
- 부모 노드 접근
  - `parentNode`
- DOM 문서 트리 내에 같은 계층에 있는 요소들에게 접근
  - `nextSibling`
  - `previousSibling`

- `getElementsByClassName()`

- `getElementsByName()`

- `querySelectorAll()` , `querySelector()`



## 웹 문서의 조작

### write / writeln

- DOM 초기 메소드로 노드 적용 불가
- 로딩 완료후 호출시 모든 컨텐츠를 지우고 출력하므로 주의



### 노드의 생성과 삽입

- `createElement()`
- `createTextNode()`
- `appendChild()` : 특정 노드의 자식으로 삽입

- `부모노드.insertBefore(삽입할노드, 레퍼런스 노드)` : 특정 요소 앞에 삽입

- `부모노드.replaceChild(새로운노드, 바뀔노드)`



### 노드 속성 조작

- getAttribute(), setAttribute()
  - `노드.getAttribute("속성명")`
  - `노드.setAttribute("속성명","속성값")`

### 노드에 CSS 속성 적용

- `노드.style.css속성 = css속성값`
  - 하이픈>대문자로 ex : background-color > backgroundColor



### innerHTML

- HTML5에서 표준으로 인정됨
- createElement(), createTextNode(), appendChild()를 한꺼번에 처리하는 효과 발휘
- ex : document.getElementById("id값").innerHTML = 스트링