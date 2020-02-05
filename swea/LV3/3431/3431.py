T = int(input())
for T in range(T):
    L, U, X = [n for n in map(int, input().strip().split())]
    
    result = 0
    if X > U:
        result = -1
    else:
        if X > L:
            result = 0
        else:
            result = L-X
        
    
    print('#{} {}'.format(T+1, result))