import sys
sys.stdin = open('input4012.txt')
def f(v, s): #0, k, 0, N
    global res
    if v == N//2:
        res = min(res, abs(get_sum(lst) - get_sum(get_lst(lst)) ))
    else:
        for w in range(s, N//2+v+1):
            lst[v] = w
            f(v+1, w+1)

def get_sum(lst):
    ret = 0
    for i in lst:
        for j in lst:
            ret += field[i][j]
    return ret

def get_lst(lst):
    return [i for i in range(N) if i not in lst]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    lst = [0]*(N//2)
    res = 1000000
    f(0, 0)
    print(f'#{tc} {res}')