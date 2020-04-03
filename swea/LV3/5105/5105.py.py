import sys
sys.stdin = open("input5105_2.txt")
'''
0: 통로
1: 벽
2: 출발
3: 도착
'''
def go(start):
    v = [list(0 for _ in range(N)) for _ in range(N)]
    q = [start]
    v[start[0]][start[1]] = 1
    while q:
        x, y = q.pop(0)
        if field[x][y] == '3':
            return v[x][y]-2
        else:
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<N and 0<=ny<N and field[nx][ny] != '1' and not v[nx][ny]:
                    q.append((nx, ny))
                    v[nx][ny] = v[x][y] + 1
    return 0

def ret_start():
    for x in range(N):
        for y in range(N):
            if field[x][y] == '2':
                return x, y

dx = [0, 0, 1,-1]
dy = [1,-1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(input()) for _ in range(N)]
    print(f'#{tc} {go(ret_start())}')