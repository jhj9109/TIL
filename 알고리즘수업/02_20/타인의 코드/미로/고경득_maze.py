T = int(input())
for tc in range(1, T+1):
    width = int(input())
    maze = []
    for _ in range(width):
        maze.append(list(map(int, list(input()))))
    for w in range(width):
        if 2 in maze[w]:
            sx = w
            sy = maze[w].index(2)
        if 3 in maze[w]:
            ax = w
            ay = maze[w].index(3)

    dx = [-1, 1, 0, 0]
    dy = [0, 0 , -1, 1]
    
    stack = [[sx, sy]]
    while stack:
        x, y = stack.pop()
        if maze[x][y] == 3:
            print(f'#{tc} 1')
            break
        maze[x][y] = 1
        for i in range(4):
            if 0 <= x+dx[i] < width and 0 <= y+dy[i] < width:
                if maze[x+dx[i]][y+dy[i]] == 0 or maze[x+dx[i]][y+dy[i]] == 3:
                    stack.append([x+dx[i], y+dy[i]])
    else:
        print(f'#{tc} 0')