def cal_move(w, h, p, q, t):
    x, y = p, q
    tx, ty = t % (2*w), t % (2*h)
    if x + tx <= w:
        x = x + tx
    elif x + tx <= 2*w:
        #x = w - (x + tx - w)
        x = 2*w - (x + tx)
    else:
        x = x + tx - 2*w
    if y + ty <= h:
        y = y + ty
    elif y + ty <= 2*h:
        #y = h - (y + ty - h)
        y = 2*h - (y + ty)
    else:
        y = y + ty - 2*h
    return x, y


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
print(cal_move(w, h, p, q, t))