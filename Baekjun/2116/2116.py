'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
>>>29
'''
def my_cnt(num1, num2):
    if (num1 == 6 and num2 == 5) or (num1 == 5 and num2 == 6):
        return 2
    if num1 == 6 or num2 == 6:
        return 1
    return 0

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
#0-5, 1-3, 2-4
com = [5, 3, 4, 1, 2, 0]
min_res = 1000000

for tc in range(6):
    res = 0
    down = dices[0][tc]
    head = dices[0][com[tc]]
    res += my_cnt(down, head)
    for i in range(1, N):
        down, head = head, dices[i][com[dices[i].index(head)]]
        res += my_cnt(down, head)
    min_res = res if res < min_res else min_res
print(N*6 - min_res)'''