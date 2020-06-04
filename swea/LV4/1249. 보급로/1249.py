import sys
sys.stdin = open('input1249.txt')
import time
start_time = time.time()

from collections import deque
def bfs(r, c):
    maxV = (2 * N - 3) * 9
    v = [ [maxV]*N for _ in range(N)]

    q = deque( [[r, c]] )
    v[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [ (0,1), (0,-1), (-1,0), (1,0) ]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                nValue = v[r][c]+f[nr][nc]
                if nValue < min(v[nr][nc], v[N-1][N-1]) :
                    v[nr][nc] = nValue
                    if (r, c) != (N-1, N-1):
                        q.append( [nr, nc] )
    return v[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    f = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {bfs(0, 0)}')

print(time.time() - start_time, 'seconds')