def solution(d):
    answer = True
    s = []
    for c in d:
        if c == '(':
            s.append(c)
        else:
            if s == [] or s.pop() != '(':
                return False

    if s == []:
        return True
    else:
        return False
    return True