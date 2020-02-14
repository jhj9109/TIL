from pprint import pprint
import sys
N, M = map(int, sys.stdin.readline().split())

# 1. 인접행렬
field = [[False]*N for _ in range(N)]
for _ in range(M):
    f, t = map(int, sys.stdin.readline().split())
    for x in range(N):
        for y in range(N):
            if x == f and y == t or x == t and y == f:
                field[x][y] = True


if go(0, N, field):
    print(1)
else:
    print(0)

def check (base, field):
used = []
for x in range(N):
    for y in range(N):

def go(y, N, field):
    if y==5:
        return True
    for x in range(N):
        for y in range(N):
            if field[x][y]=True:
                field[x][y]=False
                field[y][x]=False
                if check(y, i, a, n):
                    if go(y+1, N, field):
                        return True
                field[x][y]=True
                field[y][x]=True





''' 2. 인접리스트
from pprint import pprint

import sys
N, M = map(int, sys.stdin.readline().split())
d = [[]] * N

for _ in range(M):
    f, t = map(int, sys.stdin.readline().split())
    if d[f] == []:
        d[f] = [t]
    else:
        d[f].append(t)
    if d[t] == []:
        d[t] = [f]
    else:
        d[t].append(f)
'''