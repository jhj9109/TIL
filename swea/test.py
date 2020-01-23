T = int(input())

for i in range(T):
    n = int(input())
    for k in range(n):
        speed = 0
        length = 0
        command = list(map(int,input().spilit()))
        if command[0] == 0 :
            pass
        elif command[0] == 1 :
            speed += command[1]
        else:
            speed -= command[1]
            if speed < 0 :
                speed = 0

        length += speed

print('#{0} {1}'.format(i+1, length))