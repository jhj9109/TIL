#기초실습:네이버금융 원/달러 환율 가져오기

import requests
import bs4

url = 'https://finance.naver.com/'

response = requests.get(url).text

data=bs4.BeautifulSoup(response,'lxml')

route='#content > div.article2 > div.section1 > div.group1 > table > tbody > tr.up.bold > td:nth-child(2)'

ex=data.select_one(route)#copy selector : 해당 값까지 특정되는 최단 경로를 찾는다.

print('현재 원/달러 환율은 ',ex.text)



