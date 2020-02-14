def DFS(v):
    visited[v] = 1
    stack.append(v)
    visited[v] = True
    print(v, end='-')

    while stack:
        p = v
        for w in G[v]:
            if not visited[w]:
                stack.append(w)
                v = w
                visited[w] = True
                print(v, end='-')
                break
        else:
            if p == v:
                v = stack.pop()



import sys

sys.stdin = open('input.txt')

V, E = map(int, input().split())

G = [ [] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

DFS(1)
