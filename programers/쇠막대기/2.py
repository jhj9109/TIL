#예시 ()(((()())(())()))(()) , 출력 17
def solution(s):
    s = list(s)
    d = []
    res = 0
    while s:
        if s.pop() == '(':
            res += d.pop() if d != [] else 0
        elif s.pop() == '(':
            d = [x+1 for x in d]
        else:
            d.append(1)
    return res

data = input()
print(solution(data))