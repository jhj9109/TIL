import sys
sys.stdin = open('input.txt')

def to_90(data):
    N = len(data)
    ret = []
    for y in range(N):
        temp = list()
        for x in range(N):
            temp.append(data[-x+-1][y])
        ret.append(temp)
    return ret

T = int(input().strip())
for T in range(T):
    N = int(input().strip())
    
    data = list()
    for _ in range(N):
        data.append( list(map(int, input().strip().split(' '))) )
    data_90 = to_90(data)
    data_180 = to_90(data_90)
    data_270 = to_90(data_180)
    print('#{}'.format(T+1))
    for a in range(N):
        for b in range(N):
            print('{}'.format(data_90[a][b]),end='')
        print('',end=' ')
        for b in range(N):
            print('{}'.format(data_180[a][b]),end='')
        print('',end=' ')
        for b in range(N):
            print('{}'.format(data_270[a][b]),end='')
        print('')