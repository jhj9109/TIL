from pprint import pprint
import sys
sys.stdin = open('input.txt')

V, Edge = map(int, input().split())

M = [[0] * V for _ in range(V)]
G = {node: [] for node in range(V)}
K = [[] for _ in range(V)]
F = []

for _ in range(Edge):

    f, t = map(int, input().split())
    print(f, t)
    M[f][t] = 1
    M[t][f] = 1

    G[f].append(t)
    G[t].append(f)

    G2[f].append(t)
    G2[t].append(f)

    K[f].append(t)
    K[t].append(f)
    
    #3.Edge 리스트
    F.append([f, t])
    F.append([t, f])

for i in range(len(F)):
    for j in range(len(F)):
        A, B = F[i]
        C, D = F[j]

        #소거
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not M[B][C]:
            continue
        for E in G[D]:
            if E == A or E == B or E == C or E == D:
                continue
            print(1)
            sys.exit(0)
pprint(0)
pprint(M)
pprint(G)
pprint(K)
pprint(F)