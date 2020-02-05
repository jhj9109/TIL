T = int(input())
for T in range(T):
    N = int(input())
    
    farm = []
    for _ in range (N):
        farm.append( [int(n) for n in input().strip()] )
    
    Q = N // 2
    result = 0    
    for y in range(Q): #y = 3 0 6, q=3
        result += sum(farm[y][Q-y : Q+y+1])
        #print(2*y+1)
    for y in range(Q,N):
        result += sum(farm[y][y-Q : 3*Q-y+1])
        #print('{} : {}'.format(y-Q, 3*Q-y))
    
    print('#{} {}'.format(T+1,result))