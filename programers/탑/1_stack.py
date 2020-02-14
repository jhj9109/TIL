def solution(h):
    ans = [0]
    for i in range(1, len(h)):
        s = []
        for j in range(i):
            if h[j] > h[i] :
                s.append(j+1)
        if len(s):
            ans.append(s.pop())
        else:
            ans.append(0)
    return ans