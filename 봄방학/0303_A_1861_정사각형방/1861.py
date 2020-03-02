import sys
sys.stdin = open('input1861.txt')
'''
4:39~5:03
좌표(i,j) 1~N^2
+1 >>> 얼마나 많이
'''
def go(x, y):
    s = [(x, y)]
    ret = [field[x][y], 0]
    while s:
        x, y = s.pop()
        if not visited[x][y]:
            visited[x][y] = True
            ret[1] += 1
            ret[0] = min( ret[0], field[x][y] )
            for k in range(4): 
                if abs(field[x+dx[k]][y+dy[k]] - field[x][y]) == 1:
                    s.append((x+dx[k], y+dy[k]))
    return ret

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
            temp = go(x, y)
            if res[1] < temp[1]:
                res = temp
            if res[1] == temp[1]:
                res[0] = temp[0] if temp[0] < res[0] else res[0]
    print(f'#{tc} {res[0]} {res[1]}')