'''
10 8
3
0 3
1 4
0 2
>>>30
'''def my_cal(x_line, y_line, i, j):
    #print (f'({x_line[i+1]}-{x_line[i]})*({y_line[j+1]}-{y_line[j]})')
    return (x_line[i+1]-x_line[i])*(y_line[j+1]-y_line[j])

Y, X = map(int, input().split())
N = int(input())
x_line = [0, X]
y_line = [0, Y]
for _ in range(N):
    command, num = map(int, input().split())
    if command == 0:
        x_line.append(num)
    elif command == 1:
        y_line.append(num)
x_line.sort()
y_line.sort()
#print(x_line)
result = 0
for i in range(len(x_line)-1):
    for j in range(len(y_line)-1):
        temp = my_cal(x_line, y_line, i, j)
        result = temp if temp > result else result
print(result)