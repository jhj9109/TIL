'''
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

# import sys
# sys.stdin = open("input15686.txt")
import sys
input = sys.stdin.readline

def check():
    for r in range(N):
        for c in range(N):
            if f[r][c] == 1:
                home.append((r, c))
            elif f[r][c] == 2:
                store.append((r, c))

def sel(n, lst):
    if lst and len(lst) == M:
        cal(lst)
    elif n < len(store):
        sel(n+1, lst+[store[n]])
        sel(n+1, lst)

def cal(chicken):
    global res
    cnt = 0
    for h in home:
        temp = 2*N
        for c in chicken:
            temp2 = abs(h[0]-c[0])+abs(h[1]-c[1])
            temp = temp2 if temp2 < temp else temp
        cnt += temp
        if cnt >= res:
            return
    res = cnt
    return

T = 1
for tc in range(1, T+1):    
    N, M = map(int, input().split())
    f = [list(map(int, input().split())) for _ in range(N)]
    home = []
    store = []
    check()
    res = (2*N)*(2*N)
    sel(0, [])
    print(res)