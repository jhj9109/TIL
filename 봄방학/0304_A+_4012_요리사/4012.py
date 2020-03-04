import sys
sys.stdin = open('input4012.txt')
'''
1시간
2명의 손님에게 음식
식재료  N / 2개씩
두가지 요리
N :4~16, field값 :1~20000
'''
def dfs(k, lst):
    global res
    if len(lst) == N//2:
        res = min(res, abs(get_sum(lst) - get_sum(get_lst(lst)) ))
        return
    if len(lst) <= (N//2)-1:
        dfs(k+1, lst+[k])
    if k-len(lst) <= (N//2)-1:
        dfs(k+1, lst)

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
    res = 1000000
    dfs(0, [])
    print(f'#{tc} {res}')