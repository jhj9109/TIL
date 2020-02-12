# import sys
# sys.stdin = open('input2.txt')

def to_90(data):
    N = len(data)
    ret = []
    for y in range(N):
        temp = list()
        for x in range(N):
            temp.append(data[-x+-1][y])
        ret.append(temp)
    return ret

T = int(input())
for T in range(T):
    data = list()
    for _ in range(9):
        data.append(list(map(int, input().strip().split(' '))))
    
    result = 1 #초기값
    #row 검증
    for numbers in data:
        for num in range (1,10):
            if not ( num in numbers) :
                result = 0

    for x in range(0,9,3):
        temp = list()
        for y in range(0,9,3):
            for xi in range(3):
                for yi in range(3):
                    temp.append(data[y+yi][x+xi])
            for num in range(1,10):
                if not ( num in temp):
                    result = 0
    
    data = to_90(data)
    #col 검증
    for numbers in data:
        for num in range (1,10):
            if not ( num in numbers) :
                result = 0

    print('#{} {}'.format(T+1,result))