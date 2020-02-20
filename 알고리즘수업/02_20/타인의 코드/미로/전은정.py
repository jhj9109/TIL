dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def find(r, c, N):
    if board[r][c] == '3':
        return 1

    else:
        visited[r][c] = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] != '1' and not visited[nr][nc]:
                    if find(nr, nc, N):
                        return 1
        else:
            return 0
        

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    s_r = s_c = None
    for i in range(N):
        for j in range(N):
            if board[i][j] == '2':
                s_r, s_c = i, j
                break
        if s_r and s_c:
            break
    
    result = find(s_r, s_c, N)
    print('#{} {}'.format(tc, result))