import sys
sys.stdin = open('input.txt')
#출력값 1>>>3 2>>>3 3>>>5 4>>>15 5>>>9 6>>>14
import copy
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

def shot(X, Y, n):
    dx = [ 0,-1, 1]
    dy = [-1, 1, 1]
    cnt = 0
    if 0<=X<=N-n and 0<=Y<=M-1 and not field[X][Y]: #False : 적 >>> 해치운적 : True
        return (X,Y)
    for k in range(1, D):
        x, y = (X + dx[0]*k), (Y + dy[0]*k)

        if 0<=x<=N-n and 0<=y<=M-1 and not field[x][y]:
            return (x,y)

        for i in range(k):
            x, y = x+dx[1], y+dy[1]
            if 0<=x<=N-n and 0<=y<=M-1 and not field[x][y]:
                return (x,y)

        for i in range(k):
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
    # print(archers)
    while n != N: #n : 1~N까지 수행후 종료
        n += 1
        V = []
        for archer in archers:
            temp = shot(N-n, archer, n)
            if temp and (temp not in V):
                V.append(temp)
        res += check(V, n)
    # print(f'n:{n}')   
    return res

T = 1 #제출시 1로, 테스트시 원하는 값으로
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