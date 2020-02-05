'''
1. 10 x 10 격자 생성
2. input으로 주어진 조건에 따라 색칠
    - 왼쪽 상단 인덱스 & 오른쪽 하단 인덱스
3. 겹쳐진 구간 출력
'''

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0

    tile = [[0] * 10 for _ in range(10)]
    # [[0] *10] * 10 속도차이가 나서  comprehension쓰는게 좋다

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                tile[i][j] += color
                if tile[i][j] = 3:
                    cnt += 1