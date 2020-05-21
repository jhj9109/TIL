import sys
sys.stdin = open('input5247.txt')

from collections import deque

def bfs(): # k:단계, val:값
    v =  [0] * 1000001
    # cnt = 0
    q = deque( [N] )
    while q:
        # cnt += 1
        n = q.popleft()
        if n == M:
            # print(cnt)
            return v[n]

        for cal in [n-10, n*2, n-1, n+1]:
            if 0 <= cal <= 1000000 and not v[cal]:
                q.append(cal)
                v[cal] = v[n]+1
    return abs(N-M)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = bfs()
    print(f'#{tc} {res}')

'''
cnt
기본 : 44 | 205 | 41644
기본 & 0 ~ 백만 : 15 | 70 | 39194

기본 & visited : 44 | 129 | 2252
기본 & 0 ~ 백만 & visited[n] : 15 | 49 | 2105
기본 & 0 ~ 백만 & visited[cal] : 10 | 25 | 918
'''