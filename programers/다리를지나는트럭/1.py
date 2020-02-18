from collections import deque


def solution(bridge_length, weight, truck_weights):
    '''
    l, w : 문제에서 주어진 다리길이, 최고 하중
    d3 : 주어진 트럭 데이터를 deque로 생성
    d1, n : 통과한 트럭 수, 주어진 트럭 수(목표)
    d2 : 다리 길이만큼 생성한 deque, 한개씩 빼고 더해 차량의 이동을 표현
    cw : 다리 위의 트럭 하중
    '''
    l, w= bridge_length, weight
    d1, d2, d3= 0, deque([0]*l), deque(truck_weights)
    t, cw, n = 0, 0, len(d3)
    
    while d1 != n:
        t += 1
        temp = d2.popleft()
        cw -= temp
        d1 += 1 if temp else 0
        
        if len(d3) and w >= cw + d3[0]:
            cw += d3[0]
            d2.append(d3.popleft())
        else:
            d2.append(0)
    return t

a, b, c = 	2, 10, [7, 4, 5, 6]
print(solution(int(a), int(b), c))