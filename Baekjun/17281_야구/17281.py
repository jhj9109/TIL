import sys
# input = sys.stdin.readline #백준용
sys.stdin = open('input17281.txt')
#예제출력 1, 4, 43, 46, 216, 89

'''10:51
N이닝, 3아웃, 공수교대
경기시작전 타순, 도중 변경 불가
주자 O, 1루타, 2루타, 3루타, 홈런, 아웃
----------------타순 정하기------------------------
4번 타순 :No.1 >>> 0~8번 타순 : 3번타순No.0
------------------입력-----------------------------
N : 2~50
N 줄 : 각 이닝 별 별과
안타1 2루타2 3루타3 홈런4 아웃0
------------------데이터---------------------------
lineup = [0, 1, 2, 3>>>No.1, 4, 5, 6, 7, 8] 0~8
'''

def permute(arr):
    arr.insert(3, 0)
    result = [arr[:]]
    arr.pop(3)
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            arr.insert(3, 0)
            result.append(arr[:])
            arr.pop(3)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

def go(N, lineup, score):#이미 라인업을 만든 후, N개의 이닝별 데이터로 계산하자
    #N이닝 동안 진행
    #0번 타순에 해당하는 선수 <lineup[0]>부터 시작
    now = 0
    res = 0
    ining = 0 #0이닝부터 N-1이닝까지
    j = []
    out = 0
    while ining <= N-1:
        if (N-ining)*24 + res < score: #백트래킹
            return score
        while out < 3:
            #현재 타순 <now> 은 이미 전에 결정되서 넘어온다고 치면
            if d[ining][lineup[now]] == 0:
                out += 1
            if d[ining][lineup[now]] == 4:
                res += 1 + len(j)
                j = []
            if d[ining][lineup[now]] == 3:
                res += len(j)
                j = [3]
            if d[ining][lineup[now]] == 2:
                if j:
                    for i in range(len(j)-1, -1, -1):
                        j[i] += 2
                        if j[i] >= 4:
                            j.pop(i)
                            res += 1
                j.append(2)
            if d[ining][lineup[now]] == 1:
                if j:
                    for i in range(len(j)-1, -1, -1):
                        j[i] += 1
                        if j[i] >= 4:
                            j.pop(i)
                            res += 1
                j.append(1)
            #다음 타순
            now = (now+1) % 9
        #3out
        j = []
        out = 0
        ining += 1
    score = res if res > score else score
    return score

T = 6
for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range (N)]
    lineups = permute( list(range(1,9)) )
    score = 0
    for lineup in lineups:
        score = go(N, lineup, score)
    print(score)