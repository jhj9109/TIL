import sys
sys.stdin = open('sample_input4874.txt')

def calc(data):
    s = []
    for d in data:
        if d.isdigit():
            s.append(int(d))
        else:
            if d == '.':
                if len(s) == 1:
                    return int(s[0])
                else:
                    return 'error'
            if len(s) < 2:
                return 'error'
            n2, n1 = s.pop(), s.pop()
            if d == '+':
                s.append(n1 + n2)
            if d == '*':
                s.append(n1 * n2)
            if d == '/':
                s.append(n1 // n2)
            if d == '-':
                s.append(n1 - n2)


T = int(input())
for tc in range(1, T+1):
    d = input().split()
    print(f'#{tc} {calc(d)}')