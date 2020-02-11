import sys
sys.stdin = open('input.txt')
#예제출력 d, a, a, b
def my_func(a, b):
    X = [0, 0, 2, 2]
    Y = [1, 3, 1, 3]
    x1, y1, x2, y2 = a
    for i in range(4):
        if (x1 < b[X[i]] < x2) and (y1 < b[Y[i]] < y2):
            return 'a'
    for i in range(4):
        if not(b[2] <= x1 or b[0] >= x2) and not(b[3] <= y1 or b[1] >= y2):
            return 'a'
    for i in range(4):
        if (b[X[i]]==x1 or b[X[i]]==x2) and y1 < b[Y[i]] < y2:
            return 'b'
    for i in range(4):
        if (b[X[i]]==x1 or b[X[i]]==x2) and (b[Y[i]]==y1 or b[Y[i]]==y2):
            return 'c'
    return'd'


for tc in range(1, 4+1):
    d = list(map(int, input().split()))
    a = d[0:4]
    b = d[4:8]
    print(my_func(a,b))