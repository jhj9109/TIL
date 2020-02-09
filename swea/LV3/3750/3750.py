import sys
sys.stdin = open('sample_input.txt')

def my_digit_sum(num):
    result = 0
    while num // 10 != 0:
        result += num % 10
        num //= 10
    result += num % 10
    return result

T = int(input().strip())
for tc in range(1, T+1):
    n = int(input().strip())
    while n >= 10 :
        n = my_digit_sum(n)
    print(f'#{tc} {n}')