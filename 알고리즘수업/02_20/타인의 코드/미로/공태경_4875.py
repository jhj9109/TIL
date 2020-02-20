dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x,y):
    Possible = 0
    Queue = list()
    check[x][y] = 1
    Queue.append([x,y])

    while Queue:

        cx, cy = Queue.pop(0)
        if data[cx][cy] == 3:
            Possible = 1

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (0 <= nx < N) and (0 <= ny < N):
                if not check[nx][ny] and data[nx][ny] == 0 or data[nx][ny] == 3:
                    Queue.append([nx,ny])
                    check[nx][ny] = 1
    return Possible
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int,list(input()))) for _ in range(N)]
    check = [[0]*N for _ in range(N)]
    start = [[i,j] for i in range(N) for j in range(N) if data[i][j] == 2]
    x = start[0][0]
    y = start[0][1]
    result = BFS(x,y)
    print('#{} {}'.format(tc,result))