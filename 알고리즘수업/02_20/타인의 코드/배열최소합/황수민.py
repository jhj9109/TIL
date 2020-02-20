def check(i, n, s):
    global result
    if i == n:
        if result > s:
            result = s
        return
    for j in range(n):
        if visited[j] == 0:
            visited[j] = 1
            temp = s
            s += L[i][j]
            if s < result:
                check(i+1, n, s)
            s = temp
            visited[j] = 0



T = int(input())
for case in range(1, T+1):
    N = int(input())
    L = []
    for i in range(N):
        l = list(map(int, input().split()))
        L.append(l)

    visited = [0]*N
    S = 0
    result = 1000000
    check(0, N, S)
    print('#{} {}'.format(case,result))