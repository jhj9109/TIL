#_*_ coding: utf-8 _*_

#07-12.py

"""
step1
*
**
***
****
step2
*
**
***
****
*
**
***
****
step3
    *
   ***
  *****
 *******
*********
"""
###step1###
# for i in range(1,5): #step1 1~4개 별 프린트
#     print("*"*i)    #*i 반복제어변수
#단체 주석처리 ctrl+/

# i=1
# while i <= 4:
#     print("*"*i)
#     i+=1

###step2###
# for i in range(1,3):
#     for k in range(1,5):
#         print("*"*k)

# i,k=1,1 #while문은 for문 대비 변수 설정 필요
# while i<=2:
#     while k<=4:
#         print("*"*k)
#         k+=1
#     i+=1
#     k=1 #k를 초기화해주는 코드가 없었다

###step3###
"""
5/1/5
4/3/4
3/5/3
2/7/2
1/9/1
11
"""

i,k=5,1
while i>=0:
    print("{0}{1}".format(" "*i,"*"*(2*k-1)))
    i-=1
    k+=1
'''
i,k=5,1
while i>=0:
    print("{0}".format(" "*i),"*"*(2*k-1)) #이코드도 되긴된다.
    i-=1
    k+=1
'''