def minimum(i, num, s):
    if len(result) > 0 and min(result) < s:
        return
    if i == num-1:
        for j in range(num):
            if visited[j] == 0:
                visited[j] = 1
                s += matrix[i][j]
                result.append(s)
                s -= matrix[i][j]
                visited[j]=0

    else:
        for j in range(num):
            if visited[j] == 0:
                visited[j] = 1
                s += matrix[i][j]
                minimum(i+1, num, s)
                s -= matrix[i][j]
                visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(num)]
    result = []
    visited = [0] * num
    s = 0
    for i in range(num):
        minimum(0, num, s)
    print(f'#{tc} {min(result)}')