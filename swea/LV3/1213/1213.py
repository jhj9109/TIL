T = 10
for T in range(T):
    N = int(input())
    target = input().strip() 
    sts = input().strip()
    i, result = 0, 0
    for st in sts:
        if st == target[i]:
            i += 1
            if i == len(target):
                result +=1
                i = 0
        else:
            i = 0
            if st == target[i]:
                i += 1
    print('#{} {}'.format(N, result))