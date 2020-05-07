import sys
sys.stdin = open('input5201.txt')
'''
A > B 도시 운반
N개 컨테이너, M대의 트럭
------------------------
가장 큰 컨테이너 > 가장 큰 트럭
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split())) # 화물 무게
    t = list(map(int, input().split())) # 트럭 적재용량
    t_used = [0]*M

    res = 0

    w.sort(reverse=True)
    t.sort()
    for i in range(N):
        for j in range(M):
            if w[i] <= t[j] and not t_used[j]:
                t_used[j] = w[i]
                break
    print(f'#{tc} {sum(t_used)}')
