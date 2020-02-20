import sys

sys.stdin = open('sample_input.txt')

def permutation(num_list,row,N):
    global answer, temp, visited
    if row == N:
        if answer > temp:
            answer = temp
    if temp > answer:
        return None
    for i in range(N):
        if visited[i] == 0:
            temp += num_list[row][i]
            visited[i] = 1
            permutation(num_list, row+1, N)
            temp -= num_list[row][i]
            visited[i] = 0
                
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    answer, temp = 100, 0
    permutation(num_list, 0, N)
    print('#{0}'.format(tc), answer)