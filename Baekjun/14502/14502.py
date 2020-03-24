import sys
sys.stdin = open('input14502.txt')
'''6:20~7:30
NxM 필드
0 빈칸 > 새로운 벽의 수 3
1 벽
2 바이러스 > 상하좌우 1칸씩 전진
---------조건--------------
3<=N,M<=8, 2<=바이러스<=10, 빈칸>=3
---------구상----------------
필드 > 0에 새로운 벽을 세울 조건의 수 모두 계산
go : 벽을 먼저 세움
cal : 3개의 벽이 세워지면 시뮬레이션 시작
diff : 바이러스가 퍼지는 동작
check : 각 벽이 세워진 상황에서 상황 종료 후 남은 안전공간 계산 > res에 적용
'''
def go(n):
    if n == 3:
        cal()
    else:
        for r in range(N):
            for c in range(M):
                if f[r][c] == 0:
                    f[r][c] = 1
                    go(n+1)
                    f[r][c] = 0

def cal():
    v = [[False]*M for _ in range(N)]
    copy_f = [[x for x in f[i]] for i in range(N)]
    for r in range(N):
        for c in range(M):
            if f[r][c] == 2 and not v[r][c]:
                diff(r, c, v, copy_f )
    check(copy_f)

def diff(r, c, v, copy_f):
    v[r][c] = True
    s = [(r,c)]
    while s:
        r, c = s.pop()
        for dr, dc in [(0, 1), (0,-1), (1, 0), (-1, 0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<M and not v[nr][nc] and copy_f[nr][nc]!=1:
                copy_f[nr][nc] = 2
                v[nr][nc] = True
                s.append( (nr,nc) )

def check(copy_f):
    global res
    cnt = 0
    for r in range(N):
        for c in range(M):
            if copy_f[r][c] == 0:
                cnt += 1
    res = cnt if cnt > res else res
    return

T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    f = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    go(0)
    print(res)