'''
T
문자열
하이픈의 갯수
넣을 위치
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    n = len(word)
    H = int(input())
    data = list(map(int, input().split()))
    num = [0] * (n+1) # 0 ~ n
    for d in data:
        num[d] += 1

    # num = dict
    # for i in data:
    #     if i in num:
    #         num[i] += 1
    #     else:
    #         num[i] = 1
    

    res = ''
    res += '-' * num[0]
    for i in range(n): #숫자 0~n , 
        res += word[i] + '-' * num[i+1]
    print(f'#{tc} {res}')