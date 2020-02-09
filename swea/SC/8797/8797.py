'''
4구역
----------------
T
N
NxN 당근의 개수
---------------
'''
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

T = int(input())
for tc in range(1, T+1):
    N = int(input().strip())
    carrot = [list(map(int, input().strip().split())) for _ in range (N)]

    max_carrot = 0
    min_carrot = 1000000
    for x in range(4):
        if x != 0:
            carrot = rotate_90(carrot)
        i = 0
        temp = 0
        while N-2*i > 0:
            temp += sum(carrot[i][i:N-i])
            i += 1
        max_carrot = temp if temp > max_carrot else max_carrot
        min_carrot = temp if temp < min_carrot else min_carrot
    print(f'#{tc} {max_carrot-min_carrot}')
