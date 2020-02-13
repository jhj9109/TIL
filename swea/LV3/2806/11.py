def ret_imposs(imposs_src, N, p):
    '''
    N : 체스판 크기, n : 놓은 인덱스
    -------------------------------imposs_src---------------------------
    imposs_src = [ [하나씩 감소할 인덱스], [변하지 않는 인덱스], [하나씩 증가할 인덱스]]
    '''
    for i in range(3):
        imposs_src[i].append(p)

    for i in range(len(imposs_src[0])):
         imposs_src[0][i] = -1 if imposs_src[0][i] == 0 else imposs_src[0][i] - 1
    for i in range(len(imposs_src[2])):
         imposs_src[2][i] = -1 if imposs_src[2][i] == N-1 else imposs_src[2][i] + 1

    while -1 in imposs_src[0]:
        imposs_src[0].remove(-1)
    while -1 in imposs_src[2]:
        imposs_src[2].remove(-1)
    
    return imposs_src