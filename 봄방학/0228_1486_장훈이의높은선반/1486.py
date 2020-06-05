import sys
sys.stdin = open('input1486.txt')
import time
start_time = time.time()
from itertools import combinations

def total_sub(item):
    global result
    h = max_height
    lst = list(item)
    for l in lst:
        h -= l
        if h < B:
            return False
    result = h if h < result else result
    return True

def go(): # 점원수, 탑의높이, 전체 직원의 키높이
    for r in range(N+1):
        flag = True
        for iterable in combinations(height, r): #combi : 원소 r개 짜리 집합 , 각 원소 이터러블 >>> sum
            if total_sub(iterable):
                flag = False

        if flag: # 더 이상 만족할수 있는 케이스 X
            break

T = int(input())
T = 5
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    max_height = sum(height)
    result = max_height

    go()
    print(f'#{tc} {result-B}')

print(time.time() - start_time, 'seconds')