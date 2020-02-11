def move(w, h, p, q, t):
    dx, dy = 1, 1
    n = 0
    i = 0
    x, y = p, q
    while n != t:
        if not(0<= x+dx <=w) and not(0<= y+dy <= h):
            dx *= -1
            dy *= -1
        elif not(0<= x+dx <=w):
            dx *= -1
        elif not(0<= y+dy <= h):
            dy *= -1
        n, x, y = n+1, x+dx, y+dy
    return x, y

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
print(move(w, h, p, q, t))