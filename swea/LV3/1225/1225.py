T = 10
for _ in range(T):
    N = int(input())
    n = list(map(int, input().split()))

    k = 0
    flag = True
    while flag:
        if n[0] - (k % 5 + 1)  <= 0 :
            n[0] = 0
            flag = False
        else:
            n[0] -= (k % 5 + 1)
        n.append(n.pop(0))
        k += 1
    print(f"#{N} {' '.join(map(str, n))}")