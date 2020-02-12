import sys
sys.stdin = open('input.txt')
#예제출력 d, a, a, b
def my_func(a, b):
    X = [0, 0, 2, 2]
    Y = [1, 3, 1, 3]
    A_x1, A_y1, A_x2, A_y2 = a
    B_x1, B_y1, B_x2, B_y2 = b
    if A_x1 > B_x2 or A_y1 > B_y2:
        return 'd'
    A_x1, A_y1, A_x2, A_y2 = b
    B_x1, B_y1, B_x2, B_y2 = a
    if A_x1 > B_x2 or A_y1 > B_y2:
        return 'd'
    
    if A_x1 == B_x2 and (A_y2 == B_y1 or A_y1 == B_y2):
        return 'c'
    A_x1, A_y1, A_x2, A_y2 = a
    B_x1, B_y1, B_x2, B_y2 = b
    if A_x1 == B_x2 and (A_y2 == B_y1 or A_y1 == B_y2):
        return 'c'

    if A_x1 == B_x2 and (A_y1 < B_y1 < A_y2 or A_y1 < B_y2 < A_y2):
        return 'b'
    A_x1, A_y1, A_x2, A_y2 = b
    B_x1, B_y1, B_x2, B_y2 = a
    if A_x1 == B_x2 and (A_y1 < B_y1 < A_y2 or A_y1 < B_y2 < A_y2):
        return 'b'
    return 'a'

for tc in range(1, 4+1):
    d = list(map(int, input().split()))
    a = d[0:4]
    b = d[4:8]
    print(my_func(a,b))