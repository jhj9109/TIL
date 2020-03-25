'''6:25
NxN필드
0 빈칸
1 집
2 치킨집
-----제한----
2<=N<=50, 1<=M<=13
1<=집<=2N, M<=치킨집<=13
-----목표----
M개 남기고 폐업, 치킨 거리 최소
'''

import sys
sys.stdin = open("input15686.txt")

def check():
    for r in range(N):
        for c in range(N):
            if f[r][c] == 1:
                home.append((r, c))
            elif f[r][c] == 2:
                store.append((r, c))

def sel(lst):
    global res
    if len(lst) == M:
        temp = cal(lst) #cnt
        res = temp if temp < res  else res
    else:
        templ = lst[:]
        pops = []
        for i in range(len(lst)):
            temp = templ.pop()
            sel(templ[:] + pops)
            pops.append(temp)

def cal(chicken):
    cnt = 0
    for h in home:
        temp = 2*N
        for c in chicken:
            temp2 = abs(h[0]-c[0])+abs(h[1]-c[1])
            temp = temp2 if temp2 < temp else temp
        cnt += temp
        if cnt >= res:
            return cnt
    return cnt

T = 4
for tc in range(1, T+1):    
    N, M = map(int, input().split())
    f = [list(map(int, input().split())) for _ in range(N)]
    home = []
    store = []
    check()
    res = (2*N)*(2*N) #최대거리*집
    sel(store) #치킨집수
    print(res)