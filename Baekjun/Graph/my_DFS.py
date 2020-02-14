from pprint import pprint
import sys
sys.stdin = open('input.txt')


def dfs(v):
    s = []
    res = []
    visited[v] = True
    res.append(v+1)
    for w in D[v]:
        if visited[w] == False:
            s.append(v)
            visited[w] = True
            res.append(w+1)
            break        
    while w:
        v = w
        for w in D[v]:
            if visited[w] == False:
                s.append(v)
                visited[w] = True
                res.append(w+1)
                break
        else:
            if len(s) != 0:
                w = s.pop()
            else:
                w = False
    else:
        return res


V, E = map(int, input().split())
D = [[] for _ in range(V)]
visited = [False]*V
print(visited)
for _ in range(E):
    a, b = map(int, input().split())
    D[b-1].append(a-1)
    D[a-1].append(b-1)


print(dfs(0))
