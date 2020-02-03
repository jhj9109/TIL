data_list=list(range(100,301))
"""
백자리 (x//100)몫 %2 ==0
십자리 ((x//10)몫)%10%2==0
일자리 (x%10)%2==0
"""

filter_condition = "(x//100)%2 == 0"
filter_list=list(filter(lambda x:(x//100)%2 == 0,data_list))

filter_condition = "((x//10)몫)%10%2==0"
filter_list=list(filter(lambda x:((x//10))%10%2==0,filter_list))

filter_condition = "(x%10)%2==0"
filter_list=list(filter(lambda x:(x%10)%2==0,filter_list))

num=len(filter_list)
n=1
for i in filter_list:
    if n != num:
        print(i,end=",")
        n+=1
    else:
        print(i)