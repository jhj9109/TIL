'''
8 : max-min <= K
1 : min <= 1 <= min+H 
'''
import sys
sys.stdin = open('input.txt')

def my_check(field, x, y, K, H):
    dx = [-1, -1, -1, 0, 1, 1,  1,  0]
    dy = [-1,  0,  1, 1, 1, 0, -1, -1]
    min_field, max_field = field[x+dx[0]][y+dy[0]], field[x+dx[0]][y+dy[0]]
    for i in range(1, 8):
        min_field = field[x+dx[i]][y+dy[i]] if field[x+dx[i]][y+dy[i]] < min_field else min_field 
        max_field = field[x+dx[i]][y+dy[i]] if field[x+dx[i]][y+dy[i]] > max_field else max_field
    if (max_field - min_field) <= K and 0 <= (field[x][y] - min_field) <= H:
        return True
    else:
        return False

T = int(input().strip())
for tc in range(1, T+1):
    N, M, K, H = map(int, input().strip().split())
    field = [list(map(int, input().strip().split())) for _ in range(N)]
    cnt = 0
    for x in range(1, N-1):
        for y in range(1, M-1):
            if my_check(field, x, y, K, H):
                cnt += 1
    print(f'#{tc} {cnt}')