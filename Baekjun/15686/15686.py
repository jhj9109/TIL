'''6:25~7:15 예제4 실패
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
    cnt = 0
    for r in range(N):
        for c in range(N):
            cnt += 1 if f[r][c]==2 else 0
    return cnt

def sel(n):
    global res
    if n == M:
        temp = cal()
        res = temp if temp < res else res
    else:
        for r in range(N):
            for c in range(N):
                if f[r][c] == 2:
                    f[r][c] = 0
                    sel(n-1)
                    f[r][c] = 2
def cal():
    cnt = 0
    for r in range(N):
        for c in range(N):
            if f[r][c] == 1:
                cnt += cal2(r, c)
                if cnt >= res:
                    return cnt
    return cnt

def cal2(ori_r, ori_c):
    s = [(ori_r, ori_c)]
    v = []
    while s:
        r, c = s.pop(0)
        for dr, dc in [(0,1), (0,-1), (1, 0), (-1, 0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N:
                if f[nr][nc] == 2:
                    return abs(ori_r-nr) + abs(ori_c-nc)
                else:
                    if (nr, nc) not in v:
                        s.append((nr,nc))
                        v.append((nr,nc))

T = 4
for tc in range(1, T+1):    
    N, M = map(int, input().split())
    f = [list(map(int, input().split())) for _ in range(N)]
    res = (2*N)*(2*N) #최대거리*집
    sel( check() ) #치킨집수
    print(res)