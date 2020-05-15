import sys
sys.stdin = open('input5209.txt')

def go(i, cnt):
    global res
    if cnt >= res:
        return
    if i == N:
        res = cnt
        return
    for j in range(N):
        if not v[j]:
            v[j] = 1
            go(i+1, cnt+c[i][j])
            v[j] = 0
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    c = [list(map(int, input().split())) for _ in range(N)] #cost
    v = [0]*N 
    res = 99 * N
    go(0, 0)
    print(f'#{tc} {res}')
