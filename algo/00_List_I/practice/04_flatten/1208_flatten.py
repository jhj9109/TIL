import sys

sys.stdin = open('input.txt')

def get_min_max(data):
    max_num = 0
    min_num = data[0]
    max_idx = 0
    min_idx = 0
    for i in range(len(data)):
        if data[i]>max_num:
            max_num=data[i]
            max_idx=i
        if data[i]<min_num:
            min_num=data[i]
            min_idx=i
    return max_idx, min_idx

T = 10
for T in range(T):
    N = int(input())
    cols = list(map(int, input().strip().split()))
    
    for n in range(N):
        max_i, min_i = get_min_max(cols)
        
        if cols[max_i]-1 == cols[min_i]:
            break
        max_i, min_i = get_min_max(cols)
        cols[min_i] +=1
        cols[max_i] -=1
        if min(cols) == max(cols):
            break
    result = max(cols)-min(cols)
    print('#{} {}'.format(T+1, result))