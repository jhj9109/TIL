"""
NxN칸, M개의 나무, K년후
N줄 영양 A
M줄  위치 x,y 나이 z
------------------------
초기 영양값 5
봄 : 식사량 = 나이, 나이 += 1
여름 : 죽은 나무 // 2 = 양분
가을 : if 나이%5==0 : 8개의칸에 1살 나무
겨울 : 양분추가
------------------------
영양값[0],[1~나무들]

1. N M K 
2. N반복 : A 
3. M반복 : x,y,z
-------------------------
초기데이터셋
1. NxN 토지
2. 토지[x][y] == 영양분
3. 나무[x][y].append() : 나무
data [ [[],[],[]], [[],[],[]], [[],[],[]], ]
수정 [x][y][z] = 수정값
추가 [x][y].append(추가값)
--------------------------
봄
if 나무[x][y] != [] :
    if sum(나무[x][y]) >= 토지[x][y]:
        토지[x][y] -= sum
        나무[x][y] = [n+1 for n in 나무[x][y]]
    else :
        나무[x][y].sort
        temp = 0
        for i in 길이(나무[x][y]):
            if 토지[x][y] >= 나무[x][y][i]:
                토지[x][y] -= 나무[x][y][i]
                나무[x][y][i] += 1
            else :
                temp += 나무[x][y][i]//2
                나무[x][y].remove(i)
        토지[x][y] += temp
가을
if 나무[x][y] != [] :
    for d in 나무[x][y]:
        if d % 5 == 0:
            for i in range(8):
                pass
겨울
양분추가

                

-----------------------------

"""
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
first_tree = [list(map(int, input().split())) for _ in range(M)]
