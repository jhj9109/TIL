import sys
sys.stdin = open('sample_input.txt')

'''
11일 11시 1분
D 일 H시 M분
T
D H M
'''
T = int(input())
for tc in range(1, T+1):
    D, H, M = map(int, input().split())
    date1 = 11 + 11*60 + 11*60*24
    date2 = M + H*60 + D*60*24
    if date1 > date2:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {date2-date1}')