import sys
sys.stdin = open('input1952.txt')
def go():
    res = year
    cnt = 0
    i = 0
    s = [(0, 0)]
    while s:
        i, cnt = s.pop()
        if i <= 11:
            s.append( (i+3, cnt+quarter) )
            s.append( (i+1, cnt+month) )
            s.append( (i+1, cnt+day*plans[i]) )
        else:
            res = cnt if res > cnt else res

    return res

T = int(input())
for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())
    plans = [int(x) for x in input().split() ]
    print(f'#{tc} {go()}')