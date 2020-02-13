import sys
sys.stdin =open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    d = input()
    s = []
    for c in d:
        if c == '(' or c == '{':
            s.append(c)
        if c == ')':
            if s == [] or s.pop() != '(':
                print(f'#{tc} 0')
                break
        if c == '}':
            if s == [] or s.pop() != '{':
                print(f'#{tc} 0')
                break
    else:
        if s == []:
            print(f'#{tc} 1')
        else:
            print(f'#{tc} 0')