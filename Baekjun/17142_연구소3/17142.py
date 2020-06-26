import sys
sys.stdin = open('input17142.txt')

from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
def bfs(virus, cnt):
    global res
    clab = deepcopy(lab)
    dq = deque([])

    # 0 : 바이러스가 퍼져야할 공간 (빈칸0)
    # 1 : 벽이나 활성바이러스가 자리 잡은 곳
    # 2 : 비활성화 바이러스 자리 잡은 곳
    for r, c in virus:
        clab[r][c] = 1
        dq.append( (r, c, 0) ) 

    # 초기 바이러스 큐
    while dq:
        r, c, n = dq.popleft()

        # 백트래킹
        if n >= res:
            return
        
        # 바이러스 확산 동작
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            # 바이러스가 새로 퍼질 공간이라면
            if 0 <= nr < N and 0 <= nc < N and clab[nr][nc] != 1:
                if clab[nr][nc] == 0:
                    # 빈 공간이 바이러스로 바껴야함
                    cnt -= 1
                    if cnt == 0:
                        res = n+1 # (n+1)이 res보다 작거나 같은 상태
                        return
                #else: 비활성화 바이러스 => 활성화 바이러스
                clab[nr][nc] = 1
                dq.append( (nr, nc, n+1) )

    # 바이러스가 모든 공간에 퍼지는 것 실패
    return
T = 1
T = 7 # 테스팅용
for tc in range(1, T+1):
    N, M = map(int, input().split()) # NxN 연구소크기, M 초기활성시킬 바이러스 수
    
    lab = [list(map(int, input().split())) for _ in range(N)] # 0빈칸, 1벽, 2바이러스

    init_cnt = 0
    goal = 0
    input_virus = []
    for r in range(N):
        for c in range(N):
            if lab[r][c] == 0:
                goal += 1
            elif lab[r][c] == 2:
                input_virus.append( (r,c) )          
    if goal == 0:
        print(0)
    else:
        res = float('inf')

        for p in combinations(input_virus, M):
            # 각 바이러스 동시 작용 => 최소 시간 => BFS
            bfs(p, goal)
        
        print(res if res != float('inf') else -1)