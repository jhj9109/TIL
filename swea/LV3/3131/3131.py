# for num in range(2, (10 ** 6)+1):
#     div = 2
#     while num % div and num != div:
#         div += 1
#     if num == div:
#         print(num, end=' ')
#----------------위 단순방식----------

'''
2,5 제외하면 1 3 7 9
'''
print(2,3,5,7, end=' ')
for num in range(11, (10**6)+1,2):
    div = 2
    while div < num ** (1/2):
        if not(num % div):#소수가 아니면
            break
        div += 1
    else:
        print(num, end=' ')