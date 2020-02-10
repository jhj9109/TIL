import sys
sys.stdin = open('input.txt')

def my_sero_check(data): #길이3 리스트 인풋
    X, Y, Z, count = data[0], data[1], data[2], data[3]
    #우 / 좌 / 아래 / 종료
    if X+1 == 99:
        if field[X+1][Y] == 2:
            return X+1, Y, 0 , True

    if 0 <= Y+1 <= 99:
        if field[X][Y+1] == 1:
            return X, Y+1, 2 , False
    if 0 <= Y-1 <= 99:
        if field[X][Y-1] == 1:
            return X, Y-1, 1, False

    return X+1, Y, 0, count
        
def my_garo_check(data):
    X, Y, Z, count = data[0], data[1], data[2], data[3]
    #아래 / 좌 / 우 / 종료
    if field[X+1][Y] == 2:
        return X+1, Y, 0, True
    if field[X+1][Y] == 1:
        return X+1, Y, 0, False
    if data[2] == 1:
        return X, Y-1, 1, False
    if data[2] == 2:
        return X, Y+1, 2, False

T = 10
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 10001
    min_idx = 100
    for idx in range(100):
        position = [0, 0, 0, 0] #값 x, y, 0아래/1좌/2우, True/False
        if field[0][idx] == 1:
            #초기값
            
            position[0] = 1
            position[1] = idx
            while position[0] != 99:
                if position[2] == 0:
                    position = my_sero_check(position)
                elif position[2] == 1 or position[2] == 2:
                    position = my_garo_check(position)
                else:
                    break

            else:
                if position[3]:
                    print(f'#{tc} {idx}')