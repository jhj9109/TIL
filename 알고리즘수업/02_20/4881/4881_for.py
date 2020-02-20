import sys
sys.stdin = open('sample_input4881.txt')

def go(field, N):
    res = 1000000
    x, cnt = 0, 0
    s = []
    X, Y = [], []
    for w in range(N):
        if w not in Y:
            s.append((x, w)) #스택에 푸쉬
    while s:
        x, y = s.pop() #스택에서 팝

        while len(Y) < x or x < len(Y):
            cnt -= field[X.pop()][Y.pop()]

        X.append(x)
        Y.append(y) #y열 사용 기록

        cnt += field[x][y] #합계
        if cnt < res:
            if len(Y) == N: #순열완성
                res = cnt if cnt < res else res #최소값 교체
            else:
                for w in range(N): 
                    if (0<=x+1<=N-1) and (w not in Y):
                        s.append((x+1, w)) #스택에 푸쉬
    return res


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {go(field, N)}')