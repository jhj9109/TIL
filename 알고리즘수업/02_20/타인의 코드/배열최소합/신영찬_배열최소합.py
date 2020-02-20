ts=int(input())

def get_min_val(N,line,min_val,cur):
    if line>=N:
        return min(min_val,cur)
    for i in range(N):
        if line==0:
            cur=0
        if not exception[i]:
            exception[i]=True
            cur+=d[line][i]
            if not cur>min_val:
                min_val=get_min_val(N,line+1, min_val,cur)
            exception[i]=False
            cur-=d[line][i]
    return min_val


for test_case in range(1,1+ts):
    N=int(input())
    d=[list(map(int, input().split())) for _ in range(N)]
    exception=[False]*N
    print('#{} {}'.format(test_case,get_min_val(N,0,1000,0)))