import sys
sys.stdin = open('input.txt')
#예제출력 d, a, a, b
def my_func(a, b): # x1:[0], y1:[1], x2:[2], y2:[3]
    '''
    모든 조건은 수행 후 a,b 스왑하여 진행

    d : 겹치지 않음 >>>A_big_x < B_small_x  or  A_big_y < B_small_y

    c : 점 >>> A_big_x == B_small_x  and ( A_big_y == B_small_y or A_small_y == B_big_y )

    b : 선분 >>>  A_big_x == B_small_x and ( B_small_y < A_big_y <B_big_y or B_small_y < A_small_y <B_big_y )
                  A_big_y == B_small_y and ( B_small_x < A_big_x <B_big_x or B_small_x < A_small_x <B_big_x )
                  

    a :
    '''
    if a[0] > b[2] or a[1] > b[3]:
        return 'd'
    a, b = b, a
    if a[0] > b[2] or a[1] > b[3]:
        return 'd'
    
    if a[0] == b[2] and (a[3] == b[1] or a[1] == b[3]):
        return 'c'
    a, b = b, a
    if a[0] == b[2] and (a[3] == b[1] or a[1] == b[3]):
        return 'c'

    if a[0] == b[2] and (a[1] < b[1] < a[3] or a[1] < b[3] < a[3]):
        return 'b'
    if a[1] == b[3] and (a[0] < b[0] < a[2] or a[0] < b[2] < a[2]):
        return 'b'
    a, b = b, a
    if a[0] == b[2] and (a[1] < b[1] < a[3] or a[1] < b[3] < a[3]):
        return 'b'
    if a[1] == b[3] and (a[0] < b[0] < a[2] or a[0] < b[2] < a[2]):
        return 'b'
    return 'a'

for tc in range(1, 4+1):
    d = list(map(int, input().split()))
    a = d[0:4]
    b = d[4:8]
    print(my_func(a,b))