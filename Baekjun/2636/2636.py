import sys
sys.stdin = open("input2636.txt")

def act():
    '''
    #1. 노출된 치즈 2 >>> 0 res[1] 카운팅, 치즈 남은 여부 : act
    '''
    cnt = 0
    for i in range(H):
        for j in range(W):
            if f[i][j] == 2:
                f[i][j] = 0
                cnt += 1
    for i in range(H):
        if sum(f[i]) != 0:
            return -1
    else:
        return cnt

def go(): # 메인
    res[0] += 1
    '''
    #1. 0,0부터 공기층 순회
    #2. 노출된 치즈 1 >>> 2
    '''
    
    v = [[False]*W for _ in range(H)]
    s =[ (0, 0) ]
    v[0][0] = True
    while s:
        i, j = s.pop()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<=H-1 and 0<=nj<=W-1:
                if not v[ni][nj] and f[ni][nj] == 0:
                    s.append((ni,nj))
                    v[ni][nj] = True
                elif f[ni][nj] == 1:
                    f[ni][nj] = 2
    temp = act()
    if temp != -1:
        res[1] = temp
        return 
    go()

H, W = map(int, input().split())
f = [list(map(int,input().split())) for _ in range(H)]
res = [0, 0]
go()
print(res[0])
print(res[1])

'''십억에 1초
메인 프로세스
0. 초기화 : 바깥공기 순회하며 노출된 치즈 좌표 s 푸쉬
---------------------------go-------------------------
1. s 꺼내며 1>>>0, 주변탐색 : (1 and not in s)>>>ns 푸쉬, 

'''

'''필기
1. 바깥 공기층 순회하며 표시 >>> 치즈속 구멍과 구별위함
2. 표시가 된 (0 > -1 으로 바뀐 공기) 공기층을 순회하면서 인접한 치즈를 녹임 (공기층으로 만들기)
3. 치즈는 녹인 후, 치즈구멍 > 공기가 되는 과정을 처리(단, 방금 공기가 된 구멍과 맞닿는 치즈는 녹으면 안됨을 주의)
3a. 마지막으로 남아 있는 치즈 칸의 개수


'''
'''간단버전
1. 바깥 공기층 순회하며 노출된 치즈 1>>>2 표시 : go
2. n번재 res[0]과 노출된 치즈 2 >>> 0 res[1] 카운팅, 치즈 남은 여부 : act
'''