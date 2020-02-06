import sys
sys.stdin = open('sample_input.txt')

'''
T
N 건초더미 갯수
N개 건초더미 크기
--------데이터---------
모두 같았다 = 평균값
평균을 구한다. 평균에서 각자 뺀다.
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    data = []
    data_sum = 0
    for _ in range(N):
        temp = int(input())
        data.append(temp)
        data_sum += temp
    ave = data_sum // N

    res = 0
    for d in data:
        res += abs(d - ave)
    print(f'#{tc} {res//2}')