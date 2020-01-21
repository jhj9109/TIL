# Python의 심화

> #컴퓨터조작 # 웹스크래핑 #파일명바꾸기

## Ⅰ 컴퓨터 조작하기

- Python IDLE

- 쉘 애밀레이터 -> 리눅스와 유사

- Git 설치

- 마지막 단계에서 Launch Git Bash

### (1) cmd 명령어

- `pwd` : printing working directory

- `ls` : 현재 디렉토리 보여줘

- `cd` : chage directory 
- `mkdir` : make directory
- `code` : 코드에디터 열기
- `cls` : 지우기

- 검색시 `철자일부 +Tab`  : 자동으로 검색

- 홈 디렉토리 `~`로 표시

  

- `.` : 현재 폴더 의미
- `..` : 상위 폴더 의미
- `cd ..`: 상위 폴더로 이동
- `cd ~` : 홈 디렉토리로 이동
- `code .` : 현대 폴더 기준으로 열기
- `mkdir 만들고자하는 폴더명` : 폴더생성
- `ctrl+n` : New File
- `Linter pylint is not installed.` : 스타일, 장고 들어갈때 할 예정

- 파이썬 익스텐션 설치하기 : 익스텐션스 > Python 검색 > 설치
- `python --version` : 파이썬 버전 체크, 파이썬에게 무언가 시킬때 python 치면 됌
- `python 파일명.py` : 파이썬아 `파일명.py` 실행해줘
- `request` : 요청에 대한 응답을 처리 하기 위함



### (2) Python 명령어

- **import webbrowser**

- `webbrowser.open(url)`

- Sniffing : 네트워크 주변을 지나다니는 패킷을 엿보면서 추적하는 행위

- query : 질의

- 한글 : url언어로 변경

- ```python
  #개발모드 (디버깅) : 오토 로딩  
  if __name__ == '__main__' :
      app.run(debug=True)
  ```



## Ⅱ. 웹 브라우저를 조작하기

1. 검사
2. 네트워크
3. 헤더스

- DNS : 이름주소를 실제 어드레스로 변환

- 네이버 : 들어올때 일어나는 일들 말해보세요
- 앞으로 고객이 아닌 제공자 입장에서 생각해보기
- thevc.kr
- 토스 카뱅 뱅크샐러드
- 가치 투자유치 * 10배 / 100억이상투자받은곳.안전

- 오후에 제공자 입장으로 vonvon만들기

### (1) cmd 명령어

#### 	1.1 PIP

- `pip` : 매니징 해주는 아이
- `pip install 이름` : 파이썬 패키지 인스톨
- `pip list` : 니가 가지고 있는 거 보여줘 (여기선 명령어,기능)
- `pip install Faker` :페이크 데이터 생성
- `fake = Faker('ko_KR')` : 한국 언어 설정

- ` requests` : 브라우저 요청 응답 해주는 패키지 설치

- `bs4` : Beautiful Soup 버전4 설치

- `lxml` : 문서를 더 빨리 찾게 도와주는 도구

### (2) 기타

- bs4 : HTML안에서 특정 정보를 빨리 찾게 만들어주는 프로그램,  (파이썬이 파씽) 구조화=파씽, 트리 구조

- 사이트 요청에 대한 응답 response의 결과

- 상태코드 : 200 - O.K, 4xx -사용자 잘못, 5xx - 개발자 잘못



html

head / body

​		 / div / div

id : 식별,구분하기 위함

코스피 지수 : id=KOSPI_now , class=num

- 크롬에서 내가 원하는 부분 우클릭 검사 -> 위치 대략 찾아줌 

1. copy selector >>> #KOSDAQ_now



스크랩핑

1. url 입력
2. ID 입력 or Html > body > div 아래 경로 : 모두 `copy selector`로 긁어 오면 된다

### (3) 기초 실습 : 네이버 금융 원/달러 환율가져오기

### (4) 심화 실습 : query.py 

# API 활용하기

> Dictionary와 유사한 Json, Json 형식의 페이지를 보기 좋게 Json viewer
>
> Json 문서로 응답 받음, Json :  Key와 value를 가진다. 

- f스트링 : f'문자열{인자}'

- IM 완전탐색
-  Pro B형 효율성
- 교집합 

```python
cnt = len (set(리스트1) & set(리스트2))
```

# Flask

>플라스크 : 서버 만들수 있는 환경

- 플라스크와 텔레그램 연결, 텔레그램 위에서 작동하는 챗봇 만들것
- `flask run` : 서버 구동
- `import render_template` : html 렌더링, `templates` : 폴더에 넣어야 하는 규칙
- `request` : 받은 데이터 활용
- return render_template('이름.html', 보낼네임=값)

- @ : 데코레이터
- /`<name>`  : 변할 수 있는 변수 
- /`<int: name>` : 미리 자료형을 변경
- 입력&출력 : int 안됌
- datetime.now().month / datetime.now().day

# HTML

> HyperText Markup Language : 마크를 하는 언어, 링크가 달린 문서

- `<` `>` : Tag를 통해 표현한다
- `html`
- `head`
- `title` : 브라우저에 보이는 이름
- `body` : 중요한 정보들이 들어간다
- `h1~h6`
- `hr` : 밑줄, 단태그
- `p` : paragraph 문단
- `a` : anker
- `href` : 하이퍼 래퍼런스
- `li` : list
- `ul` : unordered list >>>뷸렛 포인트
- `ol` : ordered list >>>넘버링 포인트
- `input type="text"` : 
- `input type="submit"` : 
- `input name` = "query" : ?query=input값을 전송한다 (검색창 input값 네이버 : query, 다음,구글 : q) 
- `form action="주소"`  : 무엇가를 전송할때 사용한다. input을 감싸준다. 주소로 이동한다
- `input placeholder="멘트"` : 무엇을 입력할지 알려주는것
- `!`+`tab`: 기본 양식 자동완성
- viewport : for 모바일 최적화
- http-equiv : for 익스플러어
- `{{이름}}`: Mustache, 이름=값 으로 넘어온 정보 사용



# 배포

> pythonanywhere 사용