# 01차시. HTML5의 이해



- W3C : Worild Wide Web Consortium의 약자, 웹 표준 개발 논의 재정하는 조직
- DOCTYPE : HTML 문서형식 선언
- metadata : 문서, 파일 정보 들어있는 내부 데이터

- 학습내용

1. HTML 역사, 특징 의미
2. 전문적인 텍스트 에디터 특징
3. DOCTYPE 선언, HTML 기본구조 학습
4. `<head>`부분 타이틀, 문자 인코딩, 메타데이터 학습
5. 외부 CSS파일, Javascript 파일 연결 방법

- 학습목표

1. HTML 구조 이해, HTML 문서 작성
2. 문자 인코딩 이해, 설정
3. 중요 메타데이터 설정
4. 외부 CSS 파일, JavaScript파일 HTML 파일 연결





## 최근 웹 기반 사업과 기술

- 웹 기반 사업과 기술의 발전에 따른 HTML 한계 극복

1. ​	Ajax : 자바스크립트 이용, 웹서버와 동기화 된 웹이 한계 극복
2. Web2.0 : 사용자의 능동 참여, 편의성 극대화 웹
3. 미디어의 활용
4. 다양한 모바일 디바이스 탄생
5. 웹 어플리케이션 : 문서 작성등 다양한 기능을 하는 웹 어플리케이션 등장

- 동적인 웹을 위한 표준화 기술 요구

1. 게임, 웹 어플리케이션을 비로스 동적웹 요구 증가
2. 플래쉬, 실버라이트, 자바 >>> 동적인 웹 제작에 사용
3. 플래쉬, 플러그인 방식에 대한 거부

- W3C의 XHTML2 발전 예고 >>> 여전한 웹 구조, 표현에 집중 >>> 반발 >>> WHATWG 탄생

HTML Living Standard : apple, google, microsoft, mozilla

2019 5/18 : 대통합

- 지오로케이션 : 위치 정보 처리
- 웹소켓 : 웹 서버와 실시간 통신
- 웹스토리지 : 클라이언트 저장 공간 활용
- 웹워커 : 다중 프로세서의 배면 작업



- 텍스트 에디터 : Notepad++, Komodo Edit, Aptana Studio 3



## Doctype 지정, HTML 구조

### 1. DOCTYPE 지정

> 웹 브라우저가 정확히 HTML을 표현하기 위해 HTML 버전 명시
>
> HTML5 : `<!DOCTYPE html>`

### 2. HTML 서식

요소 : HTML의 마크업(연산X) 명령어, 대소문자 구분 X

- 표현 : 콘텐츠와 구분하기 위해 꺽쇠로 둘러쌈

- 범위 : `<시작태그>` , `</마침태그>` , 단독으로 사용되는 빈요소 : `<br>` 줄바꿈 ,  `<img>` 이미지요소

- 속성 기술 : HTML 필수적, 부가적인 설정 값 의미 

  요소명 뒤에 `공백 하나`를 두고 `속성명="속성값"` 형식으로 기술, 속성값은 `'`나 `"`로 표시한다 

### 3. HTML의 헤드와 바디

head

- 내용이 담긴 body처리전, 설정부분

- HTML의 metadata, Scriptm, CSS등이 위치
- 콘텐츠는 넣지 않는다

body

- 콘텐츠가 담기는 곳
- 입력한 내용 웹 브라우저에 표시

## HEAD 설정하기

- 타이틀 : HTML파일의 제목
- 문자인코딩 : 인코딩 형식, 저장시에도 문자인코딩 형식 설정 >>> `<meta charset="UTF-8">`
- 메타데이터 : 파일에 관한 정보, 빈요소
  - ex : 사진 - 날짜, 모델명, 노출, GPS, ex : MP3 - 연주자, 앨범 정보, 가사
  - HTML - 문자인코딩, 설명, 키워드, 작성자, 저작권, 연락처, 작성일
  - 필요성 : 유명 검색 로봇에 의해 수집되는 정보
  - HTML에 대한 정보 기록
    - `<meta name="이름"content="내용"
    - decription : 간략한 설명
    - keywords : 키워드
    - author : 작성자
    - copyright : 저작권 정보
    - reply-to : 연락처 메일
    - date : 작성일

### 외부 파일 연결

웹 페이지 3 요소

- HTML : 콘텐츠 구조 정의

- CSS : 콘텐츠의 레이아웃, 표현등 외향을 정의

- JavaScript : 콘텐츠의 작동 정의

HTML에 CSS, JavaScript 연결

- CSS : `<link rel="stylesheet" href="css/style.css>"` HTML파일 위치 기준 상대 위치 기록 + 추가 type, media도 가능
- JavaScript : `<script language="javascript"></script>`
- `<script src="js/script.js"></script>` : HTML5 표기



# Why learn HTML5?

> 웹 어플리케이션 개발을 하기 위해서 >>> sw 개발을 위해서

웹 커리큘럼

PJT를 통한 SW 개발 주기 경험 / GIT 통한 프로젝트 관리 / 프레임워크, SW개발 학습 방법

- Statice web : HTML, JS, CSS
- Dynamic Web with framework : django
- SPA with frontend framework

# 개발 환경 설정

Visual Studio Code + 패키지



소스코드 알고 싶다 -> 검사

element.Style : 디버깅가능

Network : 

slow 3g : 인터넷 접속 속도 관련 체험가능

caiuse.com

Hyper Text : 서로 링크 O >>> 주고받는 규칙 Hyper Text Tranfer Protocol

<html lan="ko">

## 메타데이터 새로운 규약

open graph protocol

카톡 공유시. property = "og:title" ... 

## 시맨틱태크

header : 문서 전체나 섹션의 헤더

nav : 네비게이션

aside: 사이드에 위치한 공간, 메인 콘텐츠와 연관성 low

section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현

article : 문서,페이지, 사이트 안에서 독립적으로 구분되는 영역

footer : 문서 전체나 섹션의 푸터(마지막 부분)

- 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
- 구역 나누기 X 의미 담긴 태그
- 검색엔진최적화SEO를 위해 메타태그, 시맨틱태그 마크업 효과적 할 필요가 있다.
- Non semantic 요소 div, span / h1 table태그도 시맨틱태그

보이는 화면이 아닌 의미 있는 태그로 분루되어있는지.

## 인라인 / 블록(다른줄) 요소

>  css에서 더 자세한 내용 다룰 예정

## 그룹컨텐츠

- p
- hr
- ol, ul
- pre, blockquote
- figure, div

## 텍스트 관련 요소

- a
- b : X >>> 모양은 css
- strong : 강조
- em : 강조
- i : X >>> 모양은 css
- span, br, img

## table

> 이러한 내용이 있다

## form

- 서버에서 데이터 처리
- 