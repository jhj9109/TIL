import sys
sys.stdin = open('input1486.txt')
import time
start_time = time.time()

from itertools import combinations

def powerset(N, k, r, l, h): # k:depth, r: 목표 원소 갯수 l: 현재 원소 갯수, sums: 값
    global result, flag
    if h < B:
        return
    if r == l:
        result = h if h < result else result
        flag = False
        return
    if N == k:
        return
    powerset(N, k+1, r, l+1, h-height[k])
    powerset(N, k+1, r, l, h)

def go(N, B, max_height): # 점원수, 탑의높이, 전체 직원의 키높이
    global flag
    for r in range(N+1):
        flag = True
        powerset(N, 0, r, 0, max_height)
        if flag: # 더 이상 만족할수 있는 케이스 X
            break

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    max_height = sum(height)
    result = max_height
    flag = True

    go(N, B, max_height)
    print(f'#{tc} {result - B}')

print(time.time() - start_time, 'seconds')