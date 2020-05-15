import sys
sys.stdin = open('input2806.txt')

def go(n):
    global res
    if n == N:
        res += 1
        return
    for i in range(N):
        if not m[i] and not dia1[n+i] and not dia2[n-i+(N-1)]:
            m[i] = dia1[n+i] = dia2[n-i+(N-1)] = 1
            go(n+1)
            m[i] = dia1[n+i] = dia2[n-i+(N-1)] = 0
    return     

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    res = 0
    m = [0] * N
    dia1 = [0] * (2*N-1) # 상향대각 : i+j : 0 ~ 2(N-1)
    dia2 = [0] * (2*N-1) # 하향대각 : i-j : -(N-1) ~ (N-1) >>> (i-j)+(N-1)
    go(0)
    print(f'#{tc} {res}')