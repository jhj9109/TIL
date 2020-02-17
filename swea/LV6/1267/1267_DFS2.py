import sys
from pprint import pprint 
sys.stdin = open('input.txt')

def DFS(v, res):
    visited[v] = True
    res.append(str(v))
    
    for w in G[v]:
        if (not visited[w]):
            for idx in G2[w]:
                if not visited[idx]:
                    break
            else:
                DFS(w, res)

T = 10
for tc in range(1, T+1):    
    V, E = map(int, input().strip().split())
    line = list(map(int, input().strip().split()))
    visited = [False for _ in range(V+1)]
    G = [[] for _ in range(V+1)]
    G2 = [[] for _ in range(V+1)]
    for i in range(E):
        G[line[i*2]].append(line[i*2+1])
        G2[line[i*2+1]].append(line[i*2])
    res = []
    visited = [False for _ in range(V+1)]

    for i in range(1, V+1):
        for j in range(1, V+1):
            if (len(G[j]) != 0) and (i in G[j]):
                break
        else:
            DFS(i, res)
        if len(res) == V:
            print('#{}'.format(tc), ' '.join(res))
            break
    #print('#{}'.format(tc), ' '.join(res))