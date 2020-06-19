import sys
sys.stdin = open('input13458.txt')

import sys
T = 1
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    a = sys.stdin.readline().split()
    B, C = map(int, sys.stdin.readline().split())
    print(sum(list(map(lambda x: 1  if int(x)<=B else (int(x)-B)//C + 2 if (int(x)-B)%C else (int(x)-B)//C + 1, a))))