import sys
sys.stdin = open("input.txt")
'''
원본리스트 1~10
빈리스트

빈리스트 = 1,2
뒤에올 아이 탐색

빈리스트 = 여기 1,2,7,8...

결과 = 1,2,7,8,9,10,3,4,5,6

'''
T = int(input())
for T in range(T):
    N = int(input())
    data = list(map(int, input().strip().split()))
    
    res = []
    res = [data.pop(0), data.pop(0)]

    while data:
        for i in range(0, len(data), 2):
            if res[-1] == data[i]:
                res.append(data.pop(i))
                res.append(data.pop(i))
                break
        for i in range(0, len(data), 2):
            if res[0] == data[i+1]:
                temp = []
                temp.append(data.pop(i))
                temp.append(data.pop(i))
                res = temp + res
                break
    print(f'#{T+1} ',end='')
    for ch in res:
        print(f'{ch}',end=' ')
    print()