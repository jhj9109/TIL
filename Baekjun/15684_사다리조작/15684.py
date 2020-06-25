import sys
sys.stdin = open('input15684.txt')
sys.setrecursionlimit(3000) 
def game(cnt):
    global res
    for c in range(1, N+1):
        now = c
        for r in range(H):
            if bridge[r][now-1]:
                now -= 1
            elif bridge[r][now]:
                now += 1
            # else: now = now
        if now != c:
            return
    res = cnt

def sim(col, row, cnt):
    if cnt >= res:
        return
    game(cnt)

    # 해당 col의 모든 row에 새로운 다리를 놓는다
    for c in range(col, N):
        for r in range(H):
            if (c > col or r > row) and not bridge[r][c-1] and not bridge[r][c] and not bridge[r][c+1]:
                bridge[r][c] = 1
                sim(c, r, cnt+1)
                bridge[r][c] = 0
                sim(c, r, cnt)


T = 7
for tc in range(1, T+1):
    N, M, H = map(int, input().split())

    bridge = [[0]*(N+2) for _ in range(H)]

    for _ in range(M):
        # a:row, b:column
        a, b = map(int, input().split())
        bridge[a-1][b] = 1

    res = float('inf')

    # 1번 세로줄부터 가능한 다리 모두 놓는다 => 재귀

    sim(1, 0, 0)

    res = -1 if res == float('inf') else res
    print(f'{res}')

