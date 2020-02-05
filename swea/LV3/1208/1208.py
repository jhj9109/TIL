T = 10
for T in range(T):
    N = int(input())
    cols = list(map(int, input().strip().split()))
    
    for n in range(N):
        if max(cols)-1 == min(cols):
            break
        cols[cols.index(min(cols))] +=1
        cols[cols.index(max(cols))] -=1
        if min(cols) == max(cols):
            break
    result = max(cols)-min(cols)
    print('#{} {}'.format(T+1, result))