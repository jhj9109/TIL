def f(n, k):
    global minV
    if n == k: #순열 1개 완성
        s = 0
        for i in range(k):
            s += arr[i][p[i]] #p[i] i번 행에서 선택한 열 번호
    
    else:
        for i in range(k): # used를 왼쪽부터 탐색 (사용할수 있는 숫자 검색)
            if u[i] == 0: # 이미 사용한 숫자가 아니면
                u[i] = 1
                p[n]
                f(n+1, k) #다음 자리를 결정하러 이동
                u[i] = 0

A = [1,2,3]
p = [0] * len(A)
u = [0] * len(A)
f(0, len(A))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]