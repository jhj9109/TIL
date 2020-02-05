def poww(N, M):
    if M == 1:
        return N
    else:
        return poww(N, M-1) * N
T = 10
for T in range(T):
    num = int(input())
    N, M = list(map(int, input().strip().split()))
    result = poww(N, M)
    
    print('#{} {}'.format(num, result ))