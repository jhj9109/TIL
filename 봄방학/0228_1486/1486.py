import sys
sys.stdin = open('input1486.txt')
from itertools import combinations
def total_sub(total, B, item):
    lst = list(item)
    for l in lst:
        total -= l
        if total - B < 0:
            return -1
    return total

def go(n, B, total):
    res = 10000 * n
    for r in range(n+1):
        flag = True
        temp_res = 10000 * n
        for iterable in combinations(height, r): #combi : 원소 r개 짜리 집합 , 각 원소 이터러블 >>> sum
            ret = total_sub(total, B, iterable)
            if ret != -1:
                flag = False
                temp_res = ret-B if temp_res > ret-B else temp_res
        res = temp_res if res > temp_res else res
        if flag:
            break
    return res

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    total = 0
    for h in height:
        total += h

    print(f'#{tc} {go(N, B, total)}')