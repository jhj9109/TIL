"""
콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.
"""
#>>> print(“{0}”.format( list ( map ( lamda x: pow(x,2) , data_list ) ) ) )

import math

PI=math.pi
num_list=list(map(int,input().split(', ')))
result=""
for n in num_list:
    result += "%0.2f, "%(2*PI*n)
print(result[0:-2])