import sys
sys.stdin = open('input5658.txt')
'''
10:05~10:44
N, K
한줄에 2~7 >>> 8~28숫자
--------------
'''
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    n = input() #N개 16진수
    wl = N//4
    n += n[:(wl)]
    res = set()
    for i in range(N):
        res.add(int(n[i:i+wl], 16))
    print('#%d' % tc, sorted(list(res))[-1*K])
    
    # for i in range(N):
    #     temp = 0
    #     for j in range(N//4): #N//4개의 16진수가 하나의 숫자가 된다.
    #         temp *= 16
    #         temp += int(d[i+j],16)
    #     num_set.add(temp)
    # num_lst = sorted(list(num_set), reverse = True)
    # print(f'#{tc} {num_lst[K-1]}')