import sys
sys.stdin = open('input1247.txt')

def dfs(k, now, dis):
    global res
    if dis > res:
        return
    if k == N:
        dis += abs(people[now][0]-home[0]) + abs(people[now][1]-home[1])
        res = dis if dis < res else res
        return
    for w in range(1, N+1):
        if not v[w]:
            v[w] = 1
            plus = abs(people[now][0]-people[w][0]) + abs(people[now][1]-people[w][1])
            dfs(k+1, w, dis + plus)
            v[w] = 0 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    people = []
    for i,v in enumerate(list(map(int, input().split()))): #회사 집 고객 N명
        if i&1:
            people.append( (temp, v))
        else:
            temp = v
    home = people.pop(1)

    res = float('inf')
    v = [0] * (N+1)

    dfs(0, 0, 0)
    
    print(f'#{tc} {res}')
