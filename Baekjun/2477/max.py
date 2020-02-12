def max_pop(data):
    max_num = data[0]
    max_idx = 0
    for i in range(1, len(data)):
        (max_num,max_idx) = (data[i], i) if data[i] > max_num else (max_num, max_idx)
    data.pop(max_idx)
    return data

def max_idx(data):
    max_num = data[0]
    max_idx = 0
    for i in range(1, len(data)):
        (max_num,max_idx) = (data[i], i) if data[i] > max_num else (max_num, max_idx)
    return max_idx

def s_b_idx(data):
    d0 = list(data[i] for i in len(data) if not(i%2))
    d1 = list(data[i] for i in len(data) if (i%2))
    idx0 = max_idx(d0)*2
    idx1 = max_idx(d1)*2+1
    s_idx, b_idx = (idx1, idx0) if idx0 > idx1 else (idx0, idx1)
    return s_idx, b_idx