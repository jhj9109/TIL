import sys
sys.stdin = open('input1949.txt')
'''
5:05 ~ 5:43 1차 ,2차 코딩완료 / 디버깅 시작
5:43 ~ 5:52 : 1차 디버깅 완료 >>> 정상도 공사 가능 발견
5:52 ~ 6:06 : 2차 디버깅 완료 >>> visited 주범임을 발견 >>> 삭제
---1시간 문제 해결 끝---
T = 50, 15초
N : 3~8 NxN 맵크기
K : 1~6 공사 가능 깊이
지형의 높이 : 1~20 , 1보다 작게도 가능

규칙
1. 가장 높은 봉우리에서 시작
2. 낮은지형 4방향 연결
3. 한곳만 공사 가능

힌트
1. N이 크지 않다 >>> 64가지 먼저 조정하고 시작할까?
2. N^2 * K = 300가지.

# 점점 감소하는 수열 >>> 중복 우려 X (v : 기존의 등산로가 깍이지 않도록 보호하는 존재)
'''
def max_return(): # max_d : 주어진 맵에서 봉우리 좌표값 [(r,c),...], 높이값 리턴
    ret_lst = []
    maxv = 0
    for r in range(N):
        for c in range(N):
            if d[r][c] > maxv:
                ret_lst = [(r,c)]
                maxv = d[r][c]
            elif d[r][c] == maxv:
                ret_lst.append((r,c))
    return ret_lst , maxv

def go():
    for bong in bongs:
        for r in range(N):
            for c in range(N):
                if (r,c) != bong:
                    d_val = d[r][c]
                    for i in range(1, K+1):
                        d[r][c] = d_val - i
                        road(bong)  # road : 주어진 시작점을 기준으로, 맵을 가능한 경우로 수정후 탐색 시작
                    d[r][c] = d_val

def road(start): # road : 주어진 맵과 시작점에서 가장 긴 산책로 탐색
    global res
    s = [start]
    cnt = [1]
    while s:
        r, c = s.pop()
        now = cnt.pop()
        if now > res:
            res = now
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr <= N-1 and 0 <= nc <= N-1 and d[r][c] > d[nr][nc]:
                s.append((nr,nc))
                cnt.append(now + 1)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    bongs, bong_height = max_return() # max_d : 봉우리의 좌표리스트, 높이 리턴
    go()
    print(f'#{tc} {res}')