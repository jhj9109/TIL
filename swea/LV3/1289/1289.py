T = int(input())
for T in range(T):
    sts = input().strip()
    
    cnt = 0
    if sts[0] == '1':
        cnt += 1
    for i in range(len(sts)-1):
        if sts[i] != sts[i+1]:
            cnt += 1
    print('#{} {}'.format(T+1, cnt))
        
        