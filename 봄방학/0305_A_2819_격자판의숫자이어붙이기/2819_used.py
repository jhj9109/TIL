import sys
sys.stdin = open ('input2819.txt')
# u사용 go호출 : 356    / 연산횟수 8019
# 일반  go호출 : 23864 / 연산횟수 211759
def go(r, c, st):
    global cnt
    global u
    global res
    cnt += 1
    if len(st) == 7:
        # cnt += 1
        if st not in res:
            # cnt += 1
            res.append(st)
            return
    else:
        for k in range(4):
            # cnt += 7
            nr, nc  = r+dr[k], c+dc[k]
            if 0 <= nr <= 3 and 0 <= nc <= 3 and st + field[nr][nc] not in u[nr][nc]:
                u[nr][nc].append( st + field[nr][nc] )
                # cnt += 1
                go(nr, nc, st + field[nr][nc] ) 

    
dr = [0, 0, 1,-1]
dc = [1,-1, 0, 0]    
T = int(input())
for tc in range(1, T+1):
    field = [input().split() for _ in range(4)]
    u = [list([] for _ in range(4)) for _ in range(4)]
    res = []
    cnt = 0
    for r in range(4):
        for c in range(4):
            u[r][c].append( field[r][c] )
            go(r, c, field[r][c])
    print(f'#{tc} {len(res)}, {cnt}')