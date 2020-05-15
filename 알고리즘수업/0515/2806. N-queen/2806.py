import sys
sys.stdin = open('input2806.txt')

def go(n, l, m, r):
    global res
    if n == N:
        res += 1
        return
    l = [x-1 for x in l if x-1 >= 0]
    r = [x+1 for x in r if x+1 < N]
    for i in range(N):
        if i not in l+m+r:
            go(n+1, l+[i], m+[i], r+[i])
    return     


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    res = 0
    go(0, [], [], [])
    print(f'#{tc} {res}')
