import sys
sys.stdin = open('input17070.txt')
input = sys.stdin.readline #백준용
#예제출력 1, 3, 0, 13
'''
50분 컷
N x N 격자, (r,c)칸, 벽X == 빈칸만 차지
파이프 모양 : 가로, 세로, 대각석
미는 방향 →, ↘, ↓ 
밀면서 회전(45도) 가능,
가로 : 가로 + 1 & 가로유지, 대각선회전
세로 : 세로 + 1 & 세로유지, 대각선회전 
대각석 : 대각선 + 1 & 대각선 유지 / 가로 + 1 & 바로 변환 / 세로 + 1 & 세로 변환
--------------------------------------------------------------------------
초기 (0,0)(0,1):가로상태 >>> (N-1,N-1)으로 이동하는 방법의 개수
--------입력-------------------------------------
N
N x N 격자 : 빈칸0>>>True 벽1>>>False
-----------파이프 좌표 구성 >>> 1 의 값만 사용-------------------
가로 : 2 1
세로
2
1
대각선
4 3
2 1
----------------------------------------------------------

'''
def go(N):
    #초기화
    pipe = ('가로', 0, 1) #파이프상태, x, y
    s = []
    s.append(pipe)
    cnt = 0
    while s:
        pipe = s.pop()
        #최종 목표지점 도달 >>> cnt += 1
        if pipe[1] == N-1 and pipe[2] == N-1:
            cnt += 1
        else:
            #다음 이동경로 탐색
            temp = check(pipe)
            if temp:
                s.extend(temp)
    return cnt
        

def check(pipe):
    ret = []
    x, y = pipe[1], pipe[2]
    if pipe[0] == '가로':
        if (y+1<=N-1) and field[x][y+1]:
            ret.append(('가로', x, y+1))
            if (x+1<=N-1 and y+1<=N-1) and field[x+1][y] and field[x+1][y+1]:
                ret.append(('대각선', x+1, y+1))
        return ret
    if pipe[0] == '세로':
        if (x+1<=N-1) and field[x+1][y]:
            ret.append(('세로', x+1, y))
            if (x+1<=N-1 and y+1<=N-1) and field[x][y+1] and field[x+1][y+1]:
                ret.append(('대각선', x+1, y+1))
        return ret
    if pipe[0] == '대각선':
        if (y+1<=N-1) and field[x][y+1]:
            ret.append(('가로', x, y+1))
        if (x+1<=N-1) and field[x+1][y]:
            ret.append(('세로', x+1, y))
        if (x+1<=N-1 and y+1<=N-1) and field[x][y+1] and field[x+1][y] and field[x+1][y+1]:
            ret.append(('대각선', x+1, y+1))
        return ret

T = 1 #제출시 1, 여러 인풋 테스트시 원하는 값으로 변경
for tc in range(1, T+1):
    N = int(input())
    field = [list(True if x == '0' else False for x in input().split()) for _ in range(N)]
    print(f'{go(N)}')