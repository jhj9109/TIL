def go(k, cnt):

    if cnt > 10:
        return
    if k == N:
        if cnt == 10:    
            for i in range(N):
                if v[i]:
                    print(i+1, end = " ")
            print()
        return
    else:
        v[k] = 1
        go(k+1, cnt+(k+1))
        v[k] = 0
        go(k+1, cnt)
 
N = 10
v = [0]*N
go(0, 0) # 3개 원소 powerset