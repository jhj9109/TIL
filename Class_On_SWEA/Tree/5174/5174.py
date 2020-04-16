import sys
sys.stdin = open('input5174.txt')

def go(node):
    v = [0]*(E+2)
    s = [node]
    v[node] = 1
    cnt = 0
    while s:
        now = s.pop()
        cnt += 1
        for i in range(1, E+2):
            if G[now][i] and not v[i]:
                v[i] = 1
                s.append(i)
    return cnt

T = int(input())
for tc in range(1, T+1):
    # E 간선갯수, N을 루트로하는 서브트리에 속한 노드의 갯수
    E, N = map(int, input().split())
    G = [[0]*(E+2) for _ in range (E+2)]
    
    d = list(map(int, input().split()))
    for i in range(E):
        G[d[2*i]][d[2*i+1]] = 1
    print(f'#{tc} {go(N)}')