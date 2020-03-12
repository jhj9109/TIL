# CSS 문서표현(하)

## 텍스트 표현, 컬러와 배경

### 서체의 지정과 텍스트 지정
- 서체의 지정과 크기 설정
    - 문서 외형 꾸미기, 특성 제시, 구조 이해 용이
    - 웹 이용자간의 서체 공유X
    - 운영체제간에도 다른 서체들을 제시
- font-family
    - 비슷한 모양의 서체를 묶어서 제시
    - `font-family:서체,대체제1,대체제2;` 모두 없으면 기본 서체
- 일반 폰트 패밀리
    - serig(명조체) : 서체 끝 장식 X
    - sans-serif(고딕체) : 서체 끝 장식 O
    - monospace(고정폭 글꼴) : 글자마다 폭이 동일
    - cursive(필기체)
    - fantast(판타지)
- 서체 크기 조절
    - `font-size:값pt`
    - 크기 단위
        - 절대 크기
            - pt(포인트) : 1in = 72pt
            - pc(파이카) : 12pt = 1pc
        - 상대 크기
            - px(픽셀) : 모니터 화소 하나
            - %(퍼센트) : 부모 요소에 대한 상대적 크기 (100%)
            - em : 부모 요소에 상대적 크기 (1)
            - ex : 소문자 크기 비율
- 변형 서체
    >`font-style : 값`
        - italic
        - oblique : 강제로 기울인 italic
        - normal
    > `font-weight : bold`
        - bold
        - bolder, lighter : 부모 요소보다 더
        - 100~900
        - normal
    > `font-variant : small-caps`
        - small-cap : 알파벳 문자, 텍스트의 크기로 대소문자 표기

### 텍스트 스타일 설정
- 텍스트 간격
    - 자간 : `letter-spacing : 값단위`
    - 단어간 : `word-spacing : 값단위`
    - 행간 : `line-height : 값단위`
- 텍스트 스타일
    - 텍스트 정렬
        - 가로
            - `text-align:값`
            - 블록레벨에만 적용 가능
            - left, right, center, justify(양끝 정렬), auto, text-top

        - 세로 : `vertical-align:값`
            - inline : 상대적인 수직 위치
            - table : top, middle, bottom
    - 텍스트 indent
        - `text-indent : 값단위`

### 컬러와 배경 설정
- 컬러
    - 웹 색상 코드 : `color : # red green blue` 각 수치는 16진수or 10진수 0~255
    - HSL 표현
        - Hue(색조) : 0~360
        - Saturation(채도) : %
        - Lightness(명도) : %
        - `color:hsl(값, 값%, 값%)`
    - 색상 키워드
        - red등 정해져있는 키워드 사용, but 정밀한 색깔 표현 어려워 잘 사용되지 않는다.
    - 투명도 표현 : 10진수, color의 4변째 변수 == 투명도 (0투명 ~ 1불투명)

- 배경 설정
    - 배경
        - HTML의 블록요소에 사각형 형태의 영역
        - 크기, 배경색, 이미지
    - 배경색 : `background-color:값;`
    - 배경 이미지 : `backgrond-image:url("주소");`
    - 배경 이미지 반복 : `background-repeat : 속성`
        - repeat(기본), repeat-x, repeat-y, no-repeat
    - 배경 이미지 고정 : `background-attachment : 속성;`
        - fixed, scroll
    - 배경 이미지 위치와 크기
        - `background-position: x값단위, y값단위`
        - `background-size : x%, y%` : 상대적인 크기

## 목록, 표 꾸미기

### 블릿 꾸미기
- 블릿 스타일 설정
- 블릿 : 목록 아이템 앞에 붙는 숫자 또는 특수 문자
    - `list-style-type:값`
        - ol
            - decimal
            - decimal-leading-zero
            - upper-alpha
            - lower-alpha
            - upper-roman
            - lower-roman
        - il
            - disc
            - circle
            - square
        - none
    - `list-style-image:url(값);`
    - `list-style-position:값;`
        -inside, outside : 블릿이 목록 아이템 텍스트 보다 안/앞에 나타남

### 목록 꾸미기
- Margin, Padding
    - Margin : 박스 바깥쪽 여유 공간
        - `margin: 북px, 동px, 남px, 서px;`
    - Padding : 박스 안쪽 여우 공간
- Border
- Border : 테두리 선
    - 표 Border
        - `border-width: 굵기px;`
        - `border-style: 스타일;`
            - none, hidden, solid(실선), deshed, dotted, double
            - groove(골), ridge(툭튀), inset, outset
        - `border-color: 색깔`
        - **`table{굵기 스타일 색깔}`**
        - ex : `table {나열}`, `th, td{나열}`
        - `border-spacing: 간격px;`
        - `border-collapse: collapse`
        - 부분 선택 : `border-부분: 나열;`
    - 셀 padding
        - `th, td {padding: 여백px}`
    - 셀 배경색
        - `선택자{background-color:값;}
- 기타 설정
    - 빈 셀 감추기
        -`empty-cells: 값;`
            - empty, show
        - `border-collapse: collapse`면 적용 불가 : 셀 여백이 있는 표에만 적용 가능
    - caption 위치 정렬
        - `caption-side: 위치;`

## CSS 박스 모델

- 박스 모델
    - HTML 문서 body부분의 모든 요소가 사각형 영역 가짐
    - 요소를 박스로 구성, 위치와 상관관계 지정하는 방식
- margin, padding
### CSS 박스 모델 기초
- 블록 vs Inline의 margin과 padding
    - 웹브라우저 기본 margin, padding
        - `*{margin:0; padding:0;}` : CSS작성시 초기화한다.
    - 블록(사방), Inline(좌우) 만 margin과 padding 적용
    - width, height : 블록만 적용가능
        -`width: 값px; height: 값px`
    - 요소의 크기 : w, h, padding, border-width, margin

- margin 겹침
    - 연속되는 요소 margin 요소 적용시 겹치는 현상 발생
    - 큰 값으로 겹침

### position
- 다른 요소들과 어떠한 관계 속에서 위치 결정하는지 설정
- `position: 속성값;` `오프셋방향: 값px`
    - `relative` : 원래 위치(부모요소)에서 설정한 위치만큼 이동
    - `absolute` : 기본 흐름에서 벗어나 요소를 띄워 줌
        - `z-index: 값` : 높을 수록, default : HTML 나중에 기술된 순서로
    - `fixed` : 브라우저 원점기준