import sys
sys.stdin = open('input1247.txt')

from itertools import permutations
def cal(lst):
    global res
    cnt = 0

    for n in range(N+1):
        cnt += abs(people[lst[n]][0] - people[lst[n+1]][0]) + abs(people[lst[n]][1] - people[lst[n+1]][1])
        if cnt > res:
            return
    res = cnt
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    people = []
    res = 200 * (N+2)
    lst = list(range(N))

    for i,v in enumerate(list(map(int, input().split()))):
        if i&1:
            people.append( (temp, v))
        else:
            temp = v
    
    temp = people.pop(1)
    people += [temp]
    lst = list(range(1, N+1))
    for permutation in permutations(lst, N):
        cal([0]+list(permutation)+[N+1])
    print(f'#{tc} {res}')