# 1 : N
# 2 : S

T = 10
for tc in range(1, T+1):
    N = int(input())

    field = [list(map(int, input().strip().split())) for _ in range(N)]

    cnt = 0    
    for y in range(N):
        s = 0
        for x in range(N):
            if field[x][y] == 1 and s == 0: #s:1일땐 아무일도 일어나지 않는다
                s = 1
            if field[x][y] == 2 and s == 1: #s:0일땐 아무일도 일어나지 않는다
                cnt += 1
                s = 0
    print(f'#{tc} {cnt}')