import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().strip().split())
    field = [list(map(int , input().strip().split())) for _ in range(N)]

    max_cnt = 0
    for x in range(N):
        cnt = 0
        for y in range(M):
            if field[x][y] == 1:
                cnt += 1
                max_cnt = cnt if cnt > max_cnt else max_cnt
            else:
                cnt = 0
    for y in range(M):
        cnt = 0
        for x in range(N):
            if field[x][y] == 1:
                cnt += 1
                max_cnt = cnt if cnt > max_cnt else max_cnt
            else:
                cnt = 0
    print(f'#{tc} {max_cnt}')