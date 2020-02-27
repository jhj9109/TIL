import sys
sys.stdin = open('input6485.txt')
#예제출력 #1 1 2 2 1 1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    buss = [list(int(x) for x in input().split())  for _ in range(N)]
    # print (buss)
    P = int(input())
    stops = [int(input()) for _ in range(P)]
    # print( stops)
    res = []
    for stop in stops:
        cnt = 0
        for bus in buss:
            cnt += 1 if bus[0] <= stop <= bus[1] else 0
        res.append(cnt)
    print(f'#{tc}', end=' ')
    print(*res, sep=' ')
