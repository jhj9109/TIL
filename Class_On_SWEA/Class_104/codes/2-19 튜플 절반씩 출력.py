"""
주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의
앞 항목 절반과 뒤 항목 절반을
출력하는 프로그램을 작성하십시오.
"""
data_list = (1,2,3,4,5,6,7,8,9,10)

num = len(data_list)

temp=[]
for i in range(1,6):
    temp.append(i)
print("{0}".format(tuple(temp)))

temp=[]
for i in range(6,11):
    temp.append(i)
print("{0}".format(tuple(temp)))
