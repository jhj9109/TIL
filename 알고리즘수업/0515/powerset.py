def backtrack(selected, k, N):
    #arr 각 노드의 선택여부 판단하는 배열,
    #k 깊이, N 목표 갯수
    candidates = [0] * 2 # 선택지 사용/사용X
    
    if k == N:
        for i in range(N):
            if selected[i]:
                print(i, end = " ")
        print()
        return
    else:
        n_candidate = make_candidate(candidates)
        for i in range(n_candidate):
            selected[k] = candidates[i]
            backtrack(selected, k+1, N)

def make_candidate(candidates):
    for i in range(len(candidates)):
        candidates[i] = i
    return len(candidates)
 
N = int(input())
backtrack([0]*N, 0, N) # 3개 원소 powerset