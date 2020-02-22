import sys
sys.stdin = open('input.txt')
import copy
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

def shot(x, y, n):
    dx = [ 0,-1, 1]
    dy = [-1, 1, 1]
    cnt = 0
    if 0<=x<=N-n and 0<=y<=M-1 and not field[x][y]: #False : 적 >>> 해치운적 : True
        return (x,y)
    if D >= 2:
        x, y = x+dx[0], y+dy[0]
        if 0<=x<=N-n and 0<=y<=M-1 and not field[x][y]:
            return (x,y)

        for i in range(D):
            x, y = x+dx[1], y+dy[1]
            if 0<=x<=N-n and 0<=y<=M-1 and not field[x][y]:
                return (x,y)

        for i in range(D):
            x, y = x+dx[2], y+dy[2]
            if 0<=x<=N-n and 0<=y<=M-1 and not field[x][y]:
                return (x,y)
    return 

def check(V, n):
    cnt = 0
    for x, y in V:
        if not field[x][y]:
            field[x][y] = True
            cnt += 1
    return cnt

def go(archers):
    res = 0
    n = 0
    V = []
    # print(archers)
    while n != N: #n : 1~N까지 수행후 종료
        n += 1
        
        for archer in archers:
            temp = shot(N-n, archer, n)
            if temp and (temp not in V):
                V.append(temp)
        res += check(V, n)
    # print(f'n:{n}')   
    return res

T = 6
for tc in range(1, T+1):
    N, M, D = map(int, input().split())
    field_origin = [list(True if x == '0' else False for x in input().split()) for _ in range(N)]
    data = getSubset(list(range(M)))
    result = 0
    for archers in data:
        field = copy.deepcopy(field_origin)
        temp = go(archers)
        result = temp if temp > result else result
    print(result)