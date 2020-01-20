# Python의 문법

## 1.저장

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

#### 실습

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

#### 추천강의

- 코세라 앤드류웅(스탠퍼드) 딥러닝
- CS90 컴퓨터구조
- udacity : 하이엔드 교육 >>> 머신러닝 개론 introduction to machine learning udacicy
- Mooc 플랫폼
- 파이썬
  - introduction to copter science python (edx.org)
  - berkeley 61a SCIP

## 2.조건

> if(True) : func()

- 코드블록을 들여쓰기(Indantaion)으로 형성
- 들여쓰기 : 1Tab or 4Space

#### 실습

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



## 3.반복

> while 조건문 : func()	조건문이 True인 동안 반복, 종료조건이 필요
>
> for i in List : func()	정해진 범위 안에서 순회, 정해진 횟수 반복하므로 종료조건 불필요

#### 실습

```python
for i in range(5):
  print('안녕하세요!')
  
n=0
while n<5:
  print('안녕하세요!')
```



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



### Python함수

- 내장함수
- 외장함수 : ex) random.choice(리스트) , random.sample(리스트,갯수)
- 샘플링 : 비복원추출 (ex. 로또번호)

#### 실습

> 로또추첨기

```python
# 아래에 코드를 작성하세요.
import random

data_list=list(range(1,46))
lotto = random.sample(data_list,6) #random.sample(뽑을통, 갯수)

print(sorted(lotto))#sort는 리턴값X,

print(sorted(random.sample(list(range(1,46)),6) ))
```







