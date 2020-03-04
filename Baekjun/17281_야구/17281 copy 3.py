import sys
sys.stdin = open('input17281.txt')
#예제출력 1, 4, 43, 46, 216, 89

def getGG(d):
    cnt = 0
    ret = []
    for rows in d:
        temp = 0
        temp_res = 0
        for _ in range(3):
            for r in rows:
                if r:
                    temp += 1
                else:
                    temp_res = temp if temp > temp_res else temp_res
        cnt += temp_res 
        ret.append(cnt)
    ret = ret[::-1]
    return ret

def permute(N, arr):
    arr.insert(3, 0)
    score = 0
    score = go(N, arr, score)
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
            score = go(N, arr, score)
            if score == GG[0]:
                return score
            arr.pop(3)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return score

def go(N, lineup, score):#이미 라인업을 만든 후, N개의 이닝별 데이터로 계산하자
    #N이닝 동안 진행
    #0번 타순에 해당하는 선수 <lineup[0]>부터 시작
    now = 0
    res = 0
    ining = 0 #0이닝부터 N-1이닝까지
    j = []
    #1,2,3 = 1, 2, 3 / 1,2 > 4 , 2,3 > 5 , 1,3 > 6, 1,2,3 > 7
    out = 0
    while ining < N:
        if GG[ining] + res < score: #백트래킹
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
    N = int(sys.stdin.readline().strip())
    d = [list(map(int, sys.stdin.readline().strip().split())) for _ in range (N)]
    GG = getGG(d)
    print( permute(N, list(range(1,9)) ) )