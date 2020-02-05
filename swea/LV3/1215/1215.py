#T = 0
T = 10
for T in range(T):
    N = int(input().strip())
    
    data = list()    
    for _ in range(8):
        data.append(list(st for st in input().strip() ) )
        
    cnt = 0
    for y in range(8):
        for x in range(8 - (N - 1)):
            for i in range( N // 2) :
                if data[y][x + i] != data[y][x - i + (N - 1)]:
                    break
            else: #No break
                cnt += 1
                #print('data[y][x] : {}, {}'.format(y,x))
                
    for x in range(8):
        for y in range(8 - (N - 1)):
            for i in range( N // 2) :
                if data[y + i][x] != data[y - i + (N - 1)][x]:
                    break
            else: #No break
                #print('data[x][y] : {}, {}'.format(y,x))
                cnt += 1
    print('#{} {}'.format(T+1, cnt))