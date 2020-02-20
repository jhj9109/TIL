def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i] < a[i-1]: i -= 1
    if i <= 0: return False
    j = len(a) - 1
    while i-1<j and a[j] < a[i-1]: j -= 1
    a[j], a[i-1] = a[i-1], a[j]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True
    
t = int(input())

for tc in range(1, 1+t):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    c = list(range(n))
    res = 10000
    
    while True:
        tmp = 0
        for i in range(n):
            tmp += a[i][c[i]]
            if tmp >= res: break
        res = min(res, tmp)
        if not next_permutation(c): break
    print('#{} {}'.format(tc, res))