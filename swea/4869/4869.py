def paper(n):
    s = [0, 1, 3] #0,1,2
    for i in range(3, n+1):
        s.append(s[i-1] + 2 * s[i-2])
    return s[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N //= 10
    print(f'#{tc} {paper(N)}')