"""
암호 : 8자리숫자 (7자리 고유번호, 1검증코드)

홀수자리*3 + 짝수자리 + 검증코드 = 십의자리
------------------------------------------
가로100이하, 세로50이하
"""

'''
import sys
sys.stdin = open("input.txt")
hint = [
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1],
]
T = int(input())
for T in range(T):
    N, M = map(int, input().split())

    data = [list(map(int, list(input()))) for _ in range(N)]

    flag = True
    result = 0
    for x in range(N):
        if not(flag):
            break
        for y in range(M-1, -1, -1):
            if not(flag):
                    break
            if data[x][y] == 1:
                temp = []
                number = 0
                sums = 0
                for i in range(8):
                    #temp.append(data[x][y-55 + 7*i : y-55 + 7*(1+i)])
                    for j in range(10):
                        if temp[i] == hint[j]:
                            print(f'i:{i}, j:{j}')
                            number += j
                            if (i+1) % 2 and i != 7:
                                sums += j * 3
                            else:
                                sums += j
                print(f'number:{number}, sums:{sums}')
                flag = False
                result = number if sums % 10 == 0 else 0
    print(f'{T+1} {result}')
'''
import sys
sys.stdin = open("input1240.txt")
hint = [ '0001101', '0011001', '0010011', '0111101', '0100011',\
    '0110001', '0101111', '0111011', '0110111', '0001011'
]
T = int(input())
for T in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    #############print(data)
    flag = False
    for x in range(N):
        for y in range(M): #-1==79, : -y + M - 56
            if data[x][-y] == '1':
                ######print(x,-y)
                source =data[x][-y+M-55:-y+M+1] #-55~ 0
                ###############print(source)
                flag = True
            if flag:
                break
        if flag:
            break
    sums = 0
    numbers = 0
    #########print(source)
    for i in range(8):
        temp = hint.index(source[0+7*i:7+7*i])
        ###########print(temp)
        numbers += temp
        if (i+1) % 2:#짝수
            sums += temp * 3
            #########print(f'{sums} += {temp} * 3')
        else:
            sums += temp
            #######print(f'{sums} += {temp}')
    #########print(numbers, sums)
    if (sums % 10) == 0:
        print(f'#{T+1} {numbers}')
    else:
        print(f'#{T+1} 0')