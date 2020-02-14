import sys
sys.stdin = open('input.txt')

def my_remove(data, result):
    for i in range(1, V+1):
        if i not in result and data[i] == []:
            result.append(i)
            for j in range(1, V+1):
                if(data[j].count(i)):
                    data[j].remove(i)
    return data, result
    
T = 10
for tc in range(1, T+1):    
    V, E = map(int, input().strip().split())
    line = list(map(int, input().strip().split()))

    data = [[] for _ in range(V+1)]

    for i in range(E):
        data[line[i*2+1]].append(line[i*2])

    result = []
    while len(result) != V:
        data, result = my_remove(data, result)
        #print(f'{len(result)}, {result}, {data}')


    print (f'#{tc} ',end='')
    for val in result:
        print(val, end=' ')
    print('')   