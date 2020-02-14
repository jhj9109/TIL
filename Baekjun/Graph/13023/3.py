from pprint import pprint
import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
M = [[0] * V for _ in range(V)]

for _ in range(E):

    f, t = map(int, input().split())
    M[f][t] = 1
    M[t][f] = 1
print(M)