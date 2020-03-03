import sys
sys.stdin = open('input1861.txt')
'''
28번째 케이스 추가 (N=1000, 최대 이동횟수 십만)
문제 조건 읽기 - 상하좌우 이동. 모든 숫자는 다르다
N:1000, NxN인 경우 10만칸 이동 가능
재귀 호출 : python3 : 1000, pypy3.6 : 2300이 최대
재귀함수 사용 불가!
이번문제에서 주어진 입력데이터는 이동한 방이 최대 2200 & pypy라 가능했음 
-------------------------------------------------------------------
abs 활용한 양쪽 퍼지기 >>> 유일한 경로 >>> not visited 활용가능
한쪽 퍼지기 >>> 234 > 1234 가능하므로, 함수 호출전 출발지만 not visited 검사 
'''
def go(x, y, res):
    s = [(x, y)]
    temp = [field[x][y], 0]
    while s:
        x, y = s.pop()
        visited[x][y] = True
        temp[1] += 1
        temp[0] = min( temp[0], field[x][y] )
        for k in range(4): 
            nx, ny = x+dx[k], y+dy[k]
            if not visited[nx][ny] and abs(field[nx][ny] - field[x][y]) == 1:
                s.append((nx, ny))
    if res[1] < temp[1]:
        res[0], res[1] = temp[0], temp[1]
    elif res[1] == temp[1] and temp[0] < res[0]:
        res[0] = temp[0]

dx = [0, 0, 1,-1]
dy = [1,-1, 0, 0]
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    field = [ [-1] * (N+2) ]
    field.extend([ [-1] + list(map(int, input().split())) + [-1] for _ in range(N)] )
    field.append([-1]*(N+2))
    visited = [ [False]*(N+2) for _ in range(N+2) ]
    res = [N**2, 0] # 출발 방 넘버, 최대이동횟수
    for x in range(1, N+1):
        for y in range(1, N+1):
            if not visited[x][y]:
                go(x, y, res)
    print(f'#{tc} {res[0]} {res[1]}')