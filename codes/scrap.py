import requests
import bs4


url = 'https://finance.naver.com/sise/'

response = requests.get(url).text
#요청을 보내서 응답받은 결과
#response에 임시 저장

data=bs4.BeautifulSoup(response,'lxml')
#파서 lxml로 특정
#위 코드는 파이썬이 보기 좋도록 구조화

kospi=data.select_one('#KOSPI_now')
kosdaq=data.select_one('#KOSDAQ_now')
#class냐 id냐 구분, id앞에는 # 붙여준다

print(kospi.text)
print(kosdaq.text)
#그 안에 글자만 보여줘 print(kospi.text)

