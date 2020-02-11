def my_paint(f, N, d):
    x1, y1, x2, y2 = d[0], d[1], d[0]+d[2]-1, d[1]+d[3]-1
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            f[x][y] = N
    return f

def my_print(d, N):
    res = 0
    for x in range(101):
        for y in range(101):
            res += 1 if d[x][y] == N else 0
    return res

N = int(input())
f = [[0]*101 for _ in range(101)]
for n in range(1, N+1):
    f = my_paint(f, n, list(map(int, input().split())))
for n in range(1, N+1):
    print(my_print(f, n))