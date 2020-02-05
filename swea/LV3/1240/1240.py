hint = [ '0001101', '0011001', '0010011', '0111101', '0100011',\
    '0110001', '0101111', '0111011', '0110111', '0001011'
]
T = int(input())
for T in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    #############print(data)
    flag = False
    for x in range(N):
        for y in range(M): #-1==79, : -y + M - 56
            if data[x][-y] == '1':
                ######print(x,-y)
                source =data[x][-y+M-55:-y+M+1] #-55~ 0
                ###############print(source)
                flag = True
            if flag:
                break
        if flag:
            break
    sums = 0
    numbers = 0
    #########print(source)
    for i in range(8):
        temp = hint.index(source[0+7*i:7+7*i])
        ###########print(temp)
        numbers += temp
        if (i+1) % 2:#짝수
            sums += temp * 3
            #########print(f'{sums} += {temp} * 3')
        else:
            sums += temp
            #######print(f'{sums} += {temp}')
    #########print(numbers, sums)
    if (sums % 10) == 0:
        print(f'#{T+1} {numbers}')
    else:
        print(f'#{T+1} 0')