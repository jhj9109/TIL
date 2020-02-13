import sys
sys.stdin = open('input.txt')

input=sys.stdin.readline

d = []
N = int(input())
for tc in range(N):
    com = list(input().split())

    if com[0] == 'push':
        d.append(int(com[1]))

    if com[0] == 'top':
        if d != []:
            print(d[-1])
        else:
            print(-1)
        
    if com[0] == 'size':
        print(len(d))

    if com[0] == 'empty':
        print(int( not (bool(d)) ) )

    if com[0] == 'pop':
        if d != []:
            print(d.pop())
        else:
            print(-1)