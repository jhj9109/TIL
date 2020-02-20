import sys
sys.stdin = open('sample_input4880.txt')

def RPSi(i1, i2, d):
    if d[i1] == 1:
        res = i2 if d[i2] == 2 else i1
        return res
    elif d[i1] == 2:
        res = i2 if d[i2]  == 3 else i1
        return res
    elif d[i1] == 3:
        res = i2 if d[i2]  == 1 else i1
        return res

def go(data, start, end):
    if start == end:
        return start
    return RPSi(go(data, start, (start+end)//2) , go(data, (start+end)//2 + 1, end) , data)

    return r[0]

T = int(input())

for tc in range(1, T+1):
    N = int(input()) #4<=N<=100
    data = list(map(int, input().split()))
    data = [-1] + data
    print(f'#{tc} {go(data, 1, N)}')
