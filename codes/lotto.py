import requests
import random

#1.requests를 통해 동행로또 API에 요청을 보내기
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=893'


#response = requests.get(url).text #str
response = requests.get(url).json() #dict

winner =[]

for num in range(1,7):
#   winner.append(response['drwtNo'+str(num)])
    winner.append(response[f'drwtNo{num}'])
print(winner)

for _ in range(1000):
    lotto = random.sample(range(1,46),6)
    cnt = len(set(lotto) & set(winner))
    if cnt == 4:
        print('당첩입니다.')