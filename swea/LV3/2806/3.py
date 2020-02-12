from pprint import pprint
import copy
import sys
sys.stdin = open('sample_input.txt')
'''
함수
'''
def chess(imposs_index, i, , N, n):
    '''
    -------------------------------입력----------------------------------
    imposs_index : 이전에 놓은 체스 말로 인해 놓을수 없는 인덱스, 누적된다
    i : 각 행의 0~N-1 각 칸에 둘 수 있는지 for문을 밖에서 돌려 인풋으로 넣는다
    n : 놓은 체스말 수, 가능하게 되면 n+1로 chess함수 호출
    N : 목표 체스말 수 
    -------------------------------출력-----------------------------------
    i번째에 놓을수 있으면 chess함수를 또 호출한다 >>> for문으로
    i번쨰에 놓을수 있고, 체스가 마무리 되면 1을 리턴한다
    i번째에 놓을수 없으면 0을 리턴한다
    리턴은 최종적으로 cnt
    -------------------------------imposs_index---------------------------
    imposs_index = [ [하나씩 감소할 인덱스], [변하지 않는 인덱스], [하나씩 증가할 인덱스]]
    for idx in [0,2]:
        if imposs_index[idx] != []:
            k = -1 if not(idx) else +1
            for j in range(len(imposs_index[idx])):
                imposs_index[idx][j] += k
    '''
    if n > N :
        return 1
    cnt = 0
    for p in range(N):
        for q in range(3):
            break if p in imposs_index[q] else pass
        else:
            imposs_index = ret_imposs()
            for v in range(N):
                cnt += chess(imposs_index, v, n+1)
                

    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [[True] * N]
    n = 0
    while n != N:

    result = chess(N, field, 1)
    print(f'#{tc} {result}')    