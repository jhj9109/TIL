import sys
from collections import deque
#313

def BFS(v):
    dq = deque()

    #v = dq.popleft()
    visited[v] = True
    print(v, end='-')
    for w in G[v]:
        if not visited[w] and w not in dq:
            dq.append(w)
            #print(dq)

    while dq:
        v = dq.popleft()
        visited[v] = True
        print(v, end='-')
        for w in G[v]:
            if not visited[w] and w not in dq:
                dq.append(w)
                #print(dq)

sys.stdin = open('input.txt')

V, E = map(int, input().split())

G = [ [] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

BFS(1)
