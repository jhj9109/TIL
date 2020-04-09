import sys
sys.stdin = open('input5122.txt')
'''
I 번쨰 인서트
D 번쨰 딜리트
C 번째 체인지
'''
def go(c):
    if c[0] == 'D':
        del d[int(c[1])]
    elif c[0] == 'C':
        d[int(c[1])] = int(c[2])
    elif c[0] == 'I':
        d.insert(int(c[1]), int(c[2]))
    else:
        print('error')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    d = list(map(int, input().split()))
    for _ in range(M):
        go(input().split())
    if len(d) <= L:
        print(f'#{tc} {-1}')
    else:
        print(f'#{tc} {d[L]}')