import sys
sys.stdin = open('input5209.txt')

def go(N, c):
    s = [ ( {n}, c[0][n]) for n in range(N) ] # 단계, 값
    res = 99 * N
    while s:
        u, cnt = s.pop()
        i = len(u)
        if cnt >= res:
            continue
        if i == N:
            res = cnt
            continue
        for j in set(range(N))-u:
            s.append( (u.union({j}) , cnt + c[i][j]) )
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    c = [list(map(int, input().split())) for _ in range(N)] #cost
    print(f'#{tc} {go(N, c)}')