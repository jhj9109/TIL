import sys
sys.stdin = open('input1486.txt')
import time
start_time = time.time()

from itertools import combinations

def go(N, B, max_height): # 점원수, 탑의높이, 전체 직원의 키높이
    result = max_height
    for r in range(N+1):
        flag = True
        for lst in combinations(height, r): #combi : 원소 r개 짜리 집합 , 각 원소 이터러블 >>> sum
            temp = max_height - sum(lst)
            if temp < B:
                continue
            flag = False
            result = temp if temp < result else result

        if flag: # 더 이상 만족할수 있는 케이스 X
            break
    return result - B

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    max_height = sum(height)

    print(f'#{tc} {go(N, B, max_height)}')

print(time.time() - start_time, 'seconds')