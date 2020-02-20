dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def DFS(y, x, end, a, c, res):
    
    if y == end[0] and x == end[1]:
        res[0] = 1
        return
    
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<len(a) and 0<=nx<len(a) and a[ny][nx]!='1' and not c[ny][nx]:
            c[ny][nx]=True
            DFS(ny, nx, end, a, c, res)
            c[ny][nx]=False
        
        


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    a = [list(input()) for _ in range(n)]
    c = [[False]*n for _ in range(n)]
    
    start = [0,0]
    end = [0,0]
    res = [0]
    
    for i in range(n):
        for j in range(n):
            if a[i][j] == '2':
                start[0], start[1] = i, j
            elif a[i][j] == '3':
                end[0], end[1] = i, j
    DFS(start[0], start[1], end, a, c, res)
    
    print('#{} {}'.format(tc, res[0]))