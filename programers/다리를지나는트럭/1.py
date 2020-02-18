from collections import deque


def solution(bridge_length, weight, truck_weights):
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