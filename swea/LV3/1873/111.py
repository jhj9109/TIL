import sys
sys.stdin = open('input.txt')
from pprint import pprint 

def my_position(H, W, field):
    for x in range(H):
        for y in range(W):
            if field[x][y] == '^' or field[x][y] == '<' or field[x][y] == '>' or field[x][y] == 'v':
                return x, y
    print(f'오류1{x},{y}\n {field}')
    return 999, 999

def my_commend(command, x, y, H, W, field):
    if command == 'U':
        return my_move(0, x, y, H, W, field)
    if command == 'D':
        return my_move(1, x, y, H, W, field)
    if command == 'L':
        return my_move(2, x, y, H, W, field)
    if command == 'R':
        return my_move(3, x, y, H, W, field)
    if command == 'S':
        return my_shoot(4, x, y, H, W, field)

def my_shoot(command, x, y, H, W, field):
    #S:4
    #U:0 D:1 L:2 R:3
    dx = [-1, 1,  0, 0]
    dy = [ 0, 0, -1, 1]
    head = 0 if field[x][y]=='^' else 1 if field[x][y]=='v' else 2 if field[x][y]=='<' else 3

    k=1 # 1부터 점차 증가
    while (0<= x+dx[head]*k <=H-1) and (0<= y+dy[head]*k <=W-1):#경계
        if field[x+dx[head]][y+dy[head]] == '#':
            break
        if field[x+dx[head]][y+dy[head]] == '*':
            field[x+dx[head]][y+dy[head]] == '.'
            break
    return field, x, y


T = int(input())
print ('T받음')

for T in range(1):
        
    H, W = list(map(int, input().split()))
    print (f'H:{H} W:{W}받음')
    field = [list(input()) for _ in range(H)]
    print (f'F받음')
    pprint (field)
    x, y = my_position(H, W, field)
    print(f'x:{x},y:{y}')
    N = int(input())
    print (f'N:{N}받음')
    commands = [n for n in input()]
    print (f'C{commands}받음')

    z = 0
    for com in commands:
        field, x, y = my_commend(com, x, y, H, W, field)
        print ('{z}')
        z += 1
        # x, y = my_position(H, W, field)
    print(f'#{tc} ',end='')
    for i in range(H):
        print(''.join(field[i]))
    print('')

