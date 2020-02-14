import sys

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    d = sys.stdin.readline().strip()
    stack = 0
    for c in d:
        if c == '(':
            stack += 1
        else:
            if stack == 0:
                print('NO')
                break
            else:
                stack -= 1
    else:
        if stack == 0:
            print('YES')
        else:
            print('NO')