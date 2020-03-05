import sys
sys.stdin = open ('input2819.txt')
'''30분
중복가능 서로다른 7자리수
'''
# u사용 go호출 : 356    / 연산횟수 8019
# 일반  go호출 : 23864 / 연산횟수 211759
# int형도 문제는 없는것 확인 > 7자리 고정 > 앞자리 0 > 7-n자리 숫자로 변형
def go(r, c, res, st):
    global cnt
    cnt += 1
    if len(st) == 7:
        # cnt += 1
        if st not in res:
            res.append(st)
            # cnt += 1
            return
    else:
        for k in range(4):
            # cnt += 5
            nr, nc = r+dr[k], c+dc[k]
            if 0 <= nr <= 3 and 0 <= nc <= 3:
                go(nr, nc, res, st+field[nr][nc]) 

    
dr = [0, 0, 1,-1]
dc = [1,-1, 0, 0]    
T = int(input())
for tc in range(1, T+1):
    field = [input().split() for _ in range(4)]
    res = []
    cnt = 0
    for r in range(4):
        for c in range(4):
            go(r, c, res, field[r][c])
    print(f'#{tc} {len(res)}, cnt:{cnt}')