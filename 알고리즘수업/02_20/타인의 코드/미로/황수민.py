from collections import deque

def DFS(i,j):
    stack = deque()
    M[i][j] = 1
    stack.append([i,j])
    while stack:
        i, j = stack.pop()
        for k in range(4):
            if i+di[k] >= 0 and i+di[k] < N and j+dj[k] >= 0 and j+dj[k] < N:
                if M[i+di[k]][j+dj[k]] == 3:
                    return 1
                if M[i+di[k]][j+dj[k]] == 0:
                    stack.append([i+di[k],j+dj[k]])
                    M[i][j] = 1
    return 0


di = [1,-1,0,0]
dj = [0,0,1,-1]

T = int(input())
for case in range(1, T+1):
    N = int(input())
    M = []
    for i in range(N):
        m = list(map(int, list(input())))
        for j in range(N):
            if m[j] == 2:
                start = [i,j]
        M.append(m)
    print('#{} {}'.format(case, DFS(start[0],start[1])))

