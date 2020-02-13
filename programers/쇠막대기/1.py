#예시 ()(((()())(())()))(()) , 출력 17
def solution(s):
    N = len(s)
    d = []
    i = 1
    res = 0
    while i <= (N):
        if s[-i] == ')' and s[-(i+1)] == '(':
            d = [x+1 for x in data]
            i += 2
        elif s[-i] == ')':
            d.append(1)
            i += 1
        elif s[-i] == '(':
            if d != []:
                res += d.pop()
            i += 1
        else:
            print('NO')
            break
    return res

data = input()
print(solution(data))