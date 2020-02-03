"""
다음의 결과와 같이 임의의 URL 주소를 입력받아
protocol, host, 나머지(path, querystring, ...)로
구분하는 프로그램을 작성하십시오.
http://www.example.com/test?p=1&q=2
"""

data_str=input()

num1=data_str.find("://")
num2=data_str.rfind("/")
cnt = len(data_str)
print("protocol: {0}".format(data_str[0:num1] ))
print("host: {0}".format(  data_str[num1+3:num2])) 
print("others: {0}".format( data_str[num2+1:cnt+1] ) )