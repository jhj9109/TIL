import sys

sys.stdin = open('input.txt')

T = 10

for tx in range(1, T+1):
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(100)]
    
    m = 0
    
    for i in range(100):
        s = 0
        for j in range(100):
            s += d[i][j]
        if s >= m:
            m = s

    for i in range(100):
        s = 0
        for j in range(100):
            s += d[j][i]
        if s > m:
            m = s
    s = 0
    for i in range(100):
        s += d[i][i]
    if s > m:
        m = s
    
    s = 0
    for i in range(100):
        s += d[-1-i][-1-i]
    if s > m:
        m = s
    
    print(f'#{tx} {m}')