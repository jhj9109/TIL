import os
import sys
import requests
import urllib.request
from pprint import pprint
from decouple import config

client_id = config('NAVER_CLIENT_ID')
client_secret = config('NAVER_CLIENT_SECRET')

url = "https://openapi.naver.com/v1/vision/celebrity"

p_url = "https://ww.namu.la/s/91986ffc01b6136fb453c4ff8b3e63adf90e525e6b10e1643058339c924830276d1fc646c2ac918d1f31e83c59308ea232acb64afb280dabeee0afc024b9dd3031526ace08eb8a4acf0a0d8852e6ae06d2ea1f1a90186c028ba9053ef2c822e9"
#data=urllib.request.urlopen(p_url).read

#files = {'image': open(data, 'rb')}
files = {'image': open('jd.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
pprint(response.json())
# url = "https://openapi.naver.com/v1/vision/face" // 얼굴감지  
# rescode = response.status_code
# if(rescode==200):
#     print (response.text)
# else:
#     print("Error Code:" + rescode)