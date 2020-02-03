T = int(input())
for T in range(T):
    N = int(input())
    numbers = list(map(int, input().strip().split()))
    
    print(f'#{T+1} ', end='')
    idx = []
    for i in range(5):
        min_num = 101
        max_num = 0
        temp = [0,0]
        for i in range(len(numbers)):
            if numbers[i] > max_num and i not in idx:
                max_num = numbers[i]
                temp[0] = i
            if numbers[i] < min_num and i not in idx:
                min_num = numbers[i]
                temp[1] = i
        idx = idx + temp
        print(max_num, min_num, end=' ')
    print('')