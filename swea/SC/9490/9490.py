# import sys
# sys.stdin = open('input1.txt')
from pprint import pprint
def my_pollen(data, x, y, N, M):
    dx = [-1, 1,  0,  0]
    dy = [ 0, 0, -1, -1]
    

    res, cnt = data[x][y], data[x][y]
    for i in range(4):
        k = 1
        while 0 <= x+dx[i]*k <= N-1 and 0 <= y+dy[i]*k <= M-1 and k <= cnt:
            res += data[x+dx[i]*k][y+dy[i]*k]
            k += 1
    return res

# T = int(input())
T = 1
for tc in range(1, T+1):
    # N, M = map(int, input().strip().split())
    # field = [list(map(int, input().strip().split())) for _ in range(N)]

    N, M = 5, 5
    field =[
        [3,4,1,2,3],
        [3,4,1,3,2],
        [2,3,2,4,1],
        [1,4,4,1,3],
        [2,2,3,4,4]
    ]
    pprint(field)
    max_res = 0
    for x in range(N):
        for y in range(M):
            temp = my_pollen(field, x, y, N, M)
            max_res = temp if temp > max_res else max_res
    print(f'#{tc} {max_res}')