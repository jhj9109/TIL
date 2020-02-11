import sys
sys.stdin = open('input.txt')
from pprint import pprint 

def my_search(data, val, answer):
    for x in range(len(data[0])):
        for y in range(len(data)):
            if data[x][y] == val:
                answer[x][y] = True
                return x, y, answer

def my_check(d, x, y):
    dx = [0, 1, -1, 1]
    dy = [1, 0,  1, 1]
    x0 = [x, 0, 4, 0]
    y0 = [0, y, 0, 0]
    ret = 0
    for i in range(2):
        k = 0
        while k != 5 and d[x0[i]+dx[i]*k][y0[i]+dy[i]*k]:
            k += 1
        ret += 1 if k == 5 else 0
    if x + y == 4:
        k = 0
        while k != 5 and d[x0[2]+dx[2]*k][y0[2]+dy[2]*k]:
            k += 1
        ret += 1 if k == 5 else 0
    if x == y :
        k = 0
        while k != 5 and d[x0[3]+dx[3]*k][y0[3]+dy[3]*k]:
            k += 1
        ret += 1 if k == 5 else 0
    return ret

field = [list(map(int, input().split())) for _ in range(5)]
bingo = []
for _ in range(5):
    bingo.extend(list(map(int, input().split())))

answer = [[False]*5 for _ in range(5)]
answer_cnt = 0
for i in range(25):
    x, y, answer = my_search(field, bingo[i], answer)
    answer_cnt += my_check(answer, x, y)
    if answer_cnt >= 3:
        print(i+1)
        break