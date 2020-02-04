'''
수나사x암나사 + 수나사x암나사
순서 찾기
------------------------
입력
T 테이스케이스
N 갯수
2N 갯수*숫나사+암나사
-------------------------
데이터...
1. 걍 인덱스단위로 해보는거 어때?
2. 사용한거는 temp에 인덱스 보관했다가 비교하지 뭐
data = list(map(int, input().strip().split()))
for i in range(0,len(data),2): # 0, 2, 4... 짝수 숫나사/ 홀수 암나사

data[짝] data[홀]
data[짝]중 맞는것 찾기
temp = [i]
while flag:
    for i in range(0,len(data),2):
if data[temp[-1]+1] == data[j] and temp[-1]+1 != j:
    temp.append(j)

'''
"""
import sys
sys.stdin = open("input.txt")

def metal(N, data, my_list):
    """
    원본+호출리턴받은거 모두 비교해서 가장 긴 리스트 1개만 리턴
    """
    #print(f'{my_list}metal호출')
    #print()
    if len(my_list) == 2*N:
        #print(f'True와 {my_list} 리턴')
        return True, my_list

    
    for n in range(0, 2*N, 2):
        if data[my_list[-1]] == data[n] and (n not in my_list):
            # 3 4 2 3 4 5 ### idx : 2 3 0 1 4 5
            #print(f'my_list는 {my_list}, n의 값 : {n}')
            #print(f'my_list[-1]는 {my_list[-1]}, data[n]의 값 : {data[n]}')
            metal_return = metal(N, data, my_list + [n,n+1])
            if metal_return[0] == True:
                return metal_return[0], metal_return[1]
            
            
    return False, None

T = int(input())
for T in range(T):
    N = int(input())
    data = list(map(int, input().strip().split()))

    result = []

    for i in range(0, 2*N, 2):
        val_return = metal(N, data, [i, i+1])

        #print(f'for문 {i+1}번째 리턴 : {val_return}')
        if val_return[0]:
            result = val_return[1]
            break

    # print(f'#{T+1}', end=' ')
    # for j in range(max_cnt):
    #     print(max_res[j], end=' ')
    print(f'#{T+1} ', end='')
    for idx in val_return[1]:
        print(data[idx], end=' ')
    print()
"""

import sys
sys.stdin = open("input.txt")

def metal(N, data, my_list):
    if len(my_list) == 2*N:
        return True, my_list

    for n in range(0, 2*N, 2):
        if data[my_list[-1]] == data[n] and (n not in my_list):
            metal_return = metal(N, data, my_list + [n,n+1])
            if metal_return[0] == True:
                return metal_return[0], metal_return[1]
    return False, None


T = int(input())
for T in range(T):
    N = int(input())
    data = list(map(int, input().strip().split()))
    
    for i in range(0, 2*N, 2):
        val_return = metal(N, data, [i, i+1])
        if val_return[0]:
            result = val_return[1]
            break

    #결과 출력부
    print(f'#{T+1} ', end='')
    for idx in val_return[1]:
        print(data[idx], end=' ')
    print()