import sys
sys.stdin = open('input15684.txt')

from collections import deque

def game(lst):
    global res
    for c in range(1, N+1):
        now = c
        for r in range(H):
            if (r, now-1) in lst:
                now -= 1
            elif (r, now) in lst:
                now += 1
            # else: now = now
        if now != c:
            return False
    return True

def sim_bfs(init_lst):
    if game(init_lst):
        return 0

    dq = deque([ init_lst ])

    while dq:
        lst = dq.popleft()

        if game(lst):
            return len(lst) - len(init_lst)

        if len(lst) == len(init_lst):
            row, col = -1, -1 
        else:
            row, col = lst[-1]

        # 새로운 다리 놓을 후보
        for r in range(H):
            for c in range(col, N):
                if (c > col or r > row) and (r, c-1) not in lst and (r, c) not in lst and (r, c+1) not in lst:
                    dq.append( lst+[(r, c)] )
    else:
        return -1

T = 7
for tc in range(1, T+1):
    N, M, H = map(int, input().split())

    init_lst = []
    v = [[0]*(N+2) for _ in range(H)]
    

    for _ in range(M):
        # a:row, b:column
        a, b = map(int, input().split())
        init_lst.append( (a-1, b) )

    res = float('inf')

    print(f'#{tc} {sim_bfs(init_lst)}')