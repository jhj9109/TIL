import sys
sys.stdin = open('input17136.txt')
#예제출력 : 0, 4, 5, -1, 7, 4, 6, 5

'''11:26
5종류 색종이, 5개씩 
10x10 종이 : 1에는 색종이가 덮여져야함
겹침X, 경계초과X
필요한 색종이 최소 개수 or 불가능 -1
'''
def check_field(x,y,n):
    # while 0<=x+dx[k]<=9 and 0<=y+dy[k]<=9:
    i = 1
    while (0<= y+i <=9) and (not field[x][y+i]) and i != 5:#get N : NxN 
        i += 1
    flag = False
    if i > 1:
        for j in range(1, i):#x축
            for k in range(0, i):#y축
                if (x+j> 9) or field[x+j][y+k]:
                    flag = True
                if flag:
                    break
            if flag:
                break
        else:
            j += 1
        N = j
    else:
        N = i
    #get : N
    for p in range(x, x+N):
        for q in range(y, y+N):
            field[p][q] = n
    return N
dx = [0, 1, 1]
dy = [1, 0, 1]
T = 8
for tc in range(1, T+1):
    field = [list(False if x == '1' else True for x in input().split()) for _ in range(10)]
    # for f in field:
    #     print(f)
    # print('')
    d = [0]*6
    n = 2
    for x in range(10):
        for y in range(10):
            if not field[x][y]:
                d[check_field(x,y,n)] += 1
                n += 1
    #섬의 갯수 n-2
    # print(field)
    # print(n)
    # print(d)
    res = 0
    for v in d[1:]:
        if v > 5:
            res = -1
            break
        res += v
    print(res)