import sys
sys.stdin = open('input5656.txt')
'''
3시간
구슬 N번 발사 : 1~4
W 2~12 , H 2~15
명중시 상하좌우 (숫자-1)만큼 추가 제거
'''

def check(data): #전체 필드 돌며, 남은 블록 수 계산
    cnt = 0
    for r in range(H):
        for c in range(W):
            cnt += 1 if data[r][c] != 0 else 0
    return cnt

def shot(r, c, inputs): # 슈팅
    ret = [inputs[k][:] for k in range(H)]
    v = [[False]*(W) for _ in range(H)]
    s = [(r,c)]
    v[r][c] = True
    ret[r][c] = 0 
    while s:
        r, c = s.pop()
        n = inputs[r][c] - 1
        if n > 0:
            for k in range(4):
                for l in range(1, n+1):
                    nr, nc = r+dr[k]*l, c+dc[k]*l
                    if 0<=nr<=H-1 and 0<=nc<=W-1 and not v[nr][nc] and inputs[nr][nc] != 0:
                        v[nr][nc] = True
                        ret[nr][nc] = 0
                        s.append((nr,nc))
    my_fill(ret)
    return ret

def my_fill(ret): # 구멍 채우기
    for c in range(W):    
        for r in range(H-1, 0, -1):
            if ret[r][c] == 0: # 구멍 존재
                nr = r - 1
                while nr >= 0:
                    if ret[nr][c] != 0:
                        ret[r][c], ret[nr][c] = ret[nr][c], 0
                        break # 블록으로 구멍 채우기
                    nr -= 1
                else:
                    break # 구멍 위로 블록X

def go(n, inputs):
    global res
    if res != 0: #소박한 백트래킹
        if n == N:
            temp = check(inputs) #남은 블록 수
            res = temp if res > temp else res
        else:
            flag = True
            for c in range(W): # n번째 슈팅
                for r in range(H):
                    if inputs[r][c] != 0:
                        go(n+1, shot(r, c, inputs))  
                        flag = False
                        break
            if flag: # n번째 맞출 블록이 없다면 == 모든 블록 파괴
                res = 0

dr = [0, 0, 1,-1]
dc = [1,-1, 0, 0]
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(H)]
    res = W*H
    go(0, field)
    print(f'#{tc} {res}')