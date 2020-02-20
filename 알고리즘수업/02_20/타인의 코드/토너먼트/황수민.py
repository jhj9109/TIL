from copy import deepcopy

def divide_group(n, l):
    if len(l) == 1:
        return l
    left = deepcopy(l[:(n+1)//2])
    right = deepcopy(l[(n+1)//2:])
    a = divide_group(len(left), left)
    b = divide_group(len(right), right)
    if a[0][1] == 3 and b[0][1] == 1:
        return b
    elif a[0][1] == 1 and b[0][1] == 3:
        return a
    elif a[0][1] == b[0][1]:
        if a[0][0] < b[0][0]:
            return a
        else:
            return b
    else:
        if a[0][1] < b[0][1]:
            return b
        else:
            return a


T = int(input())
for case in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append([i+1,L[i]])
    print('#{} {}'.format(case,divide_group(len(A),A)[0][0]))