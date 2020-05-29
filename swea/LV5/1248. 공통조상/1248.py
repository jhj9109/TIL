import time
start_time = time.time()

import sys
sys.stdin = open('input1248.txt')

def go(a, b):
    both_parent = (findP(a, b))
    childs = findC(both_parent)
    return (both_parent, childs)

def findP(a, b):
    a_parents = []
    temp = a
    while data[temp][2]:
        a_parents.append(data[temp][2])
        temp = data[temp][2]
    temp = b
    while data[temp][2] not in a_parents:
        temp = data[temp][2]
    return data[temp][2] #공통 조상

def findC(a):
    s = [a]
    cnt = 0
    while s:
        now = s.pop()
        cnt += 1
        if data[now][0]:
            s.append(data[now][0])
        if data[now][1]:
            s.append(data[now][1])
    return cnt


T = int(input())
for tc in range(1, T+1):
    V, E, target1, target2 = map(int, input().split()) #공통조상 찾을 타겟
    t = list(map(int, input().split())) # E개의 간선
    data = [[0] * 3 for _ in range(V+1) ] #1~V개의 정점 Left, Right, Parent

    for i in range(0, E*2, 2):
        # 부모에게 자식 등록
        if not data[t[i]][0]:
            data[t[i]][0] = t[i+1]
        else:
            data[t[i]][1] = t[i+1]
        # 자식에게 부모 등록
        data[t[i+1]][2] = t[i]

    res = go(target1, target2)
    print(f'#{tc} {res[0]} {res[1]}')
print(time.time() - start_time, 'seconds')