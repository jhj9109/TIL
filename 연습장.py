T = 10
for t in range(T):

    N, number_str = list(input().strip().split())
    number = [int(n) for n in number_str]
    flag = True
    while flag:
        flag = False
        for idx in range(len(number)-1) :
            if number[idx] == number[idx+1]:
                flag = True
                number.pop(idx)
                number.pop(idx)
                break
    
    print(f'#{t+1} ',end='')
    for n in number:
        print(f'{n}',end='')
    print('')
            