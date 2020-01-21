# Python의 문법

## Ⅰ. 저장

- 저장의 개념은? Save?
- 무엇을, 어떻게 저장 할 수 있는가
- `=`의 의미는 저장한다(할당한다).
- `==`의 의미는 같다
- 무엇을 저장하는가
  1. 숫자 : 현실세계에 존재하는 모든 숫자 (글자는 No)
  2. 글자 : 현실세계에 존재하는 모든 글자 & `"`로 둘러쓴 글자
  3. 참/거짓 : 조건, 반복에 사용됨

- 하드코딩은 지양, 값은 저장해서 사용한다.
- 어떻게 저장하는가
  1. 변수 (variable) : 박스
  2. 리스트(List) : 여러 박스를 붙임 `[ ]`를 사용
  3.  딕셔너리(Dictionary) : 견출지를 붙임 `{ }`를 사용

### (1) 실습

- 프린트 & 리스트 & 딕셔너리 활용

```python
# 랜덤하게 뽑아줄때
import random #외부에서 뭔가를 불러와서 쓴다

# menu 리스트를 만들어주세요.
menu = ['스테이크','성게알밥','트러플그라탕','참치회']

phone_book = {
  '스테이크':'010-1234-5678',
  '성게알밥': '010-1111-2222',
  '트러플그라탕' : '070-2222-4444',
  '참치회' : '080-3333-6666'
}

food = random.choice(menu)
        # s      v    인자
        # s:목적어역할

#print (food+'입니다.'+'전화번호는' + phone_book[food]+'입니다')  #푸드 이름으로 전화번호 찾기
print (f"{food}입니다. 전화번호는 {phone_book[food]}입니다.") #3.6부터 생성 f스트링
print ("{}입니다. 전화번호는 {}입니다.".format(food,phone_book[food])) #3.6이전 f스트링
```



## Ⅱ 조건

> if(True) : func()

- 코드블록을 들여쓰기(Indantaion)으로 형성
- 들여쓰기 : 1Tab or 4Space

### (1) 실습

```python
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'.format(key)
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
item = soup('item')[5]
time = item.dataTime.text
dust = int(item.pm10Value.text)

# dust 변수에 들어 있는 내용을 출력해보세요.
print('{} 기준 미세먼지 농도는 {}입니다.'.format(time, dust))

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.

if dust >150 :
  print('매우나쁨')
elif dust > 80:
  print('나쁨')
elif dust > 30:
  print('보통')
else :
  print('좋음')
```



## Ⅲ 반복

> while 조건문 : func()	조건문이 True인 동안 반복, 종료조건이 필요
>
> for i in List : func()	정해진 범위 안에서 순회, 정해진 횟수 반복하므로 종료조건 불필요

### (1) 실습

```python
for i in range(5):
  print('안녕하세요!')
  
n=0
while n<5:
  print('안녕하세요!')
```

## Ⅳ. 추천강의

- 코세라 앤드류웅(스탠퍼드) 딥러닝
- CS90 컴퓨터구조
- udacity : 하이엔드 교육 >>> 머신러닝 개론 introduction to machine learning udacicy
- Mooc 플랫폼
- 파이썬
  - introduction to copter science python (edx.org)
  - berkeley 61a SCIP

# API

> Applecation Interface Programming

- 아마존 : 트래픽 수요위한 자원 보유 &클라우드 컴퓨팅 인프라(API) >>> AWS
- 코드를 모르면 API에 접근 할 수 없다.
- WEB에서의 커뮤니케이션 방식 : 웹에서 동작하는 SW service
- Service의 두가지 : 요청(request)과 응답(response)
- url : Web에서의 유일한 요청 통로
- HTML, XML, json : 문서로 응답
- **오픈소스기술 + API통신** = 쉬워진 프로그래밍
- API 내부함수를 알 필요가 없다. Input 과 Output만 알면 된다.



# Python 함수

>내장함수
>
>외장함수 : ex) random.choice(리스트) , random.sample(리스트,갯수)
>
>샘플링 : 비복원추출 (ex. 로또번호)



# 실습

## Ⅰ. 로또추첨기



```python
# 아래에 코드를 작성하세요.
import random

data_list=list(range(1,46))
lotto = random.sample(data_list,6) #random.sample(뽑을통, 갯수)

print(sorted(lotto))#sort는 리턴값X,

print(sorted(random.sample(list(range(1,46)),6) ))
```

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
- Pro B형 효율성
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

