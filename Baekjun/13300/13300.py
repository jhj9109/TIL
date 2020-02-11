import sys
sys.stdin = open('input.txt')
def my_div(n, K):
    return ((n//K)+1) if n % K else (n//K)

N, K = map(int, input().split())
d = [0]*13
for _ in range(N):
    S, Y = map(int, input().split())
    d[S*6 + Y] += 1
res = 0
print(d)
for n in d[1:]:
    res += my_div(n, K)
print(res)