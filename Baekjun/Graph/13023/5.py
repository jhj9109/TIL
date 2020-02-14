from pprint import pprint
import sys
sys.stdin = open('input.txt')

V, Edge = map(int, input().split())


G2 = dict.fromkeys(range(V), 0)
G = {node: [] for node in range(V)}
pprint(G)
pprint(G2)


for _ in range(Edge):

    f, t = map(int, input().split())

    G[f].append(t)
    G[t].append(f)

    G2[f].append(t)
    G2[t].append(f)

pprint(G)
pprint(G2)