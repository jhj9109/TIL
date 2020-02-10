import sys
sys.stdin = open('input.txt')

def my_search(data, val):
    for x in range(len(field[0])):
        for y in range(len(field)):
            if data[x][y] == val:
                return x,y
def my_check(data, x, y):
    #우/좌/상/하/우상/우하
    dx = [0,  0, -1, 1, -1, 1]
    dy = [1, -1,  0, 0,  1, 1]
    i = 0
    while i != 5 and (data[x+dx[0]*i][dy[0]*i] or not(data[x+dx[0]*i][dy[0]*i]):
        i += 1
    if i == 5:
        return True
    i = 0
    while i != 5 and (data[dx[3]*i][y+dy[3]*i] or not(data[dx[3]*i][y+dy[3]*i])):
        i += 1
    if i == 5:
        return True
    if x,y == 2,2:
        i = 0
        while i != 5 and (data[4 + dx[4]*i][dy[4]*i] or not(data[4 + dx[4]*i][dy[4]*i])):
            i += 1
        if i == 5:
            return True

field = [list(map(int, input().split())) for _ in range(5)]
bingo = []
for _ in range(5):
    bingo.extend(list(map(int, input().split())))
for i in range(25):
    my_search(field, bingo[i])