N = int(input())
d = [[False]*100 for _ in range(100)]
for _ in range(N):    
    x1, y1 = map(int, input().split())
    for x in range(x1, x1+10):
        for y in range(y1, y1+10):
            d[x][y] = True
cnt = 0
for x in range(100):
        for y in range(100):
            cnt += 1 if d[x][y] else 0
print(cnt)