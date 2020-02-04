'''10:26시작
-----입력------
T
숫자판 , 교환횟수
-----데이터----------
n = 각자릿수
n_rank 
N = len(list(n))
change = 교환횟수
--------동작---------
역순으로 있는지 조사
아니면 역순으로 1개씩

n_rank = []
for i, v in enumerate(n):
    cnt = 0
    for com in n:
        if v < com:
            cnt += 1
    n_rank.append(cnt)
#n     = [ , , , , ]
#n_rank= [ , , , , ]

0~n-1자리

idx = 0
cnt = 0 # 바꾼횟수
while cnt != change or idx <= N-1:

    if n_rank[idx] <= idx:
        pass
    else :
        temp = n_rank.index(0)
        n[0], n[temp] = n[temp], n[0]
        n_rank[0], n_rank[temp] = n_rank[temp], n_rank[0]
        cnt += 1
    idx += 1

if (change - cnt) % 2: #홀수, 짝수면 pass
    n[-1], n[-2] = n[-2], n[-1]
print(f'#{T+1} {int(''.join(map(str, n)))}')
'''
import sys
sys.stdin = open('input2.txt')

'''
n 숫자가 자릿수로 나뉘어 저장되는 리스트
n_rank 각 숫자보다 큰 숫자의 갯수
change 바꿀 횟수 / cnt 바꾼 횟수
flag : False : 동일한 숫자가 있어, 최대값으로 잉여 change 소진 가능
'''
def my_index(list_data, val):
    print(f'list_data : {list_data}')
    while True:
        try:
            print(f'try : {val}')
            return list_data.index(val) + (val + 1) #보정치
        except ValueError:
            val -= 1

T = int(input())
for tc in range(T):
    n, change =input().split()

    N = len(n)
    n = list(map(int, n))
    change = int(change)

    n_rank = []
    for v in n:
        cnt = 0
        for com in n:
            if v < com:
                cnt += 1
        n_rank.append(cnt)
    print(f'n      : {n}')
    print(f'n_rank : {n_rank}')
    idx = 0
    cnt = 0
    flag = True
    ###print(f'0~{N-1} again')
    while cnt != change and idx <= N-1:
        print(f'idx:{idx}, cnt:{cnt}, change:{change},')
        if n_rank[idx] <= idx:
            if n_rank[idx] == idx:
                flag = False
        else :
            temp = my_index(n_rank[idx:], idx)
            print(f'temp:{temp}')
            n[idx], n[temp] = n[temp], n[idx]
            n_rank[idx], n_rank[temp] = n_rank[temp], n_rank[idx]
            cnt += 1
            print(n)
            print(n_rank)
        idx += 1
    ###print(n)
    if (change - cnt) % 2 and flag:
        n[-1], n[-2] = n[-2], n[-1]

    res = int(''.join(map(str, n)))
    print(f'#{tc+1} {res}')
#2,5,6,7,8,9,10

