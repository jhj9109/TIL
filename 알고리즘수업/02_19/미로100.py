# import sys
# sys.stdin = open('input.txt')

def go(x, y):#반복버전
    dx = [0, 0, 1,-1]
    dy = [1,-1, 0, 0]
    s = []
    visited = [ [False]*100 for _ in range(100)]
    s.append(x)
    s.append(y)
    visited[x][y] = True #출발지
    while s:
        y = s.pop() #저장해둔 목록중 Go Go
        x = s.pop()
        if field[x][y] == 3: #목적지에 다다르면 중단
            return 1
        for k in range(4): #4방향 서치
            if field[x+dx[k]][y+dy[k]] != 1 and visited[x+dx[k]][y+dy[k]] == False: #방문했던곳이 아니면
                s.append( (x+dx[k], y+dy[k]) ) #방문할 칸 목록에 push, 갈림길 1개 -> 그 길로, 갈림길 2길 -> 저장.
                visited[x+dx[k]][y+dy[k]] = True
    return 0 #목적지에 도착하지 못한 경우

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    field = [list(int(x) for x in input()) for _ in range(100)]
    flag = False
    for x in range(100):
        for y in range(100):
            if field[x][y] == 2:
                print('#{} {}'.format((tc, go(x,y))))
                flag = True
            if flag:
                break
        if flag:
            break
