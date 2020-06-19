import sys
sys.stdin = open('input13460.txt')

from collections import deque
def bfs(R, B):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 빨간, 파란 구슬 위치 : r, b
    n = 1
    dq = deque([ [R, B, n] ])

    while dq:
        R, B, n = dq.popleft()
        if n > 10:
            return -1
        for k in range(4):
            # R, B => 이번 턴 수행 => [rx, ry], [bx, by]
            rx, ry = R
            bx, by = B

            flag = False # 구슬이 함께 움직임을 고려해야할 경우

            # 해당 방향 끝까지 이동한다.
            while True:
                rx, ry = rx + dx[k], ry + dy[k]
                if f[rx][ry] == 'O': # 구멍 => 종료
                    return n
                if f[rx][ry] == '#': # 벽 => 이전자리로
                    rx, ry = rx - dx[k], ry - dy[k]
                    break
                elif [rx, ry] == B: # 파란 구슬 => 이전자리로, flag = True
                    rx, ry = rx - dx[k], ry - dy[k]
                    flag = True
                    break

            while True:
                bx, by = bx + dx[k], by + dy[k]
                if f[bx][by] == 'O': # 구멍
                    break
                if f[bx][by] == '#' or [bx, by] == R: # 벽 or 빨간 구슬 => 이전자리로
                    bx, by = bx - dx[k], by - dy[k]
                    if flag: # 두 구슬이 붙어진행
                        rx, ry = bx - dx[k], by - dy[k]
                    break
            if f[bx][by] != 'O' and not ([rx, ry] == R and [bx, by] == B):
                dq.append([ [rx,ry], [bx,by], n+1 ])

T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    f = [list(input()) for _ in range(N)]
    
    for x in range(N):
        for y in range(M):
            if f[x][y] == 'R':
                R = [x, y]
            elif f[x][y] == 'B':
                B = [x, y]

    print(bfs(R, B))