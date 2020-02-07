'''
T
goal_digit_num (1~1000)
N개의 정수 (0~9)
---------------
가장 작은 정수 구하기.
1000개수 탐색
1. 0~9있는지 조사 : 1000
2. 1~9찾기 >>> 오른쪽에 0~9있는지 탐색 : 1000*2
3. 2번 + 오른쪽에.... : 1000*3
'''
import sys
sys.stdin = open('sample_input.txt')

def my_digit_check(number): #자릿수
    goal_digit_num = 1
    while number // (10 ** goal_digit_num) != 0:
        goal_digit_num += 1
    return goal_digit_num

def my_get_digit(number, n):
    return ( number // 10 ** (n-1) ) % 10

T = int(input())
for tc in range(1, T+1):
    numbers_length = int(input())
    numbers = []
    
    while len(numbers) != numbers_length:
        numbers.extend(list(map(int, input().split())))

    while_flag = True
    now_finish_flag = False
    result = 0
    goal_digit_num = my_digit_check(result)

    while while_flag:
        while_flag = False

        for idx in range(goal_digit_num - 1, numbers_length):
            n = 1
            now_find_digit = my_get_digit(result, n)

            while numbers[idx + 1 - n] == now_find_digit:
                if n == goal_digit_num :
                    now_finish_flag = True
                    break

                else:
                    n += 1
                    now_find_digit = my_get_digit(result, n)

            if now_finish_flag:
                result += 1
                while_flag = True
                now_finish_flag = False
                goal_digit_num = my_digit_check(result)
                break
    print(f'#{tc} {result}')