import sys
sys.stdin = open('sample_input4875.txt')

def ret_s(data, n):
    for x in range(n):
        for y in range(n):
            if data[x][y] == 2:
                return x, y

def go(field, N, x, y):#출발
    dx = [0, 0, 1,-1]
    dy = [1,-1, 0, 0]
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    s = []
    s.append(x)
    s.append(y)
    while s:
        y = s.pop()
        x = s.pop()
        visited[x][y] = True
        if field[x][y] == 3:
            return 1

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if (0<=nx<=N-1) and (0<=ny<=N-1) and field[nx][ny] != 1 and not visited[nx][ny]:
                s.append(nx)
                s.append(ny)    
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, list(input()))) for _ in range(N)]
    #0:통로, 1:벽, 2:출발지, 3:도착지
    #sx, sy = ret_s(field, N)
    print(f'#{tc} {go(field, N, *ret_s(field, N))}')