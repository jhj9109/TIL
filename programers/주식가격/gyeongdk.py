from collections import deque
def solution(prices):
    answer = deque()
    temp = deque()
    for _ in range(len(prices)):
        p = prices.pop()
        s = 0
        for t in temp:
            if p <= t:
                s += 1
            else:
                s += 1
                break
        temp.appendleft(p)
        answer.appendleft(s)
    return list(answer)