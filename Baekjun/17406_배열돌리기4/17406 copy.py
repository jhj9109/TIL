import sys
sys.stdin = open('input17406.txt')

'''6:17 ~7:30
3<= N, M <= 50
1 <= K <= 6
1 <= A[i][j] <= 100
1 <= s
1 <= r-s < r < r+s <= N
1 <= c-s < c < c+s <= M
-------------------------
NxM 배열A, 값 각 행에 있는 모든 수의 최솟값
-----------회전연산------------------------
r, c, s
r,c ±s

'''
from pprint import pprint
def go(data):
    global res
    # 기존 데이터 변형 막기 위한 카피
    nA = [[A[i][j] for j in range(M+2)] for i in range(N+2)]

    for d in data:
        r, c, s = d[0], d[1], d[2]
        while s:
            # (R,C)의 값을 (nR,nC)에 저장하며,
            # 동시에 (nR,nC)의 본래 값은 temp에 잠시 저장한다.
            R, C = r-s, c-s
            temp = nA[R][C]
            for k in range(4):    
                for n in range(2*s):
                    nR, nC = R+dr[k], C+dc[k]
                    temp, nA[nR][nC] = nA[nR][nC], temp
                    R, C = nR, nC
            s -= 1
    temp = min( sum(nA[i]) for i in range(1, N+1) )
    res = temp if temp < res else res

def sel(lst):
    if len(lst) == K:
        go(lst)
    else:
        for i in range(K):
            if B[i] not in lst:
                sel( lst + [B[i]] )

dr = [0, 1, 0,-1]
dc = [1, 0,-1, 0]
T = 1
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    A = [[0]*(M+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]
    B = [list(map(int, input().split())) for _ in range(K)]
    res = 100*M

    for i in range(K):
        sel([B[i]])
    print(res)
