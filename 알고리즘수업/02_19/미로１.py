# import sys
# sys.stdin = open('input1266.txt')

def f(i, j):
    di = [0, 1, 0,-1]
    dj = [1, 0,-1, 0]
    if maze[i][j] == '3':
        return 1

    maze[i][j] = '1'
    for k in range(4): #상하좌우에
        ni = i + di[k]
        nj = j + dj[k]
        if maze[ni][nj] != '1': #벽이 아닌칸이 있다면
            if f(ni, nj) == 1: #이동
                return 1
    return 0

for _ in range(1, 10+1):
    tc = int(input())
    maze = [list(input()) for _ in range(16)]
    si, sj = -1, -1
    for x in range(16):
        for y in range(16):
            if maze[x][y] == '2':
                print(f(x, y))

def def(i, j):#반복버전
    s = []
    visited = [ [False]*16 for _ in range(16)]
    s.append(i)
    s.append(j)
    visited[i][j] = True #출발지
    while s:
        j = s.pop() #저장해둔 목록중 Go Go
        i = s.pop()
        if maze[i][j] == '3': #목적지에 다다르면 중단
            return 1
        for k in range(4): #4방향 서치
            ni = i +di[k]
            nj = j +dj[k]
            if maze[ni][nj] != '1' and visited[ni][nj] == False: #방문했던곳이 아니면
                s.append( (ni, nj) ) #방문할 칸 목록에 push, 갈림길 1개 -> 그 길로, 갈림길 2길 -> 저장.
                visited[ni][nj] = True
    return 0 #목적지에 도착하지 못한 경우