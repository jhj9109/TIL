import sys
sys.stdin = open('input5208.txt')

def go(i, cnt):
    global res
    if cnt > v[i] or cnt >= res:
        return
    
    v[i] = cnt

    for k in range(stops[i], 0, -1):
        if i+k >= N:
            res = cnt
            return
        go(i+k, cnt+1)

T = int(input())
for tc in range(1, T+1):
    stops = list(map(int, input().split())) # N개, 1~N정류장
    res = N = len(stops)
    v = [N]*(N+1)
    go(1, 0)
    print(f'#{tc} {res}')