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

def add_sort(lst, num, K):
    if num not in lst:
        i = 0
        for idx in range(len(lst)):
            i += 1 if num < lst[idx] else 0 # 내림차순 정렬 인덱스
            if i > K-1: # 0~K-1까지만 보관
                break
        else:
            lst.insert(i, num)
            if len(lst) > K:
                lst.pop()

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    d = input() #N개 16진수
    d += d[:(N//4)]
    num_set = list()
    for i in range(N):#0,1,2
        temp = 0
        for j in range(N//4):
            temp += t(d[i+j])*(16**(N//4 -1 - j))
        add_sort(num_set, temp, K)
    print(f'#{tc} {num_set[K-1]}')
#[3957, 3611, 2945, 2875, 2079, 1886, 1505, 952, 947, 503, 435]
#1 503