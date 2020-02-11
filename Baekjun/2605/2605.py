N = int(input())
d = list(range(1,N+1))
for i, n in enumerate(list(map(int, input().split()))):
    d[i-n:i+1] = d[i:i+1] + d[i-n:i]
for n in d:
    print(n, end=' ')
print('')