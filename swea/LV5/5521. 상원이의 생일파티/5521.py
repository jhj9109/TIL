import sys
sys.stdin = open('input5521.txt')

def bfs(node):
    global cnt, f, r

    r += 1
    Q[r] = node # enQeueu
    V[node] = 1
    # cnt += 1 상원이 본인은 카운트 X

    while (f != r): # Not Empty
        f += 1
        now = Q[f]
        if V[now] >= 3:
            return
        for w in G[now]:
            if not V[w]:
                r += 1
                Q[r] = i
                V[w] = V[now]+1
                cnt += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    
    Q = [0] * (N*N)
    f = r = -1

    V = [0]*(N+1)

    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    cnt = 0
    bfs(1)
    print(f'#{tc} {cnt}')