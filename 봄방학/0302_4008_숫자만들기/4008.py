import sys
sys.stdin = open ('input4008.txt')
'''
10:06
N : 3~ 12
숫자 순서 변경 X
'''
def calc(n1, n2, ope):
    if ope == 0:
        return n1 + n2
    if ope == 1:
        return n1 - n2
    if ope == 2:
        return n1 * n2
    if ope == 3:
        return int(n1 / n2)


def go(nums):
    used = [[opes[0], opes[1], opes[2], opes[3]]] #연산자 사용횟수
    s = [nums[0]] #
    idx = [0]
    res = []
    while s:
        n = s.pop()
        u = used.pop()
        i = idx.pop()
        #push
        if i == N-1:
            res.append(n)
        else:
            for k in range(4):
                if u[k]:
                    u[k] -= 1
                    used.append(u[:])
                    u[k] += 1
                    s.append(calc(n, nums[i+1], k))
                    idx.append(i+1)
    return max(res) - min(res)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    opes = list(map(int, input().split())) #연산자 +, -, *, / N-1개
    nums = list(map(int, input().split())) # N개의 숫자
    print(f'#{tc} {go(nums)}')