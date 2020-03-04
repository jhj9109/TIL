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
def dfs(s, percent):
    v = []
    res = 0
    while s:
        # r, c, now = s.pop() #
        r, c = s.pop() # v도착후 행동
        now = percent.pop() #확률
        while len(v) != r:
            v.pop()
        v.append(c)

        if now > res: #백트래킹
            if r == N-1: # 일 분배완료 & now > res
                res = now
            else:
                for w in range(N): #w서치
                    if w not in v:
                        # s.append((r+1, w, now*field[r+1][w]))
                        s.append((r+1, w))
                        percent.append(now*field[r+1][w])
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = list( [float(n)/100 for n in input().split() ] for _ in range(N))
    #초기값
    percent = [n for n in field[0]]
    #s = [(0, i, percent[i]) for i in range(N) ]
    s = [(0, i) for i in range(N)]
    print('#{0} {1:00.6f}'.format(tc, dfs(s, percent)*100 ))