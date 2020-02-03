"""
단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.
"""

a= input()
a= a.split(', ')
b=[]
for i in a:
    temp = int(i)
    b.append(temp)
data_list = [i for i in b if i%2==1]
i=1
for d in data_list:
    if i==3:
        print(d,end="")
    else:
        print(d,end=', ')
    i+=1
print("")