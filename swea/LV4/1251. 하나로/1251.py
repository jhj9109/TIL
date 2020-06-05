import sys
sys.stdin = open('input1251.txt')

import heapq

def prim():
    INF = float('inf')

    mst = [False] * N
    key = [INF] * N
    pq = []
    total = 0

    key[0] = 0
    heapq.heappush(pq, (0, 0))
    while pq:
        k, u = heapq.heappop(pq)
        if mst[u]:
            continue

        mst[u] = True
        total += k

        for w in range(N):
            if not mst[w] and adj[u][w] < key[w]:
                key[w] = adj[u][w]
                heapq.heappush(pq, (key[w], w))
    return float(total)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    land = [[0, 0] for _ in range (N)]
    for i, x in enumerate(map(int, input().split())):
        land[i][0] = x
    for i, y in enumerate(map(int, input().split())):
        land[i][1] = y
    E = float(input())
    adj = [ [0] * N for _ in range(N)]
    for i in range(N-1):
        for j in range(1, N):
            adj[i][j] = adj[j][i] = (land[i][0]-land[j][0])**2 + (land[i][1]-land[j][1])**2
    print(f'#{tc} {round(E * prim())}')