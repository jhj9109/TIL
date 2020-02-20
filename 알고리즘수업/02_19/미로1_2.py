import sys
sys.stdin = open('input1226.txt')
'''
중간에 실패했던 이유
미로를 안 닫고 & 3방향 서치하는 코드로 바꿈
visited를 사용 안하기 때문에 갔던길 계속 감
이전에는 길을 닫았기 때문에 괜찮았음
>>>visited 사용하는 4방향 서치로 바꾸어 해결
>>>*
'''
def return_start(field): #시작점
    for x in range(16):
        for y in range(16):
            if field[x][y] == 2:
                return x, y

def go(field, x, y): #메인 함수
    visited[x][y] = True
    if field[x][y] == 3:
        return 1
    dx = [ 0, 0,-1, 1]
    dy = [-1, 1, 0, 0]
    for k in range(4): #4방향 서치
        if 0<=x+dx[k]<=15 and 0<=y+dy[k]<=15: #경계조건
            if field[x+dx[k]][y+dy[k]] != 1 and not visited[x+dx[k]][y+dy[k]]: #if 벽이 아니야? and 갔던길빼고
                if go(field, x+dx[k], y+dy[k]): #go
                    return 1
    return 0

T = 10
for _ in range(1, T+1):
    tc = int(input())
    field = [list( int(x) for x in input() ) for _ in range(16)]
    visited = [[False]*16 for _ in range(16)]
    #x1, y1 = return_start(field) #시작점(사용)
   
    print(f'#{tc} {go(field, *return_start(field))}')