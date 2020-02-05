T = int(input())
for T in range(T):
    N, M = map(int, input().strip().split())
    print('#{} {} {}'.format(T+1, 2*M-N, N-M))