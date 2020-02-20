import requests
from pprint import pprint
from decouple import config

client_id = config('NAVER_CLIENT_ID')
client_secret = config('NAVER_CLIENT_SECRET')
                                                                #post 문서로 보내야하고, 문서엔 헤더가 존재
papago_url = "https://openapi.naver.com/v1/papago/n2mt"         #헤더엔 문서의 정보, 메타의 정보가 들어간다.
text = '띵작'

headers = {
    'X-Naver-Client-Id' : client_id,
    "X-Naver-Client-Secret" : client_secret, # ',' 파이썬,장고 +자바 붙이는것 허용
}

data = {
    'source' : 'ko',
    'target' : 'en',
    'text' : text    
}

response = requests.post(papago_url, headers=headers, data=data)   #requests.post(url, 헤더정보}, {데이터}) ,헤더와 데이터는 딕트형태

#.json()
pprint(response.json())