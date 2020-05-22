import sys
sys.stdin = open('input5249.txt')
import heapq


def prm(V, E, adj):
    INF = float('inf')
    mst = [False] * (V+1)
    key = [INF] * (V+1)
    pq = []

    result = 0
    
    key[0] = 0
    heapq.heappush(pq, (0, 0))
    
    while pq:
        k, node = heapq.heappop(pq)
        if mst[node]:
            continue
        mst[node] = True
        result += k

        for dest, wt in adj[node]:
            if not mst[dest] and wt < key[dest]:
                key[dest] = wt
                heapq.heappush(pq, (key[dest], dest))
    return result
    

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = {i :[] for i in range(V+1)}
    for _ in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])
        adj[e].append([s, c])
    print(f'#{tc} {prm(V, E, adj)}')