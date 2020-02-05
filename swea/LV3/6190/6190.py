'''
T 입력
N 갯수
N개 정수
-----데이터---
data = 리스트형태로 정수 저장
for i in r
'''
import sys
sys.stdin = open("input.txt")


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     #data = list(map(int, input().split()))
#     data = list(input().split())

#     max_num = -1
#     for i in range(N):
#         for j in range(N):
#             if i != j:
#                 flag = True
#                 temp = str(int(data[i]) * int(data[j]))
#                 for n in range(len(temp)-1):
#                     if temp[n] > temp[n+1]:
#                         flag = False
#                         break
#                 if flag:
#                     if int(temp) > max_num:
#                         max_num = int(temp)
#     print(f'#{tc} {max_num}')


# T = int(input())
# for tc in range(1, T+1):
#     NN = int(input())
#     data = list(map(int, input().split()))
#     N = len(data)
#     multis = sorted([data[x] * data[y] for x in range(N-1) for y in range(x+1,N)], reverse=True)
#     #print(multis)
#     for multi in multis:
#         flag = True
#         num = multi
#         i = 1
#         temp = num % (10 ** i) #N자리 몫 N-1, 나머지 N
#         num -= temp
#         while num // (10 ** i) != 0:
#             i += 1
#             if temp < num % (10 ** (i)):
#                 flag = False
#                 break
#             num -= num % (10 ** (i))
#         if flag:
#             print(f'#{tc} {multi}')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    products = sorted([numbers[i]*numbers[j] for i in range(n-1) for j in range(i+1, n)], reverse=True)
    for product in products:
        current = str(product)
        previous_digit = int(current[0])
        for digit in current:
            if int(digit) < previous_digit:
                break
            else:
                previous_digit = int(digit)
        else:
            result = product
            break
    else:
        result = -1
    print('#{} {}'.format(tc, result))