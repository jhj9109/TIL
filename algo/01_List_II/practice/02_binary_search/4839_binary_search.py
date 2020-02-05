import sys
sys.stdin = open("input.txt")



def find(total, target):
    l = 1
    r = total
    m = int((1 + r)/2) #(1 +r)//2
    cnt = 1

    while m != target:
        if m < target:
            l = m
        else:
            r = m
        cnt +=1

    return cnt

T= int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    A = find (P, Pa)
    B = find (P, Pb)

    result = '0'

    if A < B:
        result = 'A'
    elif A > B:
        result = 'B'

    print(f'{tc} {result}')