import sys
sys.stdin = open('input1226.txt')

def go2(field, x, y): #메인 함수
    #좌/우/상/하
    dx = [ 0, 0,-1, 1]
    dy = [-1, 1, 0, 0]
    for k in range(4): #4방향 서치
        if 0<=x+dx[k]<=15 and 0<=y+dy[k]<=15: #경계조건

            if field[x+dx[k]][y+dy[k]] == 3: #도착하면
                return 1

            elif field[x+dx[k]][y+dy[k]] == 0: #길이면  
                field[x+dx[k]][y+dy[k]] = 1 #길을 잠시 닫음

                if go2(field, x+dx[k], y+dy[k]): #go
                    return 1
                field[x+dx[k]][y+dy[k]] = 0 #길을 다시 복구
    else:
        return 0

def return_start(field): #시작점, 종료점 반환
    for x in range(16):
        for y in range(16):
            if field[x][y] == 2:
                return x, y

T = 10
for _ in range(1, T+1):
    tc = int(input())
    field = [list( int(x) for x in input() ) for _ in range(16)]
    x1, y1 = return_start(field) #시작점
    
    print(f'#{tc} {go2(field, x1, y1)}')
