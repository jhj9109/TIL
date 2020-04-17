import sys
import itertools
# input = sys.stdin.readline
sys.stdin = open('input17406.txt')

def go(data):
    global res
    # 기존 데이터 변형 막기 위한 카피
    nA = [[A[i][j] for j in range(M)] for i in range(N)]

    for d in data:
        r, c, s = d[0]-1, d[1]-1, d[2]
        while s:
            # (R,C)의 값을 (nR,nC)에 저장하며,
            # 동시에 (nR,nC)의 본래 값은 temp에 잠시 저장한다.
            R, C = r-s, c-s
            temp = nA[R][C]
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:    
                for _ in range(2*s):
                    nR, nC = R+dr, C+dc
                    temp, nA[nR][nC] = nA[nR][nC], temp
                    R, C = nR, nC
            s -= 1
    temp = min([sum(nA[i]) for i in range(N)])
    res = temp if temp < res else res

# 여기서 오류 생겼음 찾아야함
# def sel(lst):
#     if len(lst) == K:
#         go(lst)
#     else:
#         for i in range(K):
#             if B[i] not in lst:
#                 sel( lst + [B[i]] )

T = 1
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(K)]
    res = 50000
    for p in itertools.permutations(B):
        go( p )
    print(res)