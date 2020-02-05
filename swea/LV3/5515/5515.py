months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

T = int(input())
for T in range(T):
    #1.1 금요일
    # 1 2 3 4 5 6 7
    # 금 토
    # 4 5
    m, d = map(int, input().strip().split())
    print('#{} {}'.format(T+1, (sum(months[0:m]) + d + 3)%7))