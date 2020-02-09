'''
줄기의 갯수, 가장 긴 줄기 고구마수
T
N
N개 고구마수
--------------------
단조구간 > 갯수
'''
def my_sum(data, a, b):
    res = 0
    for i in range(a, b+1):
        res += data[i]
    return res

# import sys
# sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input().strip())
    sweat = list(map(int, input().strip().split()))

    start, end, max_l, max_v, cnt, i = 0, 0, 0, 0, 0, 0
    while i <= N-1:
        if i != N-1 and sweat[i] < sweat[i+1]:
            end = i+1
            i += 1
        else:
            if start != end:
                cnt += 1
                if (end-start) > max_l:
                    max_l, max_v = (end-start), my_sum(sweat, start, end)
                elif (end-start) == max_l:
                    max_v = my_sum(sweat, start, end) if my_sum(sweat, start, end) > max_v else max_v
            start, end = i+1, i+1
            i += 1
    print(f'#{tc} {cnt} {max_v}')
    
    '''
    마지막 X
    start, end = N-1, N-1
    마지막 O
    start, end = i, N-1
    '''