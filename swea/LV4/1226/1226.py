import sys
sys.stdin = open('input1226.txt')
def return_start_end(field): #시작점, 종료점 반환
    x1, y1, x2, y2 = 0, 0, 0, 0
    for x in range(16):
        for y in range(16):
            if field[x][y] == 2:
                x1, y1 = x, y
            if field[x][y] == 3:
                x2, y2 = x, y
    return x1, y1, x2, y2

def go(field, x, y, res): #메인 함수
    #좌/우/상/하
    dx = [ 0, 0,-1, 1]
    dy = [-1, 1, 0, 0]
    for k in range(4): #4방향 서치
        if 0<=x+dx[k]<=15 and 0<=y+dy[k]<=15: #경계조건
            if field[x+dx[k]][y+dy[k]] == 0: #길이면

                field[x+dx[k]][y+dy[k]] = 1 #길을 잠시 닫음

                go(field, x+dx[k], y+dy[k], res) #go

                field[x+dx[k]][y+dy[k]] = 0 #길을 다시 복구

            elif field[x+dx[k]][y+dy[k]] == 3: #종료도착 >>> 출력 res[0] = 1
                res[0] = 1
                return


T = 10
for _ in range(1, T+1):
    tc = int(input())
    field = [list( int(x) for x in input() ) for _ in range(16)]
    x1, y1, x2, y2 = return_start_end(field) #시작점(사용), 도착점(사용안함) 
    
    res = [0] #도착점 못 찾으면 출력 res[0] = 0
    go(field, x1, y1, res)
    print(f'#{tc} {res[0]}')
