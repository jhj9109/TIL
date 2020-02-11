m = [0, 1, 0, 0]
for i in range(1,5):
    print(m[i%4], m[(i+2)%4], m[(i+1)%4], m[(i+3)%4])