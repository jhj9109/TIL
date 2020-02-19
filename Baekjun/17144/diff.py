def diff(R, C, field, bonus):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1,  0,  1, 1, 1, 0,-1,-1]
    for x in range(R):
        for y in range(C):
            if field[x][y] != 0 and field[x][y] != -1:
                diff_fourway(R, C, x, y, field, bonus)
    diff_add(field, bonus)

def diff_fourway(R, C, x, y, field, bonus):
    dx = [-1, 0, 1, 0]
    dy = [ 0, 1, 0,-1]
    cnt = 0
    for i in range(4):
        if (0<=x+dx[i]<=R-1) and (0<=y+dy[i]<=C-1) and field[x+dx[i]][y+dy[i]] != -1:
            bonus[x+dx[i]][y+dy[i]] += field[x][y]//5
            cnt += 1
    bonus[x][y] -= (field[x][y]//5)*cnt

def diff_add(field, bonus):
    for x in range(R):
        for y in range(C):
            field[x][y] += bonus[x][y]