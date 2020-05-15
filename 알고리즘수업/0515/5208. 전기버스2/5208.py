import sys
sys.stdin = open('input5208.txt')

def go(i, cnt):
    global res
    if cnt > res:
        return

    for k in range(d[i], 0, -1):
        if i+k >= N:
            res = cnt
            return
        go(i+k, cnt+1)

T = int(input())
for tc in range(1, T+1):
    d = list(map(int, input().split()))
    N = len(d)
    res = N
    go(1, 0)
    print(f'#{tc} {res}')