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

T = 6
for tc in range(1, T+1):
    N = int(sys.stdin.readline().strip())
    d = [list(map(int, sys.stdin.readline().strip().split())) for _ in range (N)]
    GG = getGG(d)
    print(GG)
