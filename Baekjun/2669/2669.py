def range_paint(data, ranges):
    x1, y1, x2, y2 = ranges[0], ranges[1], ranges[2], ranges[3],
    for x in range(x1, x2):#1,2,3,4
        for y in range(y1, y2):
            data[x][y] = 1
    return data

def range_sum(data):
    result = 0
    for x in range(100):
        for y in range(100):
            if data[x][y] == 1:
                result += 1
    return result


field = [[0]*100 for _ in range(100)]
ranges = [list(map(int, input().split())) for _ in range(4)]
for n in range(4):
    field = range_paint(field, ranges[n])

print(range_sum(field))