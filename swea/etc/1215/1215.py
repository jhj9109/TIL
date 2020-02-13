import sys
sys.stdin = open('input.txt')
def to_90(data):
    res = [[0]*len(data) for _ in range(len(data))]
    for y in range(len(data)):
        for x in range(len(data)):
            res[y][x] = d[-x-1][y]
    return res

for tc in range(1, 10+1):
    N = int(input())
    d = [input() for _ in range(8)]

    cnt = 0
    for x in range(8):
        for y in range(8-(N-1)):
            n = 0
            while n != N//2:
                if d[x][y +n] == d[x][y + N-1 -n]:
                    n += 1
                else:
                    break
            else:
                cnt += 1
    d = to_90(d)
    for x in range(8):
        for y in range(8-(N-1)):
            n = 0
            while n != N//2:
                if d[x][y +n] == d[x][y+N-1 -n]:
                    n += 1
                else:
                    break
            else:
                cnt += 1
    print(f'#{tc} {cnt}')