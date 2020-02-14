# from pprint import pprint
# import sys
# sys.stdin = open('sample_input.txt')
'''
함수
'''
def chess(imposs_index, N, no):
    '''
    -------------------------------입력----------------------------------
    imposs_index : 이전에 놓은 체스 말로 인해 놓을수 없는 인덱스, 누적된다
    no : 놓은 체스말 수, 가능하게 되면 n+1로 chess함수 호출
    N : 목표 체스말 수 
    -------------------------------출력-----------------------------------
    놓을 수 있는 가능성이 있으면 chess함수를 또 호출한다 >>> for문으로
    체스가 마무리 된거면 (no == N) 1을 리턴한다
    어디에도 놓을수 없으면 0을 리턴한다
    리턴은 최종적으로 cnt
    '''
    if no == N :
        cnt += 1
        return
    #cnt = 0
    for p in range(N):
        for q in range(3):
            if p in imposs_index[q]:
                break
        else:
            new_imposs_index = ret_imposs(imposs_index, N, p)
            chess(new_imposs_index, N, no+1)

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

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    init_imposs_index = [ [], [], [] ]
    no = 0
    result = chess(init_imposs_index, N, no)
    print(f'#{tc} {result}')