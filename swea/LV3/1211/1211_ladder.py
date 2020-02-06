def my_sero_check(data): #길이3 리스트 인풋
    X, Y, Z = data[0], data[1], data[2]
    #우 / 좌 / 아래 / 종료

    if 0 <= Y+1 <= 99:
        if field[X][Y+1] == 1:
            return X, Y+1, 2
        
    if 0 <= Y-1 <= 99:
        if field[X][Y-1] == 1:
            return X, Y-1, 1
        
    if field[X+1][Y] == 1:
        return X+1, Y, 0
    else:
        return X, Y, False
    
def my_garo_check(data):
    X, Y, Z = data[0], data[1], data[2]
    #아래 / 좌 / 우 / 종료
    if field[X+1][Y] == 1:
        return X+1, Y, 0

    if 0 <= Y-1 <= 99 and data[2] == 1:
        if field[X][Y-1] == 1:
            return X, Y-1, 1
        
    if 0 <= Y+1 <= 99 and data[2] == 2:
        if field[X][Y+1] == 1:
            return X, Y+1, 2
    else:
        return X, Y, False

import sys
sys.stdin = open('input.txt')


T = 1
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 10001
    min_idx = 100
    for idx in range(100):
        position = [0, 0, 0]
        if field[0][idx] == 1:
            #초기값
            
            position = [1, idx, 0]
            cnt = 2
            #print(f'{idx}:{cnt}')
            while position[0] != 99:
                # 아래 /좌우
                # 벗어나다 = False = 갈곳없음 >>> 종료
                if position[2] == 0:
                    position = my_sero_check(position)
                elif position[2] == 1 or position[2] == 2:
                    position = my_garo_check(position)
                else:#position[2] == False
                    print(f'{idx} : Fail')
                    break
                cnt += 1
            else:#맨 아래까지 도달
                if cnt < min_cnt:
                    min_cnt = cnt
                    min_idx = idx
    print(f'#{tc} {min_idx} {min_cnt}')
