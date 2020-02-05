T = int(input())
for T in range(T):
    x, y = list(map(int, input().strip().split()))
    numbers = list(map(int, input().strip().split()))
    

    result = []
    print('#{} '.format(T+1), end='')
    for i in range(1, x + 1):
        if i not in numbers:
            print(i, end=' ')
    print('')
    