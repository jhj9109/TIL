import sys
sys.stdin = open('input14499.txt')

def set_dice(c, val):
    # 동1 서2 북3 남4
    if c == 1:
        # 서,              밑,       동,      반대편        서         밑        동,       반대편
        dice[0][1], dice[0][0],  dice[0][2], dice[2] = dice[0][0], dice[0][2], dice[2], dice[0][1]
    if c == 2:
        # 서                밑,      동,      반대편        서,         밑,        동,      반대편
        dice[0][1], dice[0][0],  dice[0][2], dice[2] = dice[2], dice[0][1],  dice[0][0], dice[0][2]
    if c == 3:
        # 밑,           남,    반대편,     북         밑,     남,    반대편,     북
        dice[0][0], dice[1], dice[2], dice[3] = dice[3], dice[0][0], dice[1], dice[2]
    if c == 4:
        # 밑,          남,    반대편,     북         밑,     남,    반대편,     북
        dice[0][0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0][0]
    # 윗면 출력
    print(dice[2])
    if val:
        # 칸의 수가 바닥면으로 복사, 칸의 숫자는 0
        dice[0][0] = val
        return 0
    else:
        # 바닥면의 숫자가 칸의 숫자로 복사
        return dice[0][0]

def sim(r, c):
    dr = [0, 0, 0,-1, 1]
    dc = [0, 1,-1, 0, 0]
    for commend in commends:
        if 0 <= r+dr[commend] < N and 0 <= c+dc[commend] < M:
            r, c = r+dr[commend], c+dc[commend]
            field[r][c] = set_dice(commend, field[r][c])

# T = 1 # 제출용
T = 4 # 테스트용
for tc in range(1, T+1):
    N, M, x, y, K = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(N)]
    dice = [[0, 0, 0], 0, 0, 0]
    # 동1, 서2, 북3, 남4
    commends = list(map(int, input().split()))
    sim(x, y)