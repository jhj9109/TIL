def my_setting(N, data):
    data[(N//2) - 1][(N//2) - 1] = 2
    data[(N//2) - 1][(N//2) - 0] = 1
    data[(N//2) - 0][(N//2) - 1] = 1
    data[(N//2) - 0][(N//2) - 0] = 2
    return data

def my_place(X, Y, C, data):
    data[X][Y] = C
    return data

def my_8_check(X, Y, C, N, data):
    dx = [-1,  0,  1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1,  1,  0]
    target = 1 if C == 2 else 2
    for i in range(8):
        if 0 <= X + dx[i] <= N-1 and 0 <= Y + dy[i] <= N-1:
            j = 1
            while data[ X + dx[i]*j  ][ Y + dy[i]*j  ] == target :

                j += 1
                if not (0 <= X + dx[i]*j <= N-1 and 0 <= Y + dy[i]*j <= N-1):
                    break
                if data[ X + dx[i]*j  ][ Y + dy[i]*j  ] == 0:
                    break
                if data[ X + dx[i]*j  ][ Y + dy[i]*j  ] == C: 
                    for k in range(1, j):
                        data[ X + dx[i] * k  ][ Y + dy[i] * k  ] = C
                    break
    return data

import sys
sys.stdin = open('input.txt')    
        
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = [[0]*N for _ in range(N)]
    field = my_setting(N, field)
    for n in range(1, M+1):
        X, Y, C = map(int, input().split())
        field = my_place(X-1, Y-1, C, field)
        field = my_8_check(X-1, Y-1, C, N, field)
    cnt_1_B, cnt_2_W = 0, 0
    for y in range(N):
        for x in range(N):
            if field[y][x] == 1:
                cnt_1_B += 1
            if field[y][x] == 2:
                cnt_2_W += 1
    print(f'#{tc} {cnt_1_B} {cnt_2_W}')