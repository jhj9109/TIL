import sys
sys.stdin = open('input.txt')
from pprint import pprint
'''
.평지 -물
*벽돌 #강철
^<>v
------입력---
U D L R : 방향회전, 평지라면 전진
S : 바라보고 있는 방향 포탄
포탄 >>> 벽or 경계 >>> 벽돌 파괴
'''
def my_position(H, W, field):
    for x in range(H):
        for y in range(W):
            if field[x][y] == '^' or field[x][y] == '<' or field[x][y] == '>' or field[x][y] == 'v':
                return x, y
    print(f'오류1{x},{y}\n {field}')
    return False, False

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
    


def my_move(command, x, y, H, W, field):
    #U:0 D:1 L:2 R:3 S:4
    #c =  [ 0, 1,  2, 3]
    dx = [-1, 1,  0, 0]
    dy = [ 0, 0, -1, 1]

    if not(0<= x+dx[command] <=H-1) or not(0<= y+dy[command] <=W-1):#경계초과시
        field[x][y] == '^'
        return field, x, y
    elif field[x+dx[command]][y+dy[command]] != '.':#평지가 아니면
        field[x][y] == '^'
        return field, x, y
    else:
        field[x][y], field[x+dx[command]][y+dy[command]] == '.', '^'
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
            break
        if field[x+dx[head]][y+dy[head]] == '*':
            field[x+dx[head]][y+dy[head]] == '.'
    return field, x, y

T = int(input())
print ('T받음')

for tc in range(1, T+1):
    H, W = list(map(int, input().split()))
    print (f'H:{H} W:{W}받음')
    field = [list(input()) for _ in range(H)]
    print (f'F받음')
    pprint (field)
    N = int(input().strip())
    print (f'N:{N}받음')
    comman = input('야 들어와').strip()
    print (f'받음')

    x, y = my_position(H, W, field)
    z = 0
    for com in comman:
        field, x, y = my_commend(com, x, y, H, W, field)
        print ('{z}')
        z += 1
        # x, y = my_position(H, W, field)
    print(f'#{tc} ',end='')
    for i in range(H):
        print(''.join(field[i]))
    print('')