def DFS(v, res):
    visited[v] = 1

    res.append(str(v))

    for w in G[v]:
        if not visited[w]:
            DFS(w, res)
    
import sys

sys.stdin = open('input.txt')

V, E = map(int, input().split())

G = [ [] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

res = []

DFS(1, res)

print('-'.join(res))