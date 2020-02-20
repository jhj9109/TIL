def BT(col,row):
    global s
    global m
    if s >= m:
        return
    if col == N:
        if m > s:
            m = s
    for row in range(N):
        if not check[row]:
            check[row] = 1
            s += d[col][row]
            col += 1
            BT(col,row)
            col -= 1
            s -= d[col][row]
            check[row] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int,input().split())) for _ in range(N)]
    check = [0]*N
    m = 100000000
    s = 0
    BT(0,0)
    print('#{} {}'.format(tc,m))