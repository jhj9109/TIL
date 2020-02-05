T = 10
for T in range(T):
    N = int(input())
    data = list()
    for _ in range(100):
        data.append( list(map(int, input().strip().split())) )
    result = 0
    
    for i in range(100):
        temp1, temp2= 0, 0
        for k in range(100):
            temp1 += data[i][k]
            temp2 += data[k][i]
        if temp1 > result:
            result = temp1
        if temp2 > result:
            result = temp2
    temp3, temp4 = 0, 0
    for i in range(100):
        temp3 += data[i][i]
        temp4 += data[-i+1][-i+1]
    if temp3 > result:
        result = temp3
    if temp4 > result:
        result = temp4
    print('#{} {}'.format(N, result))