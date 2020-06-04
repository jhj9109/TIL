import time
start_time = time.time()

import sys
sys.stdin = open('input1248.txt')

def go(a, b):
    both_parent = (findP(a, b))
    preorder(both_parent)
    return both_parent

def findP(a, b):
    a_parents = []
    temp = a
    p = data[a][2]
    while p:
        a_parents.append(p)
        p = data[p][2]
    p = data[b][2]
    while p not in a_parents:
        p = data[p][2]
    return p #공통 조상

def preorder(node):
    global cnt2
    if node != 0:
        cnt2 += 1
        preorder(data[node][0])
        preorder(data[node][1])

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

    cnt2 = 0
    res = go(target1, target2)
    print(f'#{tc} {res} {cnt2}')
print(time.time() - start_time, 'seconds')