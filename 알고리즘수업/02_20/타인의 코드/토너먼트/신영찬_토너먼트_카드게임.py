def rps(a, b,d):
    num1=d[a-1]
    num2=d[b-1]
    if num1==num2:
        return a
    if num1==1:
        if num2==2:
            return b
        if num2==3:
            return a
    if num1==2:
        if num2==1:
            return a
        if num2==3:
            return b
    if num1==3:
        if num2==1:
            return b
        if num2==2:
            return a

def play(i,j,d):
    if i>=j:
        return j
    a=play(i,(i+j)//2,d)
    b=play((i+j)//2+1,j,d)
    return rps(a,b,d)

ts=int(input())

for test_case in range(1,1+ts):
    people=int(input())
    d=list(map(int,input().split()))
    ret=play(1,people,d)
    print('#{} {}'.format(test_case, ret))