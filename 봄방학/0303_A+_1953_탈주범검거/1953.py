import sys
sys.stdin = open('input1953.txt')

'''
11:40~
1~L시간동안 있을수 있는 장소 >>> visited
1 : 사방    2 : 세로 3 : 가로
4 : N, E    5 : S, E    6 : S, W    7 : W, N
일단 DFS >>> visited 경로가 겹쳐 정답보다 적게 나오는 현상 발생 >>> 응급 코드로 땜질
>>>궁극적으로 BFS 풀어야 좀더 알맞음
'''
def go(r, c, t, field):
    # 북 동 남 서

    dr = [-1, 0, 1, 0]
    dc = [ 0, 1, 0,-1]
    k_lst = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [1, 2], [2, 3], [3, 0]] # 현재 pipe(1~7)가 4방향 중 가능한 서치방향 
    p_lst = [[1, 2, 5, 6], [1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5]] # 다음 pipe가 4방향에 연결 가능한지

    s = [(r, c)]
    time = [1]
    visited = [[False]*M for _ in range(N)]

    cnt = 0
    while s:
        r, c = s.pop()
        now = time.pop()
        pipe = field[r][c]
        if visited[r][c] == False:
            visited[r][c] = now
            cnt += 1
        else:
            visited[r][c] = now if now > visited[r][c] else visited[r][c]
        if now != t:
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]
                if (0 <= nr <= N-1 and 0 <= nc <= M-1) and (not visited[nr][nc] or now < visited[nr][nc] ) and (k in k_lst[pipe] and field[nr][nc] in p_lst[k]):
                    s.append( (nr, nc))
                    time.append( now+1 )
    return cnt



T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    field = [list(map(int,input().split())) for _ in range(N)]
    
    print(f'#{tc} {go(R, C, L, field)}')