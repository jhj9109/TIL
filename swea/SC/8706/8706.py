'''
0 / 1~N :
T
N M:수레용량
------------
각 구역에 도착한다.
당근 숫자를 더한다.
당근 숫자가 수레 용량보다 크면 M만큼 뺀다.& 이동거리 += 해당인덱스*2
몫과 나머지를 사용하면 좋겠다.
N : 나머지 != 0 이동거리 += 해당인덱스*2
'''
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    carrot = [0]
    carrot += list(map(int, input().split()))

    goods = 0
    distance = 0 #곱하기 2할 예정
    for idx in range(1, N+1):
        goods += carrot[idx]
        goods, distance = (goods % M) ,(distance + (goods // M) * idx)
    if goods != 0:
        distance += N
    print(f'#{tc} {distance*2}')