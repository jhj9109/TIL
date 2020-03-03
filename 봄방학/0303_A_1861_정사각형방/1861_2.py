import sys
sys.stdin = open('input1861.txt')
'''
일반 반복문 버전
1. 1~N^2 배열 v를 만든다.
2. field를 돌며 주변에 +1인 칸이 존재하면 v[field[r][c]] = True로 한다.
3. 배열 v에서 최장 True 배열길이를 찾는다. (길이 같으면, 왼쪽 배열이 우선)
'''
def ret_v(field):
    v = [False]*(N**2+1)
    for r in range(N):
        for c in range(N):
            for k in range(4): 
                nr, nc = r+dr[k], c+dc[k]
                if 0 <= nr <= N-1 and 0 <= nc <= N-1 and field[r+dr[k]][c+dc[k]] - field[r][c] == 1:
                    v[field[r][c]] = True
                    break
    return v
def ret_res(data, res):
    cnt = 1
    start = 1
    for i in range(1, len(data)):
        if data[i]:
            cnt += 1
        else:
            if cnt > res[1]:
                res[0], res[1] = start, cnt 
            start = i + 1
            cnt = 1
    return

dr = [0, 0, 1,-1]
dc = [1,-1, 0, 0]
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    res = [0, 0]
    ret_res( ret_v(field), res )
    print(f'#{tc} {res[0]} {res[1]}')