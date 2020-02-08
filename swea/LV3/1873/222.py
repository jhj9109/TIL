def my_position(H, W, field):
    for x in range(H):
        for y in range(W):
            if field[x][y] == '^' or field[x][y] == '<' or field[x][y] == '>' or field[x][y] == 'v':
                return x, y

def my_commend(com, x, y, H, W, field):
    return_com={ 'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3, 'S' : 4 }
    if com == 'S':
        return my_shoot(return_com[com], x, y, H, W, field)
    else:
        return my_move(return_com[com], x, y, H, W, field)

def my_move(command, x, y, H, W, field):
    #U:0 D:1 L:2 R:3
    #c =  [ 0, 1,  2, 3]
    dx = [-1, 1,  0, 0]
    dy = [ 0, 0, -1, 1]
    heading = { 0 : '^', 1 : '∨', 2 : '<', 3 : '>' }
    
    if not(0<= x+dx[command] <=H-1) or not(0<= y+dy[command] <=W-1):#경계초과시
        field[x][y] == heading[command]
        return field, x, y
    elif field[x+dx[command]][y+dy[command]] != '.':#평지가 아니면
        field[x][y] == heading[command]
        return field, x, y
    else:
        field[x][y], field[x+dx[command]][y+dy[command]] == '.', heading[command]
        return field, x+dx[command], y+dy[command]

def my_shoot(command, x, y, H, W, field):
    #S:4
    #U:0 D:1 L:2 R:3
    dx = [-1, 1,  0, 0]
    dy = [ 0, 0, -1, 1]
    head = 0 if field[x][y]=='^' else 1 if field[x][y]=='v' else 2 if field[x][y]=='<' else 3

    k=1 # 1부터 점차 증가

    while (0<= x+dx[head]*k <=H-1) and (0<= y+dy[head]*k <=W-1):#경계
        if field[x+dx[head]][y+dy[head]] == '#':
            return field, x, y
        if field[x+dx[head]][y+dy[head]] == '*':
            field[x+dx[head]][y+dy[head]] == '.'
            return field, x, y
        k += 1
    return field, x, y

T = int(input())

for tc in range(1, T+1):
    H, W = (map(int, input().split()))
    field = [list(input()).strip() for _ in range(H)]
    x, y = my_position(H, W, field)
    N = int(input())
    commands = input()
    print(f'com:{commands}')
    for com in commands:
        field, x, y = my_commend(com, x, y, H, W, field)
    print(f'#{tc} ',end='')
    for i in range(H):
        print(''.join(field[i]))