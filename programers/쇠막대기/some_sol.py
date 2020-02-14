def solution(d):
    res = 0
    s = 0
    raser = False
    for c in d:
        if c == ')':
            s, res, raser = s-1, res+s, False if raser else s-1, res+1, raser
        else:
            s, raser = s+1, True
    return res

#1-1인덱스 사용
def solution(d):
    res = 0
    s = 0
    raser = False
    for i in range(len(d)):
        if d[i] == ')':
            s -= 1
            if d[i-1] == '(':
                res += s
            else:
                res += 1
        else:
            s += 1
    return res

#1-2데이터&flag 사용
def solution(data):
    res = 0
    s = 0
    raser = False
    for d in data:
        if d == ')':
            if raser:
                s -= 1
                res += s
                raser = False
            else:
                s -= 1
                res += 1             
        else:
            s += 1
            raser = True
    return res