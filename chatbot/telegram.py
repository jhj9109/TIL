import requests
#파이썬이 문서를 이쁘게 출력하는 pprint
from pprint import pprint 
from decouple import config

base_url= 'https://api.telegram.org'
key = 'TELEGRAM_BOT_TOKEN'
update_url = f'{base_url}/bot{key}/getUpdates'
# #1.chat+id 먼저 받아오기(사용자)
# response = requests.get(update_url).json() #.json()통해 텔레그램이 읽을 수 있는 언어로 변환
# pprint.pprint(response)
# chat_id=response['result'][0]['message']['chat']['id']
# print(chat_id)

# #2. 받아온 chat_id로 메세지 보내기
# text = '파이썬으로 보낸 메세지'
# message_url = f'{base_url}/bot{key}/sendMessage?chat_id={chat_id}&text={text}'
# requests.get(message_url)

#3.메세지 보낸 사람 모두의 chat_id 전부 받아오기
#.json()통해 텔레그램이 읽을 수 있는 언어로 변환
response = requests.get(update_url).json() 

"""
chat_ids = []
for result in response['result']: #갯수만큼 : 6
    #print(result['message']['chat']['id'])
    chat_ids.append(result['message']['chat']['id'])
#print(set(chat_ids)) #받아온 chat_id를 출력하는것임

#4. 메세지 보낸 사람 모두에게 chat 보내기
data_set = set(chat_ids) #위에서 받은 chat_id를 중복제거
"""
chat_ids = set()#set으로
for result in response['result']:
    chat_ids.add(result['message']['chat']['id'])#add로

text = input()
for i in chat_ids: #chat_ids 셋객체로 변경
    requests.get(f'{base_url}/bot{key}/sendMessage?chat_id={i}&text={text}')

# ###메세지 분석
# for result in response['result']:
#     if result['message']['text'] =='안녕':