import sys
sys.stdin = open('input.txt')
# #7 8 10 13 19 20 23
def my_sum(d):
    res = 0
    for n in d:
        res += n
    return res

d = []
for _ in range(9):
    d.append(int(input()))
res = []

s = my_sum(d)
flag = False
for i1 in range(0, 8):
    for i2 in range(i1+1, 9):
        if s - d[i1] - d[i2] == 100:
            d.pop(i2)
            d.pop(i1)
            flag = True
            break
    if flag:
        break
d = sorted(d)
for n in d:
    print(n)