import sys
sys.stdin = open('sample_input4881.txt')

def go(x, cnt, res):
    if cnt > res:
        return 1000000
    if x == N:
        return cnt
    for y in range(N):
        if not V[y]:
            V[y] = True
            temp = go(x+1, cnt+field[x][y], res)
            if temp < res:
                res = temp
            V[y] = False
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    V = [False] * N
    res = 1000000
    print(f'#{tc} {go(0, 0, res)}')