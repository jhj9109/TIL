def my_position(val):
    '''
    pre_line : 숫자가 속한 전 줄 번호
    '''
    i = 0
    while val > my_sum(i):
        i += 1
    pre_line = i-1
    #print(pre_line)
    return (val - my_sum(pre_line)) , ((pre_line + 2) - (val - my_sum(pre_line)))

def my_sum(num):#num줄까지 1~my_sum(num)숫자가있다.
    return ((1 + num) * num) // 2
'''
N줄 : N개의 숫자
M줄 첫번째 숫자 (1,M) >>> (M,1)

값으로 포지션구하기 (v)
1.N+1 구하기 >>>값 (1+N)*N/2 = sums
2.포지션 : (v-sums), ((N+1)+1) - (v-sums)

포지션으로 값구하기 (x,y)
1. x + y = N + 2
2. 값 = (x+y-2)의 sums + x
''' 
def my_value(position):
    return my_sum(position[0] + position[1] - 2) + position[0]

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())
    pi, qi = my_position(p), my_position(q)
    newi = [ pi[0]+qi[0] , pi[1]+qi[1] ]
    result = my_value(newi)

    print(f'#{tc} {result}')