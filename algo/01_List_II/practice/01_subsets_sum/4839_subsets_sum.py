"""
T = int(input())
for T in range(T):
    #원소 N개짜리 부분집합의 합 K의 갯수 result 출력
    N, K = map(int, input().strip().split())
    arr = list(range(1,12+1))

    result = 0
    for i in range(2 ** len(arr)):
        sums = 0
        lens = 0
        for j in range(len(arr)):
            if i&(1<<j):
                sums += arr[j]
                lens += 1
        if lens == N and sums == K:
            result += 1
    print(f'#{T+1} {result}')
"""
import sys
sys.stdin = open("input.txt")
from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    subsets = combinations(range(1, 13), N)
    # cnt = 0
    # for subset in subsets:
    #     if sum(subset) == K:
    #         cnt += 1
    cnt = sum(1 for subset in subsets if sum(subset) == K)
    print(f'#{tc} {cnt}')