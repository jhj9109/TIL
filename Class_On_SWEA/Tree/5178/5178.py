import sys
sys.stdin = open('input5178.txt')

def go(node):
    s = [node]
    cnt = 0
    while s:
        now = s.pop()
        # 0
        if now*2 > N:
            if f[now] == None:
                return -1
            cnt += f[now]
        # 1
        elif now*2 == N:
            s.append(now*2)
        # 2
        elif now*2 <= N-1:
            s.extend([now*2,now*2+1])
    return cnt

T = int(input())
for tc in range(1, T+1):
    # 노드N개, leaf 노드 M개, 출력 노드번호 L
    N, M, L = map(int, input().split())

    f = [None]*(N+1)
    for _ in range(M):
        m, num = map(int, input().split())
        f[m] = num
    print(f'#{tc} {go(L)}')