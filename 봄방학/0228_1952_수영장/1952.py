import sys
sys.stdin = open('input1952.txt')
def go():
    res = year
    cnt = 0
    i = 1
    s = [(0, 0)]
    while s:
        i, cnt = s.pop()
        if cnt < res: # 백트래킹
            if i <= 12:
                s.append( (i+3, cnt+quarter) ) #i+1, i+2달 요금을 0으로 만들어주기 때문에, 뺼수 없는 코드
                s.append( (i+1, cnt+min(month,day*plans[i]) ) )#한달 비용, 일일권 정액권 중 저렴한 금액 선택
            else:
                res = cnt
    return res

T = int(input())
for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())
    plans = [0] + [int(x) for x in input().split() ]
    print(f'#{tc} {go()}')