import sys
sys.stdin = open('input5102.txt')

def go(S, G):
    v = [0]*(V+1)
    q = [S]
    v[S] = 1
    while q:
        now = q.pop(0)
        if now == G:
            return v[now] - 1
        else:
            for w in d[now]:
                if not v[w]:
                    q.append(w)
                    v[w] = v[now] + 1
    
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) #V:노드수, E:간선수
    d = [[] for _ in range(V+1)]

    for _ in range(E): #간선수만큼
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)

    S, G = map(int, input().split()) #S:출발지, G:도착지
    print(f'#{tc} {go(S, G)}')