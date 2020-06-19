import sys
sys.stdin = open("input12100.txt")

# 12:05
def dfs(n, f):
    global res
    if n == 5:
        temp = max([ max(f[i]) for i in range(N) ])
        res = temp if temp > res else res
        return
    # 동
    nf = [[0]*N for _ in range(N)]
    for r in range(N):
        i = -1
        for c in range(-1, -(N+1), -1):
            if f[r][c]:    
                if not nf[r][i]: # 합칠 대상이 없으면
                    nf[r][i] = f[r][c]
                elif nf[r][i] != f[r][c] : # 값이 다르면
                    i -= 1
                    nf[r][i] = f[r][c]
                else: # 이젠 합칠때
                    nf[r][i] *= 2
                    i -= 1
    dfs (n+1, nf)

    # 서
    nf = [[0]*N for _ in range(N)]
    for r in range(N):
        i = 0
        for c in range(N):
            if f[r][c]:    
                if not nf[r][i]: # 합칠 대상이 없으면
                    nf[r][i] = f[r][c]
                elif nf[r][i] != f[r][c] : # 값이 다르면
                    i += 1
                    nf[r][i] = f[r][c]
                else: # 이젠 합칠때
                    nf[r][i] *= 2
                    i += 1
    dfs (n+1, nf)

    # 북
    nf = [[0]*N for _ in range(N)]
    for c in range(N):
        i = 0
        for r in range(N):
            if f[r][c]:    
                if not nf[i][c]: # 합칠 대상이 없으면
                    nf[i][c] = f[r][c]
                elif nf[i][c] != f[r][c] : # 값이 다르면
                    i += 1
                    nf[i][c] = f[r][c]
                else: # 이젠 합칠때
                    nf[i][c] *= 2
                    i += 1
    dfs (n+1, nf)

    # 남
    nf = [[0]*N for _ in range(N)]
    for c in range(N):
        i = -1
        for r in range(-1, -(N+1), -1):
            if f[r][c]:    
                if not nf[i][c]: # 합칠 대상이 없으면
                    nf[i][c] = f[r][c]
                elif nf[i][c] != f[r][c] : # 값이 다르면
                    i -= 1
                    nf[i][c] = f[r][c]
                else: # 이젠 합칠때
                    nf[i][c] *= 2
                    i -= 1 
    dfs (n+1, nf)

# 동 서 남 북
T = 1
for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    dfs(0, d)
    print(res)