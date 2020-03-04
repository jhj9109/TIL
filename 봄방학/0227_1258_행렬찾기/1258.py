from operator import itemgetter, attrgetter
import sys
sys.stdin = open('input1258.txt')
#예제출력
#1 2 2 1 1 4 
#2 4 1 2 5 1 2 4 4 3
#3 6 1 2 2 3 8 1 3 7 5 8 9 5
#4 10 1 8 2 5 11 1 12 2 5 6 8 4 6 9 4 15 9 10 10 11
#5 8 1 6 10 2 2 15 6 11 7 14 11 10 17 7 15 17
#6 10 1 10 16 1 7 4 4 18 11 7 6 16 18 6 12 11 15 12 13 15
#7 13 1 13 6 3 19 1 3 12 8 6 12 4 4 14 7 11 15 8 14 10 11 15 10 19 13 20
#8 15 2 1 3 4 1 22 4 13 8 9 25 3 12 8 9 11 10 17 15 12 13 15 11 18 22 10 18 23 17 25
#9 18 8 2 3 7 4 10 15 3 9 6 14 4 11 8 7 16 6 21 16 9 10 17 21 14 27 11 17 18 18 20 26 15 20 23 23 27
#10 20 2 1 13 2 5 6 4 13 14 5 6 15 25 4 9 16 12 14 21 8 16 11 22 9 20 10 10 21 8 29 11 25 15 22 30 12 29 28 28 30

def my_search(data, x, y, n):
    '''
    0이 아닌 첫 탐색지점 (x,y)를 기준으로 x,y축 인덱스를 탐지후 리턴
    '''
    dx = [1, 0]
    dy = [0, 1]
    #ret_index = [x, y]
    size = []
    for i in range(2):
        k = 1
        while ((x+dx[i] <= n-1) and (y+dy[i] <= n-1)) and field[x + dx[i]*k][y + dy[i]*k] != 0:
            k += 1
        #ret_index.append(ret_index[i] + k - 1)
        size.append(k)
    size.append(size[0]*size[1])
#    return ret_index
    return size


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range (n)]
    
    result = []
    for x in range(n):
        for y in range(n):
            if field[x][y] != 0 and (x == 0 or field[x-1][y] == 0) and (y == 0 or field[x][y-1] == 0):
                result.append(my_search(field, x, y, n))

    #pprint(result)
    result = sorted(result, key = itemgetter(2, 0))
    #pprint(result)
    print (f'#{tc} {len(result)}',end=' ')
    for d in result:
        print(f'{d[0]} {d[1]}', end=' ')
    print('')