# 레이아웃과 고급 CSS 기능
## 레이아웃 정렬

### 2단 레이아웃

- 다단 레이아웃 : 세로로 여러 개의 단
- HTML 문서는 오로지 위에서 아래로 콘텐츠 제시
- 플로팅과 포지셔닝 사용

- float
    1. HTML 문서 작성
        - `<div id="명칭">콘텐츠 영역의 속성을 설정하기 위한 요소</div>`
    2. section 넓이 설정
        - CSS 작성
        - margin과 padding 초기화
        - `#명칭{width:수치px}` 넓이 : 마진 + 패딩 + 보더굵기
    3. float 속성 설정
        - `float: 속성값;`
        - left, right
        - nav 요소 : 왼쪽으로 플로팅
        - nav+section 요소 : 오른쪽으로 플로팅
        - footer 올라오는거 방지
            - 방법 1 : nav, nav+section 높이 같게 지정
            - 방법 2 : footer에 clear 설정 `footer{clear:both;}`
- `position: 속성값;`
    - `relative`
        - 초기 볼륨을 유지 >>> 좌표의 원점 파악 어려움
        - 2단 레이아웃 설정하는 것은 바람직 하지 않음
    - `absolute`
        - 요소들의 원점 == 부모 요소의 왼쪽 상단 (중복)
        - 형제 요소들을 각각 위치를 수치로 조절

- `display: 속성값;`
    - `inline-block`
        - 블록을 글자 같이 취급 >>> 자간 공백문제
        - 아래 정렬 (디폴트) >>> top 정렬로 해결 가능
## CSS 네비게이션

### 인터렉티브 이미지 버튼
- HTML 이미지 버튼
    - `<input type="image" src="images/normal.png" alt="Button">`
    - 사용하지 않음
- CSS 인터렉티브 이미지 버튼
    - `<a class="button" href="#">Button</a>`
    - `a.button{속성:값;}`
        - `display: block;`: w,h 조절 위해
        - `background-image: url(파일);`
        - `background-positon: 0 0;`
        - `text-decoration: none` : 링크 파란 밑줄 제거

### 네비게이션 만들기
- 텍스트 네비게이션
    - 텍스트 > 그래픽 네비게이션으로 발저
    - 제작 쉽고 빨라 속도를 위해 사용 ex: 구글검색창

    - HTML로 텍스트 네비게이션 구조 작성
        - nav 요소 안에서 작성
        - 목록 형태 : 링크의 목록
        - 목록 작성 시 순서는 상관 X : <ol>, <ul>
        - 목록 아이템 : 링크

    - CSS로 텍스트 네비게이션 스타일 적용하기
        - **`display: inline` : 줄바꿈X, 블릿 사라짐**
        - 링크에 설정되어 있는 기본 스타일 초기화
            - `text-decoration: none;`
        - `*{margin:0; padding:0;}`
        - `a:hover{color: 색깔;}` : 마우스 롤오버시 선택자
        - `#current{color: 색깔;}` : 현재 페이제 메뉴 선택
    
## CSS 변형과 트랜지션

### 요소의 변형
- 요소 숨기기
    - ? : 웹브라우저에서 보이지 않게 하는 것
    - 이유
        - CSS 미지원시 : CSS로 숨긴 컨텐츠가 보여짐
        - 시각 장애인용 콘텐츠 제공
        - 가독성 증대
            - 펼쳐지는 콘텐츠
                - CSS의 요소 숨기기 속성 이용
                - js 사용하여 CSS 속성 조절
    - 속성
        - `visibility: 속성값;`
            - hidden, visible
            - 원래 요소가 점유했던 크기 유지한채 감추기
        - `display: 속성값;`
            - none : 점유 영역과 함께 사라짐

### 요소 클리핑
- 요소 클리핑
    - clip 속성 : 이미지 또는 요소의 특정 부분만 보이게 함
    - position: absolute; 로 지정
    - rect(상,우,하,좌) : 사각형으로 요소를 클리핑, 기준 상단, 좌측

 