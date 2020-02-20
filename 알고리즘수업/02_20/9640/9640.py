import sys
sys.stdin = open('sample9640.txt')

def go(x, y, n):
    dx = [0, 0, 1,-1]
    dy = [1,-1, 0, 0]
    if n == target:
        return True

    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<=N-1 and 0<=ny<=N-1 and field[nx][ny] == data[n+1] and V[nx][ny] == False:
            V[nx][ny] = True
            if go(nx, ny, n+1):
                return True
            V[nx][ny] = False
    return False

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    target = data[0]
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    V = [ [False] * N for _ in range(N) ]
    flag =True
    for a in range(N):
        for b in range(N):
            if field[a][b] == data[1]:
                V[a][b] = True
                if go(a, b, 1):
                    print('#{} 1'.format(tc))
                    flag = False
                V[a][b] = False
    if flag:
        print('#{} 0'.format(tc))