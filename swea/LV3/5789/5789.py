'''
1~N번 N개상자, 디폴트 = 0
Q회, 범위상자 = 동일 숫자
i회차에 L~R 상자를 i 로 변경
------------데이터-----------
0~N개 상자 만들고 (인덱스 동일)
Q회동안 반복하며
i번째에 L~R (인덱스동일) 상자 i값으로 변경

'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    boxs = [0] * (N + 1)
    for i in range(1,Q + 1):
        L, R = map(int, input().split())
        for k in range(L, R + 1):
            boxs[k] = i
    boxs = [str(i) for i in boxs[1:]]
    print(f'#{tc} ', end='')
    print(' '.join(boxs))