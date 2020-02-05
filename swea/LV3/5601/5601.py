T = int(input())
for T in range(T):
    N = int(input())
    
    print('#{} '.format(T+1),end='')
    for _ in range(N):
        print('1/{}'.format(N), end=' ')
    print('')