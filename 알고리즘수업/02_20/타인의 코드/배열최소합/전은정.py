def find(n, N, sum):
    if n == N:
        if sum < max_sum[0]:
            max_sum[0] = sum
            return

    elif sum > max_sum[0]:
        return

    else:
        for i in range(N):
            if not picked_col[i]:
                picked_col[i] = True
                picked_num = matrix[n][i]
                find(n+1, N, sum + picked_num)
                picked_col[i] = False

    
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    picked_col = [False]*N
    max_sum = [1000]

    find(0, N, 0)

    print('#{} {}'.format(tc, max_sum[0]))