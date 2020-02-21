import sys
sys.stdin = open('input.txt')# 출력값은 1과 57
'''
1 내 자리 청소
2 좌측 : O >>> 회전및 이동
3 좌측 : X >>> 회전 until 4방향서치
4 4방향서치 실패 & 후진 가능 : 후진
5 4방향서치 실패 & 후진 가능 : 후진
'''
def check_4(x, y, h):
    dx = [-1, 0, 1, 0]
    dy = [ 0, 1, 0,-1]
    #    북0 동1 남2 서3 >>> 좌회전 == +3
    nh = h
    for _ in range(4):
        nh = (nh+3) % 4 
        nx, ny = x+dx[nh], y+dy[nh]
        if field[nx][ny] == '0':    #빈칸0 벽1 청소한평지2
            return nx, ny, nh       #nh, nx, ny : 새로운 방향, 나아갈 위치
    else:
        return False

def check_back(x, y, h):
    dx = [-1, 0, 1, 0]
    dy = [ 0, 1, 0,-1]
    nh = (h+2) % 4
    nx, ny = x+dx[nh], y+dy[nh]
    if field[nx][ny] != '1':
        return nx, ny, h #후진, 방향 유지
    else:
        return False#프로그램종료

def go(x, y, h):
    cnt = 0
    while True:
        if field[x][y] == '0':
            field[x][y] = '2'
            cnt += 1
        temp = check_4(x, y, h)
        if temp:
            x, y, h = temp
        else:
            temp = check_back(x, y, h)
            if temp:
                x, y, h = temp
            else:
                return cnt

T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split()) #세로, 가로
    r, c, d = map(int, input().split()) #(r,c) 방향 북0 동1 남2 서3
    field = [list(input().split()) for _ in range(N)] #빈칸0 벽1 청소한평지2
    print( go(r, c, d) )