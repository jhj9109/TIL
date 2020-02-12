import sys
sys.stdin = open('input.txt')

def max_idx(data):
    max_num = data[0]
    max_idx = 0
    for i in range(1, len(data)):
        (max_num,max_idx) = (data[i], i) if data[i] > max_num else (max_num, max_idx)
    return max_idx

def s_b_idx(data):
    d0 = list(data[i] for i in range(len(data)) if not(i%2))
    d1 = list(data[i] for i in range(len(data)) if (i%2))
    idx0 = max_idx(d0)*2
    idx1 = max_idx(d1)*2+1
    s_idx, b_idx = (idx1, idx0) if idx0 > idx1 and idx0 != 5 else (idx0, idx1)
    return s_idx, b_idx

K = int(input())
d = []
idx = []
for _ in range (6):
    n, l = map(int, input().split())
    d.append(l)

i1, i2 = s_b_idx(d)

res = d[i1] * d[i2] - d[(i1+3)%6] * d[(i2+3)%6]
print(res * K)