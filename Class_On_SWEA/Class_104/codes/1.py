for i in range(1, 101):
    if i % 2 == 1:
        if i != 99:
            print(i, end=',')
        else:
            print(i, end="")
    else :
        print(" ")