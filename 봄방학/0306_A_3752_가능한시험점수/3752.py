import sys
sys.stdin = open('input3752.txt')
'''
N+1 x (maxv+1) 배열 형성
단계별(r) 가능한 점수를 누적한다(line:16,17)
v[-1]==1 : 최종 가능한 점수들
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    maxv = sum(data)
    v = [ [1]+[0]*(maxv) for _ in range(N+1) ]
    for r in range(N):
        for c in range(maxv+1):
            if v[r][c]:
                v[r+1][c] = 1
                v[r+1][c+data[r]] = 1
    print(f'#{tc} {sum(v[-1])}')