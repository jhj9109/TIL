import sys
sys.stdin = open('input15684.txt')

def game(cnt):
    global res
    for c in range(1, N+1):
        now = c
        for r in range(H):
            if bridge[r][now-1]:
                now -= 1
            elif bridge[r][now]:
                now += 1
        if now != c:
            return
    res = cnt

def sim_dfs(col, row, cnt):
    if cnt >= res:
        return
    game(cnt)

    # 해당 col의 모든 row에 새로운 다리를 놓는다
    for c in range(col, N):
        start = row if c == col else 0
        for r in range(start, H):
            if not bridge[r][c-1] and not bridge[r][c] and not bridge[r][c+1]:
                bridge[r][c] = 1
                sim_dfs(c, r, cnt+1)
                bridge[r][c] = 0
T = 7
for tc in range(1, T+1):
    N, M, H = map(int, input().split())

    bridge = [[0]*(N+2) for _ in range(H)]

    for _ in range(M):
        a, b = map(int, input().split())
        bridge[a-1][b] = 1

    res = 4

    sim_dfs(1, 0, 0)

    print(-1 if res == 4 else res)