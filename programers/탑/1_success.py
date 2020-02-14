def solution(h):
    ans = [0] * len(h)
    for i in range(1, len(h)):
        for j in range(i-1, -1, -1):
            if h[j] > h[i] :
                ans[i] = j+1
                break
    return ans