# Flask

1. app.py에 코드 추가하여 개발모드로 오토 로딩 구현

   ```python
   if __name__ == '__main__' :
       app.run(debug=True)
   ```

2. index.html 생성, 홈에 전생앱과 검색다모아 연결

3. 미세먼지 API

4. 공공데이터 : data.go.kr

5. 신청서 작성하여 키를 발급받아 사용 :  : 오픈 API - 개발계정 - 일반 인증키 발급

6. 인증키 발급후 API url로 가야 웹페이지 열림

7. [http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=RXxXREkZGUr8U6mRqDFPhHlVFCeSJ62DduqYu741yjYJfq3IZHY2KO%2B5F6MOTZocSezXbuu8uVkC53f7gigm4Q%3D%3D&numOfRows=10&pageNo=3&sidoName=%EC%84%9C%EC%9A%B8&ver=1.6](http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=RXxXREkZGUr8U6mRqDFPhHlVFCeSJ62DduqYu741yjYJfq3IZHY2KO%2B5F6MOTZocSezXbuu8uVkC53f7gigm4Q%3D%3D&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6)

8. XML 문서로 작성 되어 있음

# 챗봇 만들기

## Ⅰ. 텔레그램 API

- 봇 관리하는 BotFather
- http://t.me/Bangpandabot
- my <token> : 프라이빗한 키값 생성
- 기본설명 : MAking requests
- https://api.telegram.org/bot<token>/METHOD_NAME
- send message
- Getting Method
- setWebhook : 



- 샘플 URL : `https://api.telegram.org/<token>/getMe`
- ```json
  {
  ok: true,
  result: {
  	id: 1035873187,
  	is_bot: true,
  	first_name: "Jangbot",
  	username: "Bangpandabot",
  },
  }
  ```

- 샘플 URL : `https://api.telegram.org/<token>/getUpdates`

- ```json
  {
  ok: true,
  result: [ ],
  }
  ```

- Json으로 응답받음

#### getMe

>Bot의 상태
>
>https://api.telegram.org/<token>/getMe

```json
{
ok: true,
result: {
	id: <나의 봇id>,
	is_bot: true,
	first_name: <나의 봇 닉네임>,
	username: <나의 봇 고유네임>",
},
}
```

#### getUpdate

> Bot의 상태 업데이트 여부
>
> https://api.telegram.org/<token>/getUpdates

```json
{
	ok: true,
	result: [ ],
}
```



#### sendMessage

> Bot으로 메세지 보내기
>
> https://api.telegram.org/<token>/sendMessage?chat_id=<나의아이디>&text="<보낼텍스트>"

- chat_id
- text
- parse_mode
- disable_web_page_preview
- disable_notification
- reply_to_message_id
- reply_markup

#### setWebhook

> 텔레그램에 문지기 역할을 맡기기 (웹훅)

1. **getUpdate** 하다가

2. 뭔가 변화가 있으면 나에게 알려줘

3. 알림이 요청으로 들어온다

