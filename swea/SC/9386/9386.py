import sys
sys.stdin = open('input1.txt')

T = int(input().strip())
for tc in range(1, T+1):
    N = int(input().strip())
    data = input().strip()

    max_cnt, cnt = 0, 0
    for d in data:
        if d == '1':
            cnt += 1
        else:
            max_cnt = cnt if cnt > max_cnt else max_cnt
            cnt = 0
    max_cnt = cnt if cnt > max_cnt else max_cnt

    print(f'#{tc} {max_cnt}')
