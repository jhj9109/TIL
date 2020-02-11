import sys
sys.stdin = open('input.txt')

N = int(input())
data = list(map(int, input().split()))

k = 1
cnt = 1
res = 0
bonus = 0
for i in range(len(data)-1):
    if data[i+1]*k >= data[i]*k:
        cnt += 1
        bonus = (bonus+1) if data[i+1]*k == data[i]*k else 0

    else:
        k *= -1
        res = cnt if cnt > res else res
        cnt = 2 + bonus
        bonus = 0
print(res) if res > cnt else print(cnt)