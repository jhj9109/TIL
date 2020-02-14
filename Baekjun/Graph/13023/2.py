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