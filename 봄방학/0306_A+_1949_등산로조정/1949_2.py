import sys
sys.stdin = open('input1949.txt')

# 점점 감소하는 수열 >>> 중복 우려 X (v : 기존의 등산로가 깍이지 않도록 보호하는 존재)

def go(r, c, possible, cnt):
    global res
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr <= N-1 and 0 <= nc <= N-1:
            if d[r][c] > d[nr][nc]:
                v[nr][nc] = True
                go(nr, nc, possible, cnt+1)
                v[nr][nc] = False
            elif possible and not v[nr][nc] and d[r][c] > d[nr][nc] - K:
                temp, d[nr][nc] = d[nr][nc], d[r][c]-1
                go(nr, nc, 0, cnt+1)
                d[nr][nc] = temp
    else:
        res = cnt if cnt > res else res

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(N)]
    v = [[False]*N for _ in range(N)]
    h = max([max(d[i])for i in range(N)])
    res = 0
    for r in range(N):
        for c in range(N):
            if d[r][c] == h:
                v[r][c] = True
                go(r, c, True, 1)
                v[r][c] = False
    print(f'#{tc} {res}')