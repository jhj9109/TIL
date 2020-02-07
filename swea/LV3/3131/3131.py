# for num in range(2, (10 ** 6)+1):
#     div = 2
#     while num % div and num != div:
#         div += 1
#     if num == div:
#         print(num, end=' ')
#----------------위 단순방식----------
#-------------아래 두번째 도전----------
# '''
# 2,5 제외하면 1 3 7 9
# '''
# print(2,3,5,7, end=' ')
# for num in range(11, (10**6)+1,2):
#     div = 2
#     while div < num ** (1/2):
#         if not(num % div):#소수가 아니면
#             break
#         div += 1
#     else:
#         print(num, end=' ')

#---------------에라스토의체----------------

num = [True]*1000000 #십만개 형성, 999999까지
    
num[0]=False#숫자0
num[1]=False#숫자1
for i in range(2, 1001): #2~1000 : 50만,17만,12.5만,10만,8.3만,7.1만.... 
    if num[i]: #2~1000
        for j in range(i+i, 1000000, i): #그 숫자의 제곱근까지 소수 판별하면 된다.
            num[j]=False                    #제곱근까지 판별....어떤수를 곱해
    
for i in range(2, 1000000):
    if num[i]:
        print(i, end=' ')