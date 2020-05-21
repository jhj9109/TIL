import sys
sys.stdin = open('input1249.txt')
'''10:50
출발지 S(0,0) > 도착지 G(N-1,N-1) 까지 가기 위한 도로복구 빠른 시간내 수행
파여진 깊이만큼 복구 시간 증가
복구 시간이 가장 짧은 경로는?
'''
# def dfs(r, c):
#     global res
#     if v[r][c] >= res:
#         return
#     if (r, c) == (N-1, N-1):
#         res = v[r][c]
#         return
#     for dr, dc in [ (0,1), (0,-1), (-1,0), (1,0) ]:
#         nr, nc = r+dr, c+dc
#         if 0 <= nr < N and 0 <= nc < N and (not v[nr][nc] or (v[r][c] + f[nr][nc]) < v[nr][nc]):
#             v[nr][nc] = v[r][c] + f[nr][nc]
#             dfs(nr, nc)
def dfs(N):
    v = [ [0]*N for _ in range(N)]
    visited =  [ [0]*N for _ in range(N)]
    res = (2 * N - 3) * 9

    s = [(0, 0)]
    visited[0][0] = 1
    while s:
        r, c = s.pop()
        for dr, dc in [ (0,1), (1,0), (0,-1), (-1,0) ]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                if (nr, nc) == (N-1, N-1):
                    res = v[r][c] if v[r][c] < res else res
                else:
                    nValue = v[r][c] + f[nr][nc]
                    if not visited[nr][nc] or ( nValue < res and nValue < v[nr][nc] ):
                        s.append( (nr, nc) )
                        visited[nr][nc] = 1
                        v[nr][nc] = nValue
    return res

# from collections import deque
# def bfs(N):
#     v = [ [0] * N for _ in range(N)]
#     res = N * 2 * 9

#     q = deque( [(0, 0)] )
#     # v[0][0] = 0
#     while q:
#         r, c = q.popleft()
#         if (r, c) == (N-1, N-1):
#             res = v[r][c]
#             continue
#         for dr, dc in [ (0,1), (0,-1), (-1,0), (1,0) ]:
#             nr, nc = r+dr, c+dc
#             if 0 <= nr < N and 0 <= nc < N and (not v[nr][nc] or (v[r][c] + f[nr][nc] < v[nr][nc])) and (v[r][c] + f[nr][nc] < res) :
#                 v[nr][nc] = v[r][c] + f[nr][nc]
#                 q.append( (nr, nc) )
#     return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    f = [list(map(int, input())) for _ in range(N)]
    # f[0][0], f[N-1][N-1] = 0, 0
    # 맵 d에 대응하는 v 작성 > 가는데까지 걸린 소요시간 반영
    print(f'#{tc} {dfs(N)}')