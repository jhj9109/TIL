import sys
sys.stdin = open('input1865.txt')
'''
2:09 ~ 3:07
N : 1~16 >>> 경우의수 1,307,674,368,000 : 1.3조
r : 직원 N명
c : 일 N개
성공확률 Pr,c
모든 성공확률이 최대
'''
def dfs_rec(r, now):
    global res
    if r == N-1:
        res = now
    else:
        for w in range(N):
            if not v[w] and now*field[r+1][w] > res: #백트래킹
                v[w] = True
                dfs_rec(r+1, now*field[r+1][w])
                v[w] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = list( [int(n)/100 for n in input().split() ] for _ in range(N))
    v = [False]*(N)
    res = 0
    dfs_rec(-1, 100)
    print('#{0} {1:00.6f}'.format(tc, res ))