import sys
sys.stdin = open('input5248.txt')

def bfs(n):
    v[n] = 1
    for w in range(1, N+1):
        if G[n][w] and not v[w]:
            bfs(w)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = list(map(int, input().split())) # 2*M
    
    G = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        a, b = d[2*i], d[2*i+1]
        G[a][b], G[b][a] = 1, 1 
    
    v = [0] * (N+1)
    res = 0
    for i in range(1, N+1):
        if not v[i]:
            bfs(i)
            res += 1
    print(f'#{tc} {res}')
