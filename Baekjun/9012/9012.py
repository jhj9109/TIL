import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    s = []
    d = input()
    for c in d:
        if c == '(':
            s.append('(')
        else:
            if s == [] or s.pop() != '(':
                print('NO')
                break
    else:
        if s == []:
            print('YES')
        else:
            print('NO')
