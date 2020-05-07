import sys
sys.stdin = open('input5202.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    se = []
    for n in range(N):
        se.append(tuple(map(int, input().split())))
    se.sort(key=lambda se: se[1])
    se_used = [0]*N
    res = 0
    for j in range(0, N ):
        if se_used[j] == 0:
            se_used[j] = 1
            cnt = 1
            for i in range(j+1, N):
                if se[i][0] >= se[j][1]:
                    se_used[j] = 1
                    cnt += 1
                    j = i
            res = cnt if cnt > res else res
    print(f'#{tc} {res}')