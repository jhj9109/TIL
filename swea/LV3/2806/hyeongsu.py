t = int(input())

dy = [-1, 1]
dx = [-1, -1]

def check(y, x, a, n):
    for i in range(y):
        if a[i][x]: return False

    py = y-1
    px = x-1
    while py >= 0 and px >= 0:
        if a[py][px]: return False
        py -= 1
        px -= 1

    py = y-1
    px = x+1
    while py >= 0 and px < n:
        if a[py][px]: return False
        py -= 1
        px += 1

    return True

def go(y, n, a, res):
    if y==n:
        res[0]+=1
        return
    for i in range(n):
        a[y][i]=True
        if check(y, i, a, n):
            go(y+1, n, a, res)
        a[y][i]=False

for ti in range(1, t+1):
    print(f'#{ti}', end=' ')
    n = int(input())
    a = [[False]*n for _ in range(n)]
    res = [0]
    go(0, n, a, res)
    print(res[0])