def solution(pr, sp):
    a = []
    if len(pr) > 0:
        a.append( [-((pr[0]-100)//sp[0]) , 1] )
    else:
        return []
    for p, s in zip(pr[1:], sp[1:]):
        if a[-1][0] < -((p-100)//s):
            a.append( [-((p-100)//s) , 1] )
        else:
            a[-1][1] += 1
    return [ v[1] for v in a]