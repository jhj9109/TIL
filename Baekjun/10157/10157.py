def assign(C, R, K):
    x1, x2, y1, y2 = 1, R, 1, C
    dx = [ 0, 1, 0,-1]
    dy = [ 1, 0,-1, 0]
    x, y = 1, 1
    n, i = 1, 0
    while n != K:
        n += 1
        if not(x1 <= x+dx[i%4] <= x2) or not (y1 <= y+dy[i%4] <= y2):
            i += 1
            x1, x2, y1, y2 = ranges(i, x1, x2, y1, y2)
        x, y = x+dx[i%4], y+dy[i%4]
    return x, y
def ranges(i, x1, x2, y1, y2):
    m = [0, 1, 0, 0]
    return x1+m[i%4], x2-m[(i+2)%4], y1+m[(i+1)%4], y2-m[(i+3)%4]

    
R, C = map(int, input().split())
K = int(input())
# R, C= 7, 6
# X , Y = assign(C, R, 42)
print(X, Y)