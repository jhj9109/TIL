'''
T = 10
--------입력------
T
8개 숫자 스플릿
--------감소규칙-----
1 2 3 4 5 1 2 3
4 5 1 2 3 4 5 1
2 3 4 5 1 2 3 4
5 1 2 3 4 5 1 2
3 4 5 1 2 3 4 5 =15
---------데이터----
n = 리스트형태, 8개
k = 감소수
---------동작-----
k = 1
flag = True
while flag:
    if n[0] - k < 0 :
        n[0] = 0
        flag = False
    else:
        n[0] -= k
    temp = n.pop(0)
    n.append(temp)
    k += 1
출력
'''
import sys
sys.stdin = open("input1225.txt")
T = 10
for _ in range(T):
    N = int(input())
    n = list(map(int, input().split()))

    k = 0
    flag = True
    while flag:
        if n[0] - (k % 5 + 1)  <= 0 :
            n[0] = 0
            flag = False
        else:
            n[0] -= (k % 5 + 1)
        n.append(n.pop(0))
        k += 1
    print(f"#{N} {' '.join(map(str, n))}")
