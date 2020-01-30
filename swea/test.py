'''
100x100을 받는다
0을 기준으로 같은 값의 위치 0+ix를 찾는다.
for i in range
if data[0][i] == data[0][i+j]
0+1 / x-1 위치를 비교한다. ->

'''
#N = int(input())
#data = input()
data = 'CCBBCBAABCCCBABCBCAAAACABBACCCCACAABCBBACACAACABCBCCBAABCABBBCCAABBCBBCACABCAAACACABACBCCBAACBCBCAAC'
N = 100
cnt = 1
temp = 0
for x in range(N-1):#0~98
    for i in range(cnt,N-1-x):#1~99
        j = 0
        while data[0][x+j] == data[0][x+i-j]:
            if i-2j == 1 or i-2j == 2:
                cnt = i+1
                temp = 1
                print(x,j)
            j += 1

        if temp != 0:
            print('break1')
            break
    if temp != 0:
        print('break2')
        break
print(cnt)