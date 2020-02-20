#심화 실습:다음실시간검색어
import requests
import bs4

url = 'https://www.daum.net/'
response = requests.get(url).text
data=bs4.BeautifulSoup(response,'lxml')

#아래 두 코드는 날짜
date = data.select_one('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > span').text
print(f'{date[5:7]}월 {date[8:10]}일 기준 실시간 검색어\n')

#select_one
for i in range(1,11,1):
    issues=data.select_one(f'#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li:nth-child({i}) > div > div:nth-child(1) > span.txt_issue > a')
    print(issues.text)


"""
#select
route='#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li > div > div:nth-child(1) > span.txt_issue > a'
keywords = data.select(route) # 리스트와 유사한 객체 >>> 순회가 가능한다.

for keyword in keywords:
    print(keyword.text)

# for idx, item in enumerate(keywords):
#    print(f'{idx+1:2>}위 검색어: {item.text}')
"""

