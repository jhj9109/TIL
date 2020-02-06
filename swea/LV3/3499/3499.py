import sys
sys.stdin = open('sample_input.txt')
'''
T
N
N개카드

교대로 출력

'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input().split()
    res = []
    a = N//2 if not(N%2) else N//2 + 1
    for i in range(N // 2):
        res.append(cards[i])
        res.append(cards[i + a])
    if N%2:
        res.append(cards[N//2])
    result = ' '.join(res)
    print(f'#{tc} {result}')