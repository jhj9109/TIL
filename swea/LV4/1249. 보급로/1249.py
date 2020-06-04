import sys
sys.stdin = open('input1249.txt')
import time
start_time = time.time()

def Dijkstra():
    maxV = (2 * N - 3) * 9
    v = [ [maxV]*N for _ in range(N)]
    
    #초기값
    v[0][0] = 0
    w = (0, 0) # w선택
    U = set()
    U.add(w)
    v[0][1] = f[0][1] # w의 인접정점 갱신
    v[1][0] = f[1][0]
    
    while len(U) != N*N:
        # w선택
        minV = (2 * N - 3) * 9 + 1
        for u in U:
            for dr, dc in [ (0,1), (1,0), (0,-1), (-1,0) ]:
                nr, nc = u[0]+dr, u[1]+dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in U and v[nr][nc] < maxV:
                    minV = v[nr][nc]
                    w = (nr, nc)
        U.add(w)

        # w 인접정점 갱신
        for dr, dc in [ (0,1), (1,0), (0,-1), (-1,0) ]:
            nr, nc = w[0]+dr, w[1]+dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in U:
                nValue = v[w[0]][w[1]] + f[nr][nc]
                v[nr][nc] = nValue if nValue < v[nr][nc] else v[nr][nc]

    return v[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    f = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {Dijkstra()}')

print(time.time() - start_time, 'seconds')