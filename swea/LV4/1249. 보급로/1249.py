import sys
sys.stdin = open('input1249.txt')
import time
start_time = time.time()

import heapq

def Dijkstra(): #힙사용
    maxV = (2 * N - 3) * 9
    v = [ [maxV]*N for _ in range(N)]
    u = [ [0] * N for _ in range(N)]
    pq = []

    #초기값
    v[0][0] = 0
    heapq.heappush(pq, ( v[0][0], (0,0) ) )
    
    while pq:
        # 최소값 찾기
        val, (r, c) = heapq.heappop(pq) 
        
        # u로 선택
        u[r][c] = 1

        # w 인접정점 갱신
        for dr, dc in [ (0,1), (1,0), (0,-1), (-1,0) ]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and not u[nr][nc]:
                nValue = v[r][c] + f[nr][nc]
                if nValue < v[nr][nc]:
                    v[nr][nc] = nValue
                    heapq.heappush(pq, (v[nr][nc], (nr,nc) ) )
    return v[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    f = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {Dijkstra()}')

print(time.time() - start_time, 'seconds')