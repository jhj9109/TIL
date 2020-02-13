def solution(data):
    s = list(data)
    res = 0
    d = []
    while s:
        temp = s.pop()[:]
        if temp == '(':
            res += d.pop() if d != [] else 0
        else:
            temp2 = s.pop()[:]
            if temp2 == '(':
                d = [x+1 for x in d]
            else:
                d.append(1)
    return res

dd = input()
print(solution(dd))