'''
샘플 입력 100 >>> 출력 8 100 62 38 24 14 10 4 6
'''
N = int(input())
max_cnt = 1
result = [N]

for n in range(N//2, (N//3)*2+2):
    temp = [N, n]
    while temp[-2] - temp[-1] >= 0:
        temp.append(temp[-2] - temp[-1])
    if len(temp) > max_cnt :
        max_cnt = len(temp)
        result = temp[:]
print(max_cnt)
for i in range(len(result)):
    if i != len(result)-1 :
        print(result[i], end=' ')
    else:
        print(result[i])