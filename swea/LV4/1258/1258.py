import sys
sys.stdin = open('input.txt')

'''
NxN
x1~x2, y1~y2
-------------
T
N
NxN 데이터
출력 찾은 갯수 , 크기or X 작은 순서 (X,Y) 
'''
from operator import itemgetter, attrgetter
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
    result = sorted(result, key = itemgetter(2, 0))
    print (f'#{tc} {len(result)}',end=' ')
    for d in result:
        print(f'{d[0]} {d[1]}', end=' ')
    print('')