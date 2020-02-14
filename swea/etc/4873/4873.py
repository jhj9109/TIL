import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    d = input()
    s = []
    for c in d:
        if s != []:
            if s[-1] == c:
                s.pop()
            else:
                s.append(c)
        else:
            s.append(c)
    print(f'#{tc} {len(s)}')