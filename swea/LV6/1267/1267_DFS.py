import sys

sys.stdin = open('input3.txt')

def DFS(v, res):
    visited[v] = True
    res.append(str(v))
    
    for w in G[v]:
        if not visited[w]:
            DFS(w, res)

T = 2
for tc in range(1, T+1):    
    V, E = map(int, input().strip().split())
    line = list(map(int, input().strip().split()))
    visited = [False for _ in range(V+1)]

    G = [[] for _ in range(V+1)]
    for i in range(E):
        G[line[i*2]].append(line[i*2+1])
    for i in range(1, V+1):
        if len(G[i]) != 0:
            res = []
            visited = [False for _ in range(V+1)]
            DFS(i, res)
            if len(res) == V:
                break
    print('#{}'.format(tc), ' '.join(res))