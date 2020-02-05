T = 10
for T in range(T):
    n = int(input())
    buildings = list(map(int, input().strip().split(' ')))
    result = 0
    for idx in range(2,n-2):
        temp = buildings[idx] - buildings[idx-1]

        if buildings[idx] - buildings[idx-2] < temp :
            temp = buildings[idx] - buildings[idx-2]
        if buildings[idx] - buildings[idx+1] < temp :
            temp = buildings[idx] - buildings[idx+1]
        if buildings[idx] - buildings[idx+2] < temp :
            temp = buildings[idx] - buildings[idx+2]
        #print ('idx:{}, temp:{}'.format(idx, temp))
        if temp > 0 :
            result += temp
            #print ('result:{}'.format(result))
    print('#{} {}'.format(T+1,result))