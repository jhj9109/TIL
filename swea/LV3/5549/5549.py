T = int(input())
for T in range(T):
    n = int(input())
    if n % 2 :
        print('#{} Odd'.format(T+1))
    else:
        print('#{} Even'.format(T+1))