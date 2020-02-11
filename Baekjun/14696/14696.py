import sys
sys.stdin = open('input.txt')

N = int(input())

for _ in range(N):
    s = [0]*5
    d1 = list(map(int, input().split()))
    d2 = list(map(int, input().split()))
    for d in d1[1:]:
        s[d] += 1
    for d in d2[1:]:
        s[d] -= 1
    for i in s[::-1]:
        if i > 0 :
            print('A')
            break
        if i < 0 :
            print('B')
            break
    else:
        print('D')