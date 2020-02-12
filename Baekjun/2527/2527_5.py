# import sys
# sys.stdin = open('input.txt')
#예제출력 d, a, a, b
def my_func(a, b): # x1:[0], y1:[1], x2:[2], y2:[3]
    if a[0] > b[2] or a[1] > b[3] or a[2] < b[0] or a[3] < b[1]:
        return 'd'
    
    if (a[0] == b[2] and (a[3] == b[1] or a[1] == b[3])) or (a[2] == b[0] and (a[3] == b[1] or a[1] == b[3])):
        return 'c'
 
    if a[0] == b[2] and (a[1] < b[1] < a[3] or a[1] < b[3] < a[3]) or a[2] == b[0] and (a[1] < b[1] < a[3] or a[1] < b[3] < a[3]):
        return 'b'
    if a[1] == b[3] and (a[0] < b[0] < a[2] or a[0] < b[2] < a[2]) or a[3] == b[1] and (a[0] < b[0] < a[2] or a[0] < b[2] < a[2]):
        return 'b'
    return 'a'

for tc in range(4):
    d = list(map(int, input().split()))
    a = d[0:4]
    b = d[4:8]
    print(my_func(a,b))