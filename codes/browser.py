import webbrowser

base_url = 'https://search.naver.com/search.naver?query='

words= ['아이유','수지','설현']

for word in words:
    webbrowser.open(base_url+word)

#배치스크립트 컴퓨터 오픈시 프로그램 실행
#요청은 url
#응답은 문서

#웹스크레핑
#크롤링(지속적으로 정보를 계속 읽는것)