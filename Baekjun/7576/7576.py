'''1시간 소요
0 익지 않은 토마토
1 익은 토마토 > 확산
-1 들어 있지 않은 칸
M 가로 N 세로
2 <= M,N <= 1000
--------------------
모두 익는데 걸리는 시간 출력
불가능시 -1
'''
from collections import deque
import sys
sys.stdin = open('input7576.txt') #예제 5개
input = sys.stdin.readline

def start():
    cnt = 0 # 익게 만들어야할 토마토 숫자
    q = deque([]) # 시작점 == 익은 토마트 리스트
    for r in range(N):
        for c in range(M):
            if d[r][c] == 0:
                cnt += 1
            elif d[r][c] == 1:
                q.append((r,c))
                v[r][c] = 0
    return bfs(q, cnt)
              

def bfs(q, n): # 익은 토마토들의 리스트 == 시작점으로 갖고 시작
    temp = 0
    while q:
        r, c = q.popleft()
        if n == 0:
            return temp
        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            if 0<=nr<N and 0<=nc<M and d[nr][nc] == 0 and v[nr][nc] == -1:
                q.append((nr, nc))
                temp = v[r][c] + 1
                v[nr][nc] = temp
                n -= 1
    return -1

dr = [0, 0, 1,-1]
dc = [1,-1, 0, 0]

T = 5 # 제출 시 T = 1, 기타값 : 예제 돌리기용
for tc in range(1, T+1):
    M, N = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(N)]
    v = [[-1] * M for _ in range(N) ]
    print(start())