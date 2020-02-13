import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    d = input()
    s = []
    for c in d:
        if s != []:
            temp = s.pop()
            if temp != c:
                s.append(temp)
                s.append(c)
        else:
            s.append(c)
    print(f'#{tc} {len(s)}')

