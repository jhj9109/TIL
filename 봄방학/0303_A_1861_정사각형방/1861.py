import sys
sys.stdin = open('input1861.txt')
'''
4:39~5:03
좌표(i,j) 1~N^2
+1 >>> 얼마나 많이
'''
def go(X,Y):
    x, y = X, Y
    global N
    global rx, ry, rv
    cnt = 1
    while True:
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<=N-1 and 0<=ny<=N-1 and field[nx][ny] - field[x][y] == 1:
                x, y = nx, ny
                cnt += 1
                break
        else:
            if cnt > rv or (cnt == rv and field[X][Y] < field[rx][ry]):
                rv = cnt
                rx, ry, rv = X, Y, cnt
                return
            else:
                return

dx = [0, 0, 1,-1]
dy = [1,-1, 0, 0]
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    rx, ry, rv = -1, -1, -1
    for x in range(N):
        for y in range(N):
            go(x,y)
    print(f'#{tc} {field[rx][ry]} {rv}')