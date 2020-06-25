import sys
sys.stdin = open('input16235.txt')
# sys.stdin = open('input.txt')

from collections import deque

def sim(K):
    year = 0
    while year != K:
        gen = []
        for r in range(N):
            for c in range(N):
                temp = 0
                for i in range(len(trees[r][c])):
                    if land[r][c] >= trees[r][c][i]:
                        land[r][c] -= trees[r][c][i]
                        trees[r][c][i] += 1
                        if not trees[r][c][i] % 5:
                            gen.append( (r,c) )
                    else:
                        for _ in range(len(trees[r][c])-i):
                            # 여름 : 봄에 죽는 나무 양분화
                            land[r][c] += (trees[r][c].pop()) // 2
                        break
        # 가을 : 번식
        for r, c in gen:
            for dr, dc in [(-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1), (0,-1), (0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < N:
                    trees[nr][nc].appendleft(1)

        # 겨울 : 개간
        for r in range(N):
            for c in range(N):
                land[r][c] += A[r][c]

        year += 1
    return

T = 8
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # NxN 땅, M개 초기나무, K 년후
    A = [list(map(int,input().split())) for _ in range(N)] # 겨울마다 개간
   
   
    land = [[5]*N for _ in range(N)] # 땅
    trees = [[deque([]) for _ in range(N)] for _ in range(N)] # 땅에 심겨진 나무들

    for _ in range(M):
        r, c, age = map(int, input().split())
        trees[r-1][c-1].append(age)

    sim(K)

    cnt = 0
    for r in range(N):
        for c in range(N):
            cnt += len(trees[r][c])
    print(cnt)