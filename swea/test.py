T = int(input().strip())
for T in range(T):
    N = int(input().strip())
    
    data_0 = list()
    for _ in range(N):
        data_0.append( list(map(int, input().strip().split(' '))) )
    data_90 = list()
    
    for y in range(N):
        temp = list()
        for x in range(N):
            #data_90[ x ][ x + (-x-y+N-1) ] = data_0[y][x]
            #print('y,x : {},{}'.format(y,x))
            temp.append(data_0[-x+(N-1)][y])
        data_90.append(temp)

    data_180 = list()
    for y in range(N):
        temp = list()
        for x in range(N):
            temp.append(data_90[-x+(N-1)][y])
        data_180.append(temp)

    data_270 = list()
    for y in range(N):
        temp = list()
        for x in range(N):
            temp.append(data_180[-x+(N-1)][y])
        data_270.append(temp)
    
    for a in range(N):
        for b in range(N):
            print('{}'.format(data_90[a][b]),end='')
        print('',end=' ')
        for b in range(N):
            print('{}'.format(data_180[a][b]),end='')
        print('',end=' ')
        for b in range(N):
            print('{}'.format(data_270[a][b]),end='')
        print('')