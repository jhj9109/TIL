"""
다음 결과와 같이 문자열을 입력하면
짝수 인덱스를 가진 문자들을 출력하는
프로그램을 작성하십시오.
"""

#a=input()
a="H1e2l3l4o5w6o7r8l9d"
cnt = len(a)
data_str =""
for i in range (0,cnt,2):
    data_str += a[i]
print (data_str)

#0~2k
#0~2k-1