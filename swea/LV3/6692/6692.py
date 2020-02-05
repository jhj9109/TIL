T = int(input())
for T in range(T):
    N = int(input())
    result = 0
    for i in range(N):
        x, y = input().strip().split()
        result += float(x) * int(y)
    print(f'#{T + 1} { result }')