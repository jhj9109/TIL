def solution(pr, sp):
    '''
    pr : 프로세스 현재 완성도
    sp : 단위 시간당 프로세스 진행도
    -((pr[0]-100)//sp[0] : 0초를 기준으로 프로세스 개발 완성까지 걸리는 시간
    a : [각 배포시간, 배포에 포함되는 프로세스 갯수] 
    '''
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