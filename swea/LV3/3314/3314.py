T = int(input())
for T in range(T):
    scores = [n if n>=40 else 40 for n in map(int, input().strip().split())]
    print('#{} {}'.format(T+1, sum(scores) // 5))