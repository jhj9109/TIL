import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = sorted(list(map(int, input().split())))

    print(f'#{tc} ', end='')
    r = d[-5:][::-1]
    for i, j in zip(r, d[:5]):
        print(i, j, end=' ')
    print('')

print(d)