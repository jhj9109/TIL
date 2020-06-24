import sys
sys.stdin = open('input13460.txt')

from collections import deque
def bfs(Red, Blue):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 빨간, 파란 구슬 위치 : r, b
    n = 1
    dq = deque([ [Red, Blue, n] ])

    while dq:
        Red, Blue, n = dq.popleft()
        if n > 10:
            return -1
        for k in range(4):
            # R, B => 이번 턴 수행 => [rx, ry], [bx, by]
            # rx, ry = Red
            # bx, by = Blue

            flag = False # 구슬이 함께 움직임을 고려해야할 경우
            red_exit, blue_exit = False, False

            # 해당 방향 끝까지 이동한다.
            j = 1
            while True:
                # rx, ry = rx + dx[k], ry + dy[k]
                rx, ry = Red[0] + dx[k] * j, Red[1] + dy[k] * j
                if f[rx][ry] == 'O': # 구멍 => 종료
                    rx, ry = -1, -1
                    red_exit = True
                    break
                if f[rx][ry] == '#': # 벽 => 이전자리로
                    rx, ry = Red[0] + dx[k] * (j-1), Red[1] + dy[k] * (j-1)
                    break
                if [rx, ry] == Blue: # 파란 구슬 => 이전자리로, flag = True
                    rx, ry = Red[0] + dx[k] * (j-1), Red[1] + dy[k] * (j-1)
                    flag = True
                    break
                j += 1

            j = 1
            while True:
                # bx, by = bx + dx[k], by + dy[k]
                bx, by = Blue[0] + dx[k] * j, Blue[1] + dy[k] * j
                if f[bx][by] == 'O': # 구멍
                    bx, by = -1, -1
                    blue_exit = True
                    break
                if f[bx][by] == '#' or (bx == rx and by == ry) : # 벽 or 빨간 구슬 => 이전자리로
                    bx, by =  Blue[0] + dx[k] * (j-1), Blue[1] + dy[k] * (j-1)
                    if flag: # 두 구슬이 붙어진행
                        rx, ry = Blue[0] + dx[k] * (j-2), Blue[1] + dy[k] * (j-2)
                    break
                j += 1

            if red_exit and not blue_exit:
                return n
            if not blue_exit and not ([rx, ry] == Red and [bx, by] == Blue):
                dq.append([ [rx,ry], [bx,by], n+1 ])
    else:
        return -1
        
T = 7 # 테스트 케이스 용도
T = 1 # 백준 제출시
for tc in range(1, T+1):
    N, M = map(int, input().split())
    f = [list(input()) for _ in range(N)]
    
    for x in range(N):
        for y in range(M):
            if f[x][y] == 'R':
                Red = [x, y]
            elif f[x][y] == 'B':
                Blue = [x, y]

    print(bfs(Red, Blue))