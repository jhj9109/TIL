import sys
sys.stdin = open("input2806.txt")

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
    if n != 0:
        cnt = 0
        x = N - n
        for y in range(N):
            if sum(d[x][0:N+1]) == 0 and sum((list(zip(*d))[y])) == 0 and cross(N, d, x, y):
                d[x][y] = 1
                cnt += chess(N, d, n-1) #5->4....2->1
                d[x][y] = 0
            else:
                pass
        return cnt # n >= 1
    else:
        return 1 # n == 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = [[0] * N for _ in range(N)]
    result = chess(N, d, N)
    print(f'#{tc} {result}')