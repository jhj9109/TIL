import sys
sys.stdin = open('input5658.txt')
'''
10:05~10:44
N, K
한줄에 2~7 >>> 8~28숫자
--------------
0~9 : -48
A~F : -55
'''
def t(str):
    if '0' <= str <= '9':
        return ord(str) - 48
    if 'A' <= str <= 'F':
        return ord(str) - 55

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    d = input() #N개 16진수
    d += d[:(N//4)]
    num_set = set()
    for i in range(N):#0,1,2
        temp = 0
        for j in range(N//4):
            temp += t(d[i+j])*(16**(N//4 -1 - j))
        num_set.add(temp)
    num_lst = sorted(list(num_set), reverse = True)
    print(f'#{tc} {num_lst[K-1]}')
