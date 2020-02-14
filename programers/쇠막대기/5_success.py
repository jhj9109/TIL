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