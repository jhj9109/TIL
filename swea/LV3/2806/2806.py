from pprint import pprint
import copy
import sys
sys.stdin = open('sample_input.txt')


def chess(size, field_factor, n):
    #field == copy.deepcopy(field_factor)
    # if n == size + 1:
    #     return 1
    
    cnt = 0
    if n == 1:
        for y in range(size):
            
            field = copy.deepcopy(field_factor)
            field[n - 1] = [False] * size 
            field[n - 1][y] = 1
            k = 1
            while n - 1 + k <= size - 1:
                field[n - 1 + k][y] = False
                if  0 <= y - k:
                    field[n - 1 + k][y - k] = False
                if y + k <= size - 1:
                    field[n - 1 + k][y + k] = False
                k += 1
            # print(n-1, y)
            # for i in range(size):
            #     pprint(field[i])    
            cnt += chess(size, field, n + 1) #None > 갯수 리턴
        return cnt


    else:
        field = copy.deepcopy(field_factor)
        if field[n - 1] == [False] * size:
            return 0
        if n == size:
            # print('return:1')
            return 1
        for y in range(size):
            field = copy.deepcopy(field_factor)
            if field[n - 1][y] != False:
                field[n - 1] = [False] * size 
                field[n - 1][y] = 1
                k = 1
                while n - 1 + k <= size - 1:
                    field[n - 1 + k][y] = False
                    if  0 <= y - k:
                        field[n - 1 + k][y - k] = False
                    if y + k <= size - 1:
                        field[n - 1 + k][y + k] = False
                    k += 1
                # print(n-1, y)
                # for i in range(size):
                #     pprint(field[i])   
                cnt += chess(size, field, n + 1)
        return cnt
    

T = int(input())
for tc in range(1, T+1):
    size = int(input())
    field = [[True] * size for _ in range(size)]
    
    result = chess(size, field, 1)
    print(f'#{tc} {result}')    