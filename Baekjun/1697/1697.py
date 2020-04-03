'''9:55~
0<=N,K<=100,000
주인공 : 걷기, 순간이동
걷기 : X±1
순간이동 : X*2
가장 빨리 찾는 시간?
BFS
'''
import sys
sys.stdin = open('input1697.txt')

def go(N, K):
    nk = abs(N-K)
    v = [0]*(100001)
    q = [N]
    v[N] = 1
    while q:
        now = q.pop(0)
        if now == K:
            return v[now]-1
        else:
            if now <= 99999 and v[now+1] == 0:
                q.append(now+1)
                v[now+1] = v[now] + 1
            if now >= 1 and v[now-1] == 0:
                q.append(now-1)
                v[now-1] = v[now] + 1
            if now <= 50000 and v[now*2] == 0:
                q.append(now*2)
                v[now*2] = v[now] + 1

N, K = map(int, input().split())
print(go(N, K))