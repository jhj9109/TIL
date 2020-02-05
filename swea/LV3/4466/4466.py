T = int(input())
for T in range(T):
    N, K = list(map(int, input().strip().split()))
    scores = sorted(list(map(int, input().strip().split())),reverse=True)
    
    
    result = 0
    for i in range(K):
        result += scores[i]
    print('#{} {}'.format(T+1, result))