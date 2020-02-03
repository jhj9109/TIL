#T받고
#T반복
#K N M 입력받음
#K : 한번 충전에 갈 수 잇는 정류장수
#N : 0~N번정류장까지
#M : M개의 정류장
#조건1 (M+1)*K < N
#0 :  다음 정류장 까지 간다. K번안에 있는 정류장 검색, 나중꺼로 간다
#1~ : 정류장에 도착하면 K 리셋, 또다시 탐색
"""
탐색 과정
1. 어느 곳에 도착한다 (초기값 0, 충전량 K)
2. 나의 인덱스 idx >>> idx+K안에 충전소가 있는지 검색한다.
    분기 1 : 없다 result = 0 break
    분기 2 : 있다 >>> temp[0:]에 저장한다, 뒤에 정류장으로 향한다.
3. 어느 곳에 도착한다 >>> 종점이 아닌 충전소면 result +1을 한다.
    종점이면  result를 반환한다.
"""
#import sys
#sys.stdin = open("sample_input.txt", "r")


T = int(input())
for T in range(T):
    K, N, M = map(int, input().strip().split())
    #print(f'{K}, {N}, {M}')
    test = list(map(int, input().strip().split()))

    #조건1
    if (M+1)*K < N:
        result = 0
        #print(f'{(M+1)*K} < {N}')
    else:
        
        idx = 0
        result = 0
        while idx != N:
            temp = []
            #print(f'진입')
            for stops in test:
                if idx < N <= idx + K: #종점행 <0>
                    temp.append(N)
                elif idx < stops <= idx+K: #충전소행 <0>
                    temp.append(stops)
                    #print(f'충전소찾음 : {temp}', end= ' ')
            #print('')
            if temp == []: #기름고갈
                result = 0
                #print(f'기름고갈')
                break
            else:
                if temp[-1] != N: #충전소행 <+1>
                    result += 1
                    #print(f'기름충전 {temp[-1]}')
                idx = temp[-1] #충전소 or 종점
        #print(f'idx = {idx}')
        print(f'#{T+1} {result}')