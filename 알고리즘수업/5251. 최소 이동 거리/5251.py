import sys
sys.stdin = open('input5251.txt')

def go(N, adj):
    INF = float('inf')
    dist = [INF] * (N+1)
    selected = [False] * (N+1)
    
    dist[0] = 0
    cnt = 0
    while cnt < N+1:
        
        minV = INF
        u = -1
        
        for i in range(N+1):
            if not selected[i] and dist[i] < minV:
                minV = dist[i]
                u = i

        selected[u] = True
        cnt += 1 

        for dest, wt in adj[u]:
            dist[dest] = min(dist[dest], dist[u] + wt)
    
    return dist[N]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = {i :[] for i in range(N+1)}
    
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])
    
    print(f'#{tc} {go(N, adj)}')