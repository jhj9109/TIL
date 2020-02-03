T = int(input())
for T in range(T):
    #test 정수 갯수 N, 구간의 길이 M
    N, M = map(int, input().strip().split())
    test = list(map(int, input().strip().split()))

    #초기값
    max_num, min_num = 0, 0
    for i in range(M):
        max_num += test[i]
        min_num += test[i]
    #print (N, M, test, max_num, min_num)
    for idx in range(1, N - (M - 1)):
        temp = 0
        for j in range(M):
            temp += test[idx + j]
        max_num = temp if temp > max_num else max_num
        min_num = temp if temp < min_num else min_num
        #print(f'{idx},{max_num},{min_num}')
    
    print(f'#{T+1} {max_num - min_num}')