import copy
import sys
sys.stdin = open('input.txt')
# 1>>>3 2>>>3 3>>>5 4>>>15 5>>>9 6>>>14
'''
거리 = 좌표차이합
궁수 3
N,M : 3~15
사거리D : 1~10  
-------------
탐색
궁수 위치
1. 바로 윗자리 탐색
2. 점점 퍼저나감
3. 가장 왼쪽을 타겟으로 탐색
코드화
1. 한 자리 찝는다 
2. 왼쪽을 찝는다 1 >>> 1 , 2 >>> 1
3. 우상향 진행한다 1 >>> 1 , 2 >>> 2
4. 우하향 진행한다. 1 >>> 1 , 2 >>> 2

'''

def getSubset(lst):
    n = len(lst)
    ret = []
    for i in range(1<<n):
        temp = []
        for j in range(n):
            t_f = i & (1 << j)
            if t_f:
                temp.append(lst[j])
            if len(temp) > 3:
                break
        else:
            if len(temp) == 3:
                ret.append(temp)
    return ret

def shot(x, y):
    dx = [ 0,-1, 1]
    dy = [-1, 1, 1]
    cnt = 0
    if field[x][y] == 2:
        return 0
    if field[x][y]:
        field[x][y] = 2
        return 1
    if D >= 2:
        x, y = x+dx[0], y+dy[0]
        if 0<=x<=N-1 and 0<=y<=M-1:
            if field[x][y] == 2:
                return 0
            if field[x][y]:
                field[x][y] = 2
                return 1

        for i in range(D):
            x, y = x+dx[1], y+dy[1]
            if 0<=x<=N-1 and 0<=y<=M-1:
                if field[x][y] == 2:
                    return 0
                if field[x][y]:
                    field[x][y] = 2
                    return 1

        for i in range(D):
            x, y = x+dx[2], y+dy[2]
            if 0<=x<=N-1 and 0<=y<=M-1:
                if field[x][y] == 2:
                    return 0
                if field[x][y]:
                    field[x][y] = 2
                    return 1
    return 0

def check(n):
    for x in range(N-n):
        for y in range(M):
            if field[x][y] == 2:
                field[x][y] = False
    return False

def go(archers):
    res = 0
    n = 0
    while n != N: #n=N까지 수행후 종료
        n += 1 #1~N
        for archer in archers:
            res += shot(N-n, archer)
        if check(n):
            break
    # print(f'n:{n}')
    return res

T = 6
for tc in range(1, T+1):
    N, M, D = map(int, input().split())
    field_origin = [list(False if x == '0' else True for x in input().split()) for _ in range(N)]
    data = getSubset(list(range(M)))
    result = 0
    for archers in data:
        field = copy.deepcopy(field_origin)
        temp = go(archers)
        result = temp if temp > result else result
    print(f'{result}')