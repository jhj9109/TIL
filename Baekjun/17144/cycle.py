def cycle_diff(R, C, x1, x2, field):
    # 우 / 상 / 좌 / 하
    dx = [0, -1, 0, 1]
    dy = [1,  0,-1, 0]
    repeat= [C-1, x1, C-1, x1-1]
    temp = 0
    x, y = x1, 0
    for k in range(4):
        for idx in range(repeat[k]):
            field[x+dx[k]][y+dy[k]], temp = temp, field[x+dx[k]][y+dy[k]]
            x, y = x+dx[k], y+dy[k]
    # 우 / 하 / 좌 / 상
    dx = [0,  1, 0,-1]
    dy = [1,  0,-1, 0]
    repeat= [C-1, R-(x2+1), C-1, R-(x2+2)]
    temp = 0
    x, y = x2, 0
    for k in range(4):
        for idx in range(repeat[k]):
            field[x+dx[k]][y+dy[k]], temp = temp, field[x+dx[k]][y+dy[k]]
            x, y = x+dx[k], y+dy[k]