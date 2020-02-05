T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))

    pipes = [[d[i], d[i+1]] for i in range(0, N*2, 2) ]
    
    connected = pipes.pop()
    while pipes:
        for i in range(len(pipes)):
            if pipes[i][0] == connected[-1]:
                connected += pipes.pop(i)
                break
            if pipes[i][-1] == connected[0]:
                connected = pipes.pop(i) + connected
                break

    print(connected)