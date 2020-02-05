'''
----입력----
T
N
-----데이터-----
NxN보드

'''


def cross(N, d, x, y):
    xx = [1, -1, 1, -1]
    yy = [1, -1, -1, 1]
    if d[x][y] == 1:
        return False
    for i in range(4):
        n = 1
        while (0 <= x + xx[i] * n <= N-1) and (0 <= y + yy[i] * n <= N-1):
            if d[x + xx[i ]* n][y + yy[i] * n] == 0:
                n += 1
            else:
                return False
    return True

def chess(N, d, n):
    """
    #n : 놓아야할 체스말 , N-n  놓인 체스말
    #chess(N, d, n-1) 직전에서 체스를 잘 놓는다.
    #코드 :  서로 닿지않는 곳에 체스를 잘 놓는다.
    #        리턴[0] : T/F 리턴[1] : d
    #chess(N, d, n) >>> chess(N, d, n-1) >>> chess(N, d, 1)
    #n >>> 0
    """
    print('-' * 70)

    if n != 0:
        cnt = 0
        x = N - n
        for y in range(N):
            print(f'\n{n}탐색', d ,end=' ')
            print( f'x:{x}, y:{y}, sum:{sum(d[x][0:N+1])},{sum(d[0:N+1][y])}, cross:{cross(N, d, x, y)}' )
            if sum(d[x][0:N+1]) == 0 and sum((list(zip(*d))[y])) == 0 and cross(N, d, x, y):
                print('OK')
                d[x][y] = 1
                print(f'chess({N}, {n-1}, {d} 소환')
                cnt += chess(N, d, n-1) #5->4....2->1
                d[x][y] = 0
            else:
                pass
        return cnt # n >= 1
        print('fail')
        print(f'\n 리턴 cnt:{cnt}\n')
    else:
        print(f'\n리턴 1\n')
        return 1 # n == 0

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    d = [[0] * N for _ in range(N)]
    print(f'chess({N}, {N}, {d} 소환')
    result = chess(N, d, N)

    print(f'#{tc} {result}')