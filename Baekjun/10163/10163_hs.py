n = int(input())
from #pprint import #pprint

orders = [list(map(int, input().split())) for _ in range(n)]
#pprint(orders)
mxm = max([max(ai[0]+ai[2], ai[1]+ai[3]) for ai in orders])
#pprint(mxm)
c = [[-1]*mxm for _ in range(mxm)]
#pprint(c)
cnt = 1
for order in orders:
    for i in range(order[0], order[0]+order[2]):
        for j in range(order[1], order[1]+order[3]):
            c[i][j] = cnt
    cnt+=1
#pprint(c)
res = [0]*(n+1)

for i in range(mxm):
    for j in range(mxm):
        if c[i][j]>0:
            res[c[i][j]] +=1

for i in range(1, n+1):
    print(res[i])