    N = int(input())
    max_cnt = 1
    result = [N]
    for n in range(1,N):
        temp = [N, n]
        while temp[-2] - temp[-1] >= 0:
            temp.append(temp[-2] - temp[-1])
        if len(temp) > max_cnt :
            result = temp
            max_cnt = len(temp)
    print(max_cnt)
    for i in range(len(result)):
        if i != len(result)-1 :
            print(result[i], end=' ')
        else:
            print(result[i])