4. 서버(**Flask**에서는 요청(변화발생)이 발생하면 처리(응답)한다

   어디로 알려줄까? : **URL**

5. 여기서는 메아리(앵무새) 동작을 수행한다.

6. 요청을 대신 받아주는 **ngrok**

#### 기반 만들기

- app.py

- home.html

#### 실수 한거

- `templates`가 아닌 template로 오타
- `request.args.get`이 아닌 requests.args.get으로 오타



## Ⅱ. 챗봇에서 사용한 언어 리뷰

### 1. url은 f스트링 이용하여 작성

```python
base_url= 'https://api.telegram.org'
key = '키'
update_url = f'{base_url}/bot{key}/getUpdates'
```

### 2. .get()을 사용하여 chat_id 1개 받기

```python
#요청하기.url전달받아서.텔레그램에게 번역,응답:변수저장
#요청내용은 업데이트
response = requests.get(update_url).json()
#pprint.pprint(response) #출력테스트
```

### 3. 받아온 chat_id에 **requsets.get(url)** 요청을 통해 메세지 보내기

```python
text = "보낼 텍스트는 변수에 저장하기"
message_url = f'{base_url}/bor{key}/sendmessage?chat_id={chat_id}&text={text}'

requests.get(message_url)
```

### 4. 메세지 보낸 사람 모두의 chat_id 모두 받아오기

#### 	1. list 이용한 버전

```python
response = requests.get(update_url).json()
#pprint.pprint(response) #출력해서 확인해보기

#텔레그램코드상 ID 까지의 경로 주소 path_str
path_str = result['message']['chat']['id']
chat_ids=[] #list, set 두가지 방식
for result in response['result']:
    # print(path_str) 출력테스트
    # 아래를 통해 리스트 객체 안에 ID들이 각각 저장
    chat_ids.append(path_str)
#print(set(chat_ids)) #출력테스트    
```

#### 	2. set 이용한 버전

```python
response = requests.get(update_url).json()
path_str = result['message']['chat']['id']

chat_ids= set()

for result in response['result']:
   chat_ids.add(path_str) #set은 append 사용 불가
```

### 5. 정리한 chat_id에 메세지 보내기

```python
chat_ids = set()#set으로
for result in response['result']:
    chat_ids.add(result['message']['chat']['id'])#add로

text = input()
for i in chat_ids: #chat_ids 셋객체로 변경
    requests.get(f'{base_url}/bot{key}/sendMessage?chat_id={i}&text={text}')
```



- 

## setWebhook

> 이 방법을 사용하여 URL을 지정하고 발신 웹 후크를 통해 수신 업데이트를 수신하십시오. 봇에 대한 업데이트가있을 때마다 JSON 직렬화 [업데이트가](https://core.telegram.org/bots/api#update) 포함 된 HTTPS POST 요청을 지정된 URL로 보냅니다 . 실패한 요청의 경우, 우리는 합리적인 시도 횟수 후에 포기합니다. 성공하면 *True* 를 반환합니다 .
>
> Webhook 요청이 Telegram에서 온 것인지 확인하려면 URL에 비밀 경로를 사용하는 것이 좋습니다 (예 :) `https://www.example.com/`. 아무도 당신의 봇의 토큰을 알지 못하기 때문에 당신은 그것이 우리임을 확신 할 수 있습니다
>
> Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized [Update](https://core.telegram.org/bots/api#update). In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns *True* on success.
>
> If you'd like to make sure that the Webhook request comes from Telegram, we recommend using a secret path in the URL, e.g. `https://www.example.com/`. Since nobody else knows your bot‘s token, you can be pretty sure it’s us.

## ngrok

> 요청을 대신 받아줌 (대신전해드립니다^-^)
>
> 중간에 프록시 형성

로컬컴퓨터(Flask) ↔ 프록시(ngrok) ↔ 텔레그램

- cmd에서만 실행 가능 , 파이썬은 깃 배쉬에서 실행

- `ngrok http 5000` : ngrok아 내가 http를 받을건데 포트는 5000번이야

- Forwarding : https://6527adf0.ngrok.io -> http://localhost:5000

  전달하는것

## 웹

- methods=['POST']
- methods=['GET']

```python
@app.route('/telegram', methods=['POST']) #결국 텔레그램이 쓸 주소임
def telegram():
    return '', 200 # '':아무것도 보내지 않는다
```



## 아래 주소 입력에 대한 웹페이지 반환

https://api.telegram.org/bot1035873187:AAEsFm_4mJBgdSW4pZsq_3u4NCPnXoD5RtI/setWebhook?url=https://6527adf0.ngrok.io/telegram

```json
{
ok: true,
result: true,
description: "Webhook was set",
}
```



- Terminal >>>다른거 삭제>>>bash 정지 >>>터미널내 배쉬로 app.py 실행 >>> 터미널 O.K



```python
@app.route('/telegram', methods=['POST']) 
def telegram():
    response = request.get_json() #계속응답중, POST는 '_'
    pprint(response['message']['text'])
    return '', 200
```



- 메세지속 2줄 복사 , chat_id와 text 정보만 채우면 된다
- 메아리 >>> text =response....

```python
#메아리 완성
@app.route('/telegram', methods=['POST']) 
def telegram():
    response = request.get_json() #계속응답중, POST는 '_'
    text = response['message']['text']
    chat_id = response['message']['chat']['id']
    message_url = f'{base_url}/bot{key}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(message_url)
    return '', 200
```

## 파파고 API를 써보자

> 승인을 받아 Key를 갖고 있어야 한다

- 와챠의 영화 추천툴 같은 협업툴 40줄이면 O.K 
- 가이드 따라가보기
- post방식 requests.post(url, 헤더정보, 데이터)

- CFR API
- id, key 바꾸고, open('f.name')







## 점심 추천 봇

- IF문의 향연
- .get('Key') : 해당 항목이 없어도 에러나지 않는다.

```python
import random
@app.route('/telegram', methods=['POST']) 
def telegram():
    response = request.get_json() #계속응답중, POST는 '_'
    text = response['message']['text']
#------------------------------------------------------------------------------------#
    if text == '점심메뉴':
        menu = ['스테이크', '참치회', '장어곰탕', '치킨', '햄버거']
    	text = random.choice(menu) #파이썬은 블록안의 변수도 스코프 안에 갖히지 않는다
    chat_id = response['message']['chat']['id']
    #chat_id = response.got('message').get('chat').get('id')
    message_url = f'{base_url}/bot{key}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(message_url)
    return '', 200
```



## .env 사용하여 프라이빗 숨기기

- 'pip install decouple --user' : 먼저 파일을 설치한다. (∵--user는 우리가 admin이 아닌 상태로 쓰고 있음)
- `from decouple import config` : 코드에서 불러온다
- 숨긴파일 : `.`으로 시작하는 파일네임
- config() 사용
- env 쓸때는 `변수=빈칸없이` 처럼 한칸 띄면 안된다

- pip3.7 install decouple --user