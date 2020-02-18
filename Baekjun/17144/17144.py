'''
RxC 격자, T초후 미세먼지의 양

RxC 데이터, -1:공기청정기
'''
def diff(R, C, field, bonus):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1,  0,  1, 1, 1, 0,-1,-1]
    for x in range(R):
        for y in range(C):
            if field[x][y] != 0 and field[x][y] != -1:
                fourway_diff(R, C, x, y, bonus)
    for x in range(R):
        for y in range(C):
            field[x][y] != 0 and field[x][y] != -1:
                fourway_diff(R, C, x, y, field, bonus)
    

def fourway_diff(R, C, x, y, field, bonus):
    dx = [-1, 0, 1, 0]
    dy = [ 0, 1, 0,-1]
    cnt = 0
    for i in range(4):
        if (0<=x+dx[i]<=R) and (0<=y+dy[i]<=C) and field[x+dx[i]][y+dy[i]] != -1:
            bonus[x+dx[i]][y+dy[i]] += field[x][y]//5
            cnt += 1
    bonus[x][y] -= (field[x][y]//5)*cnt

def cycle(R, C, x1, x2, field, bonus):
    temp = 0
    for y in range(1, C-1):
        field[x1][y], field[x1][y+1], temp = temp, field[x1][y], field[x1][y+1]
    for x in range(x1, 0, -1):
        field[x][-1], field[x-1][-1], temp = temp, field[x][-1], field[x-1][-1]
    for y in range(-1, -N, -1):
        temp, field[0][y-1], field[0][y] = field[0][y-1], field[0][y], temp
    for x in range(0, x1-1):
        field[x][0], field[x+1][0], temp = temp, field[x][0], field[x+1][0]

R, C, T = input().split()
field = [list(map(int, input().split())) for _ in range(R)]
for x in range(R):
    if field[x][0] == -1:
        x1, x2 = x, x-1
t = 0
while t != T:
    t += 1
    bonus = [[0]*C for _ in range(R)]
    diff(R, C, field, bonus)
