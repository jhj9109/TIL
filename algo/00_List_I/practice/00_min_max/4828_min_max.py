import sys
sys.stdin = open("input.txt")

T = int(input())
for test_case in range(T):
    N = int(input())
    datas = list(map(int, input().strip().split()))
    
    max_num = datas[0]
    min_num = datas[0]
    
    for data in datas[1:]:
        if data > max_num:
            max_num = data
        if data < min_num:
            min_num = data
    print(f'#{test_case+1} {max_num-min_num}')