def DFS(v, target, res):
    visited[v] = True
    if v == target:
        res[0] = 1
        return

    for w in G[v]:
        if not visited[w]:
            DFS(w, target, res)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    visited = [False for _ in range(V+1)]
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
    #print(G)
    start, target = map(int, input().split())
    res = [0]
    DFS(start, target, res)

    print(f'#{tc} {res[0]}')