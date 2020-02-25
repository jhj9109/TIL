import sys
sys.stdin = open('input17136.txt')
#예제출력 : 0, 4, 5, -1, 7, 4, 6, 5

'''11:26 - 13:00 예제출력 성공, 백준사이트 20퍼 틀림
5종류 색종이, 5개씩 
10x10 종이 : 1에는 색종이가 덮여져야함
겹침X, 경계초과X
필요한 색종이 최소 개수 or 불가능 -1
'''
def check_field2(x,y,N):
    i, j = 0, 0
    while True: 
        if not(0<= x+i <=9 and 0<= y+j <=9) or field[x+i][y+j]:
            break
        if j == N-1:
            if i == N-1:
                print_field(x,y,N)
                return True
            i, j = i+1, 0
        else:
            j += 1
    return False

def print_field(x,y,N):
    for i in range(x, x+N):
        for j in range(y, y+N):
            field[i][j] = True
    return

dx = [0, 1, 1]
dy = [1, 0, 1]
T = 8
for tc in range(1, T+1):
    field = [list(False if x == '1' else True for x in input().split()) for _ in range(10)]

    d = [0]*6
    for N in range(5, 0, -1):
        for x in range(10):
            for y in range(10):
                if not field[x][y]:
                    if check_field2(x,y,N):
                        d[N] += 1

    res = 0
    for v in d[1:]:
        if v > 5:
            res = -1
            break
        res += v
    print(res)