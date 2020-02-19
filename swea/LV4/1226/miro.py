import sys
sys.stdin = open('sample_input.txt')

def go(field, x, y, cnt, res):
    dx = [0, 0, 1,-1]
    dy = [1,-1, 0, 0]

    for i in range(4): #4방향 서치
        if (0<=x+dx[i]<=N-1) and (0<=y+dy[i]<=N-1): #필드경계 조건
            if field[x+dx[i]][y+dy[i]] == 3: #도착

                cnt[0] += 1
                res.append(cnt[0]-1) #결과값에 지금까지 결과 덧셈
                return

            if field[x+dx[i]][y+dy[i]] == 0: #길 존재

                field[x+dx[i]][y+dy[i]] = 1 #왔던길 삭제
                cnt[0] += 1
                go(field, x+dx[i], y+dy[i], cnt, res)

                cnt[0] -= 1
                field[x+dx[i]][y+dy[i]] = 0

def return_start(field):
    for x in range(N):
        for y in range(N):
            if field[x][y] == 2:
                return x, y

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(int(x) for x in input()) for _ in range(N)]
    X, Y = return_start(field)
    
    res = []
    cnt = [0]
    go(field, X, Y, cnt, res)
    if len(res) == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {min(res)}')