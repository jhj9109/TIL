from collections import deque

def div(a, b):
    res = (a // b) if a % b == 0 else (a // b) + 1
    return res

def solution(progresses, speeds):
    '''
    p : 프로세스 현재 완성도
    s : 단위 시간당 프로세스 진행도
    cnt : 배포당 포함되는 프로세스 갯수
    프로세스를 deque로 생성
    프로젝트 완성에 걸리는 시간을 각각 비교하여 cnt 더하여 결과에 합침    
    '''
    p, s = deque(progresses), deque(speeds)
    res = []
    t = div(100 - p.popleft(), s.popleft())
    cnt = 1
    while len(p) != 0:
        temp = div((100 - p.popleft()), s.popleft())
        if temp > t:
            res.append(cnt)
            t = temp
            cnt = 1
        else:
            cnt += 1
    res.append(cnt)        
    return res