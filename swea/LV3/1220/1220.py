T = 10
for T in range(T):
    N = int(input())

    test = []
    for _ in range(N):
        test.append(list(map(int, input().strip().split())))

    cnt = 0    
    for y in range(N):
        for x in range(N):
            if test[y][x] == 1:
                for i in range(y+1,N) :
                    if test[i][x] == 1:
                        break
                    elif test[i][x] == 2:
                        cnt += 1
                        break
    print('#{} {}'.format(T+1, cnt))