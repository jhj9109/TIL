'''
현미빵 A
단호박 B
은비 C원
많은 개수의 빵
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    result = C//A if A <= B else C//B
    print(f'#{tc} {result}')