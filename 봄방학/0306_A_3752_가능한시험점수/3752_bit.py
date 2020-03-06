import sys
sys.stdin = open('input3752.txt')
# 비트연산 : 이전단계까지 누적 점수리스트 + 각 이번점수 를 누적 (|= 을통해서)
for tc in range(1,1+int(input())):
    d = input()
    data = map(int, input().split())
    a=1
    for grade in data:
        a |= a<<grade
    print('#%i'%tc,bin(a).count('1'))