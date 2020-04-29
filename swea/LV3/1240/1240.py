def go():
    for i in range(N):
        for j in range(M-1, 54, -1):
            if d[i][j] == '1':
                return go2(i, j-55)

def go2(i, j):
    lst = []
    for n in range(8):
        lst.append(k[ d[i][j+(n*7):j+(n*7)+7] ])
    if ( (lst[0]+lst[2]+lst[4]+lst[6])*3 + lst[1]+lst[3]+lst[5]+lst[7] )%10:
        return 0
    else:
        return sum(lst)

k = {
    '0001101':0,    '0011001':1,    '0010011':2,    '0111101':3,
    '0100011':4,    '0110001':5,    '0101111':6,    '0111011':7,
    '0110111':8,    '0001011':9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [ input() for _ in range(N) ]
    flag = False
    print(f'#{tc} {go()}')