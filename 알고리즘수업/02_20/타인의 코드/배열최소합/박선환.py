def f(n, k):
    if n == k:
        if sum(sum_temp) < min_sum[0]:
            min_sum[0] = sum(sum_temp)
        return
    else:
        for i in range(N):
            if used[i] == 0:
                A[n] = i
                used[i] = 1
                sum_temp[n] = M[n][A[n]]
                if sum(sum_temp) >= min_sum[0]:
                    used[i] = 0
                    continue
                f(n+1, k)
                used[i] = 0
        else:
            sum_temp[n] = 0
            A[n] = 0

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    min_sum = [10000000]
    sum_temp = [0]*N
    used = [0]*N
    A = [0]*N
    result = []
    f(0, N)

    print('#{} {}'.format(tc, min_sum[0]))