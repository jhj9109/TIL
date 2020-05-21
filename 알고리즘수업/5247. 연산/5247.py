import sys
sys.stdin = open('input5247.txt')

from collections import deque

def bfs(): # k:단계, val:값
    v = [0] * 1000001
    cnt = 0
    if N == M:
        return 0
    q = deque([(0, N)])
    while q:
        cnt += 1
        k, n = q.popleft()
        if n == M:
            print(cnt)
            return k
        # if not v[n]:
        #     v[n] = 1
        # if  0 <= n-10 <= 1000000:
        q.append((k+1, n-10))
        # if  0 <= n*2 <= 1000000:
        q.append((k+1, n*2))
        # if  0 <= n-1 <= 1000000:
        q.append((k+1, n-1))
        # if  0 <= n+1 <= 1000000:
        q.append((k+1, n+1))
    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs()}')

'''
cnt
기본 : 44 | 205 | 41644
기본 & 0 ~ 백만 : 15 | 70 | 39194

기본 & visited : 44 | 129 | 2252
기본 & 0 ~ 백만 & visited : 15 | 49 | 2105
'''