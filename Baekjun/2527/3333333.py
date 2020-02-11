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
        if (b[2] > x1 and b[0] < x2) and (b[3] > y1 and b[1] < y2):
            return 'a'
    if ((b[3] == y1 or b[1] == y2) and (x1 < b[0] < x2 or  x1 < b[2] < x2)) or ((b[0] == x2 or b[2] == x1) and (y1 < b[1] < y2 or y1 < b[3] < y2)):
            return 'b'
    if (b[0] == x2 and (b[3] == y1 or b[1] == y2)) or (b[2] == x1 and (b[3] == y1 or b[1] == y2)):
            return 'c'
    return'd'


for tc in range(1, 4+1):
    d = list(map(int, input().split()))
    a = d[0:4]
    b = d[4:8]
    print(my_func(a,b))