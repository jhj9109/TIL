import sys
input = sys.stdin.readline
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

def sum_diff(field):
    res = 0
    for x in range(R):
        for y in range(C):
            res += field[x][y]
    return res

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
    
R, C, T = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(R)]
X = []
for x in range(R):
    if field[x][0] == -1:
        X.append(x)
t = 0
while t != T:
    t += 1
    bonus = [[0]*C for _ in range(R)]
    diff(R, C, field, bonus)
    cycle(R, C, X[0], X[1], field)

print(sum_diff(field)+2)