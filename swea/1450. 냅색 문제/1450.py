import sys
sys.stdin = open('input1450.txt')

from itertools import combinations

N, C = map(int, input().split())
obs = list(map(int, input().split()))

for in range combinations(obs, n)